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