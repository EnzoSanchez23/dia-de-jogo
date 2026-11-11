# ⚽ Dia de Jogo - Notificador Automático de Partidas

Script em Python que monitora a agenda do seu time do coração e envia notificações automáticas no Telegram (e Pushover) antes do início da partida.

---

## 🚀 O que faz

- 🔍 Busca automaticamente a próxima partida via **TheSportsDB API**.
- 🌐 Converte o horário UTC da API para o fuso horário oficial de Brasília (`America/Sao_Paulo`).
- ⏱️ Calcula a janela ideal de notificação (1h30 a 2h antes do jogo).
- 📲 Envia notificações diretas via **Telegram Bot** (com formatação HTML) e **Pushover**.
- 🔄 Automação serverless executando a cada 30 minutos via **GitHub Actions**.

---

## 🛠️ Tecnologias

- **Python 3.11+**
- [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI) (Telebot)
- Requests & Python-Dotenv
- **GitHub Actions** (Workflow de Agendamento/Cron)
- **TheSportsDB API**

---

## 📂 Estrutura do Projeto

```text
dia-de-jogo/
├── .github/
│   └── workflows/
│       └── notificacao_jogo.yml
├── app/
│   ├── main.py
│   ├── api.py
│   └── utils.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Configuração Local

### 1. Clonar o repositório

```bash
git clone https://github.com/EnzoSanchez23/dia-de-jogo.git
cd dia-de-jogo
```

### 2. Instalar as dependências

```bash
pip install -r requirements.txt
```

*(Caso não tenha o `requirements.txt`, instale via: `pip install pyTelegramBotAPI requests python-dotenv`)*

---

### 3. Configurar variáveis de ambiente (`.env`)

Crie um arquivo `.env` na raiz do projeto baseado no `.env.example`:

```env
# Telegram
TELEGRAM_TOKEN=seu_token_do_botfather
TELEGRAM_USER_ID=seu_chat_id_numerico

# Time & API
TEAM_ID=134284
TEAM_NAME=Corinthians
API_SPORTSDB=sua_api_key

# Pushover (Opcional)
PUSHOVER_TOKEN=seu_token_pushover
PUSHOVER_USER=seu_user_pushover

# Configurações
DEBUG=True
```

---

### 4. Como obter as credenciais

#### 🤖 Telegram Bot & User ID
1. Fale com o [@BotFather](https://t.me/BotFather) no Telegram para criar seu bot e obter o `TELEGRAM_TOKEN`.
2. Dê `/start` no seu novo bot.
3. Obtenha seu ID numérico acessando [@userinfobot](https://t.me/userinfobot) e salve no `TELEGRAM_USER_ID`.

#### ⚽ Team ID (TheSportsDB)
- **Opção 1 (Site):** Acesse [TheSportsDB](https://www.thesportsdb.com/), pesquise seu time e pegue o ID na URL (`.../team/134284-Corinthians` → `134284`).
- **Opção 2 (API):** Acesse `https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Corinthians` e busque pela chave `"idTeam"`.

---

## ▶️ Executando Localmente

```bash
python app/main.py
```

---

## 🔄 Automação com GitHub Actions

O projeto roda automaticamente no GitHub Actions a cada 30 minutos. Para que a automação funcione sem expor seus tokens:

1. Acesse o seu repositório no GitHub.
2. Vá em **Settings** → **Secrets and variables** → **Actions** → **New repository secret**.
3. Adicione as seguintes variáveis:

| Secret | Descrição |
| :--- | :--- |
| `TELEGRAM_TOKEN` | Token retornado pelo BotFather |
| `TELEGRAM_USER_ID` | Seu ID numérico no Telegram |
| `TEAM_ID` | ID do time na TheSportsDB |
| `TEAM_NAME` | Nome exato do time para filtro |
| `API_SPORTSDB` | Chave de API da TheSportsDB |
| `PUSHOVER_TOKEN` | (Opcional) Token do aplicativo Pushover |
| `PUSHOVER_USER` | (Opcional) Chave de usuário Pushover |

### Disparo Manual
Você também pode disparar a notificação a qualquer momento na aba **Actions** → **Notificacao Jogo Corinthians** → **Run workflow**.

---

## 📱 Exemplo de Notificação Recebida

```text
⚽ Dia de Corinthians!

🆚 Corinthians x Santos
🏆 Campeonato Brasileiro
📅 18/05/2026
🕰️ 16:00
```

---

## 🧑‍💻 Autor

Desenvolvido por **[Enzo Sanchez](https://github.com/EnzoSanchez23)**.