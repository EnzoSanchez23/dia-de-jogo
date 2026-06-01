# ⚽ Dia de Jogo - Notificador de Jogos

Script em Python que monitora o próximo jogo de um time e envia uma notificação no celular antes da partida.

---

## 🚀 O que faz

* Busca o próximo jogo via API
* Converte automaticamente horários para o fuso de Brasília (quando necessário)
* Calcula o tempo até a partida
* Envia notificações automáticas para o celular
* Pode ser executado localmente ou via GitHub Actions

---

## 🛠️ Tecnologias

* Python
* requests
* python-dotenv
* GitHub Actions
* TheSportsDB API
* Pushover

---

## 📂 Estrutura

```text
app/
 ├── main.py
 ├── api.py
 ├── utils.py
```

---

## ⚙️ Configuração

### 1. Clonar o projeto

```bash
git clone https://github.com/EnzoSanchez23/dia-de-jogo.git
cd dia-de-jogo
```

---

### 2. Criar arquivo `.env`

Use o arquivo de exemplo:

```bash
cp .env.example .env
```

Depois edite o `.env` com suas credenciais:

```env
API_SPORTSDB=sua_api_key
PUSHOVER_TOKEN=seu_token
PUSHOVER_USER=seu_user
TEAM_ID=id_do_time
TEAM_NAME=nome_do_time
```

---

### 3. Como descobrir o TEAM_ID

A API utilizada é a TheSportsDB.

Existem duas formas de encontrar o ID do time.

#### Opção 1 - Pelo site da TheSportsDB (mais simples)

Acesse:

```text
https://www.thesportsdb.com/
```

Pesquise pelo nome do time e abra sua página.

Na URL será exibido o ID da equipe.

Exemplo:

```text
https://www.thesportsdb.com/team/134284-Corinthians
```

Nesse caso:

```env
TEAM_ID=134284
```

---

#### Opção 2 - Pela API

Faça uma busca pelo nome do time:

```text
https://www.thesportsdb.com/api/v1/json/SUA_API_KEY/searchteams.php?t=Corinthians
```

Na resposta JSON procure por:

```json
"idTeam": "134284"
```

Utilize esse valor no `.env`:

```env
TEAM_ID=134284
```

---

### 4. Instalar dependências

```bash
pip install requests python-dotenv
```

---

## ▶️ Rodar localmente

```bash
python app/main.py
```

---

## 🔄 Automação com GitHub Actions

O projeto pode ser executado automaticamente através do GitHub Actions.

Para isso, adicione os seguintes Secrets no repositório:

```text
API_SPORTSDB
TEAM_ID
TEAM_NAME
PUSHOVER_TOKEN
PUSHOVER_USER
```

Caminho:

```text
Settings
→ Secrets and variables
→ Actions
→ New repository secret
```

Após configurados, o workflow executará automaticamente conforme o cron definido no arquivo:

```text
.github/workflows/notificador.yml
```

Também é possível executar manualmente pela aba:

```text
Actions
→ Run workflow
```

⚠️ Observação: o GitHub Actions gratuito pode apresentar atrasos na execução dos workflows agendados.

---

## 📱 Pushover

As notificações são enviadas utilizando o Pushover.

Site oficial:

https://pushover.net

Para utilizar o serviço é necessário criar uma conta e gerar:

* PUSHOVER_TOKEN
* PUSHOVER_USER

⚠️ O Pushover oferece aproximadamente 30 dias de teste gratuito. Após esse período é necessário adquirir uma licença para continuar recebendo notificações.

---

## 📱 Exemplo de notificação

```text
⚽ Dia de Corinthians!

🆚 Corinthians x Santos
🏆 Campeonato Brasileiro
📅 18/05/2026
🕰️ 16:00
```

---

## 📌 Observações

* O `TEAM_ID` define qual time será monitorado
* O `TEAM_NAME` é utilizado para personalizar as mensagens
* Pode ser alterado no `.env` ou nos Secrets do GitHub
* Projeto simples focado em estudo e portfólio

---

## 🧑‍💻 Autor

Projeto desenvolvido para aprendizado.
