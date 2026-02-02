from playwright.sync_api import sync_playwright
from datetime import datetime
import requests
import os
from dotenv import load_dotenv

load_dotenv()

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
DATABASE_ID = os.getenv("DATABASE_ID")

if not NOTION_TOKEN or not DATABASE_ID:
    raise RuntimeError("Token ou Database ID não configurados")


headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json"
}

def criar_evento_notion(titulo, data_ddmmyyyy):
    payload = {
        "parent": {"database_id": DATABASE_ID},
        "properties": {
            "Nome": {
                "title": [{"text": {"content": titulo}}]
            },
            "Data": {
                "date": {
                    "start": datetime.strptime(
                        data_ddmmyyyy, "%d/%m/%Y"
                    ).date().isoformat()
                }
            }
        }
    }

    r = requests.post(
        "https://api.notion.com/v1/pages",
        headers=headers,
        json=payload
    )

    if r.status_code not in (200, 201):
        print("❌ ERRO Notion:", r.status_code, r.text)
        return False

    return True

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://gh.impconcursos.com.br/")
    page.get_by_label("Unidade *").select_option("asasul")
    page.get_by_label("Turno *").select_option("VESPERTINO")
    page.get_by_label("Escolha o curso *").select_option("275")
    page.locator("#grade").select_option("7")
    page.get_by_role("button", name="Ver grade horária").click()

    page.wait_for_selector("tbody tr")

    hoje = datetime.today().date()
    linhas = page.locator("//tbody/tr")

    for i in range(linhas.count()):
        linha = linhas.nth(i)

        small = linha.locator("small")
        if small.count() == 0:
            continue

        data_str = small.inner_text().strip()
        data = datetime.strptime(data_str, "%d/%m/%Y").date()

        if data <= hoje:
            continue

        conteudo = linha.locator("td:nth-child(2) div").inner_text()
        conteudo = " ".join(conteudo.split())

        ok = criar_evento_notion(conteudo, data_str)
        if ok:
            print(f"✔ Criado no Notion: {data_str} - {conteudo}")

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
