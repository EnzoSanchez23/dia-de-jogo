from string import templatelib
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from api import get_proximo_jogo
import requests
from dotenv import load_dotenv
import os
import telebot


# =========================
# CONFIG
# =========================
load_dotenv()
DEBUG = True


# Timezones reais
UTC_TZ = ZoneInfo("UTC")
BRAZIL_TZ = ZoneInfo("America/Sao_Paulo")
TEAM_NAME = os.getenv("TEAM_NAME")

if not TEAM_NAME:
    raise ValueError("TEAM_NAME não definido no .env")

TELEGRAM_KEY = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_USER_ID = os.getenv("TELEGRAM_USER_ID")

# =========================
# PUSHOVER
# =========================
def enviar_push(mensagem):
    res = requests.post(
        "https://api.pushover.net/1/messages.json",
        data={
            "token": os.getenv("PUSHOVER_TOKEN"),
            "user": os.getenv("PUSHOVER_USER"),
            "message": mensagem,
        },
    )

    if DEBUG:
        print(f"Push status: {res.status_code}")


#==========================
# TELEGRAM
#==========================
# Criando o objeto do BOT
bot = telebot.TeleBot(TELEGRAM_KEY)

def msg_telegram(mensagem):
    try:
        bot.send_message(TELEGRAM_USER_ID, mensagem, disable_notification=False)
        print("Msg enviada!")
    except Exception as e:
        print(f'Erro: {e}')


# =========================
# MAIN
# =========================
def main():
    jogo = get_proximo_jogo()

    if not jogo:
        if DEBUG:
            print("Nenhum jogo encontrado")
        return


    # Horário da API agora é tratado como UTC
    dt_jogo = datetime.strptime(
        f"{jogo['data']} {jogo['hora']}",
        "%Y-%m-%d %H:%M:%S"
    )


    # Define horário UTC
    dt_jogo = dt_jogo.replace(tzinfo=UTC_TZ)


    # Converte UTC → Brasil
    dt_jogo = dt_jogo.astimezone(BRAZIL_TZ)

    agora = datetime.now(BRAZIL_TZ)

    diferenca = dt_jogo - agora

    if DEBUG:
        print(f"Agora Brasil: {agora}")
        print(f"Jogo Brasil: {dt_jogo}")
        print(f"Faltam: {diferenca}")

    
    # Janela de notificação
    #if timedelta(minutes=0) <= diferenca <= timedelta(hours=2):
    if DEBUG:

        if DEBUG:
            print("🔔 Hora de notificar!")


        # Identifica corretamente seu time
        if TEAM_NAME.lower() in jogo["mandante"].lower():
            meu_time = jogo["mandante"]
        else:
            meu_time = jogo["visitante"]


        # Formata usando horário convertido
        data_formatada = dt_jogo.strftime("%d/%m/%Y")
        hora_formatada = dt_jogo.strftime("%H:%M")

        mensagem = f"""
⚽ Dia de {meu_time}!

🆚 {jogo["mandante"]} x {jogo["visitante"]}
🏆 {jogo["campeonato"]}
📅 {data_formatada}
🕰️ {hora_formatada}
""".strip()

        #enviar_push(mensagem)
        msg_telegram(mensagem)

    else:
        if DEBUG:
            print("Fora da janela de notificação")


if __name__ == "__main__":
    main()