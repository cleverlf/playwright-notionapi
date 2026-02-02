# 📅 Automação de Grade Horária → Notion

Este projeto automatiza a coleta da **grade horária** do site da IMP Concursos utilizando **Playwright (Python)** e sincroniza os dados com um **calendário no Notion** via API.

✔ Inclui dias com aula
✔ Inclui dias **SEM AULA**
✔ Cria eventos no calendário automaticamente
✔ Dados sensíveis protegidos (token fora do código)

---

## 🛠️ Tecnologias utilizadas

* Python 3.10+
* Playwright
* Requests
* python-dotenv
* Notion API

---

## 📂 Estrutura do projeto

```
python-fundamentos/
 ├── gh.py
 ├── .env            # NÃO versionado
 ├── .gitignore
 ├── README.md
```

---

## 🔐 Configuração de variáveis de ambiente

### 1️⃣ Criar arquivo `.env`

Na raiz do projeto, crie um arquivo chamado `.env`:

```env
NOTION_TOKEN=xxxxxxxxxxxxxxxxxxxxxxxxx
NOTION_DATABASE_ID=xxxxxxxxxxxxxxxxxxx
```

⚠️ **Nunca versionar esse arquivo**.

---

### 2️⃣ Garantir que o `.env` não vá para o Git

No arquivo `.gitignore`:

```gitignore
.env
```

---

## 📦 Instalação das dependências

Crie e ative um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
```

Instale as dependências:

```bash
pip install playwright requests python-dotenv
```

Instale o navegador do Playwright:

```bash
playwright install chromium
```

---

## ⚙️ Configuração no Notion

### 1️⃣ Criar integração

* Notion → Settings → Integrations
* Criar integração interna
* Copiar o **Internal Integration Token**

### 2️⃣ Criar database do tipo calendário

O database deve conter:

* Um campo do tipo **Title** (ex: `Name`)
* Um campo do tipo **Date** (ex: `Data`)

### 3️⃣ Compartilhar o database

* Abrir o database
* Clicar em **Share**
* Adicionar a integração criada

---

## ▶️ Executando o script

```bash
python gh.py
```

O script irá:

* Acessar o site
* Filtrar a grade horária
* Ler todas as datas futuras
* Criar eventos no calendário do Notion
* Incluir dias **SEM AULA**

---

## 📅 Exemplo de eventos criados no Notion

* `DAS 14H15 ÀS 17H50 FLÁVIO ASSIS AFO + LRF 6/18`
* `SEM AULA`

Todos com **data sem hora**.

---

## 🧪 Observações importantes

* O Notion pode exigir **atualização da página (F5)** para refletir novos eventos
* Rodar o script mais de uma vez pode gerar **eventos duplicados**
* Recomenda-se implementar verificação de duplicidade se for uso contínuo

---

## 🚀 Próximos aprimoramentos (opcional)

* Evitar eventos duplicados
* Atualizar eventos existentes
* Agendamento automático (Windows Task Scheduler / cron)
* Geração de executável `.exe`
* Logs em arquivo

---

## 🔒 Segurança

* Tokens **não ficam no código**
* `.env` é ignorado pelo Git
* Integração pode ser revogada a qualquer momento

---

## 📄 Licença

Projeto de uso educacional e pessoal.

