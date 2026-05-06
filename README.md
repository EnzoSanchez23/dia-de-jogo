# ⚽ Dia de Jogo - Notificador de Jogos

Script em Python que monitora o próximo jogo de um time e envia uma notificação no celular antes da partida.

---

## 🚀 O que faz

* Busca o próximo jogo via API
* Calcula o tempo até a partida
* Envia notificação automática

---

## 🛠️ Tecnologias

* Python
* requests
* python-dotenv
* GitHub Actions
* Pushover

---

## 📂 Estrutura

```
app/
 ├── main.py
 ├── api.py
 ├── utils.py
```

---

## ⚙️ Configuração

### 1. Clonar o projeto

```
git clone <seu-repo>
cd <seu-repo>
```

---

### 2. Criar arquivo `.env`

Use o arquivo de exemplo:

```
cp .env.example .env
```

Depois edite o `.env` com suas credenciais:

```
API_SPORTSDB=sua_api_key
PUSHOVER_TOKEN=seu_token
PUSHOVER_USER=seu_user
TEAM_ID=id_do_time
```

---

### 3. Instalar dependências

```
pip install requests python-dotenv
```

---

## ▶️ Rodar localmente

```
python app/main.py
```

---

## 🔄 Automação

O projeto roda automaticamente usando GitHub Actions.

⚠️ Observação: o agendamento pode sofrer atrasos (limitação da plataforma).

---

## 📱 Exemplo de notificação

```
⚽ Dia de Jogo!

🆚 Time A x Time B
🏆 Campeonato
📅 xx/xx/2026
🕰️ 20:30
```

---

## 📌 Observações

* O `TEAM_ID` define qual time será monitorado
* Pode ser alterado no `.env` ou nos Secrets do GitHub
* Projeto simples focado em estudo e portfólio

---

## 🧑‍💻 Autor

Projeto desenvolvido para aprendizado.
