from datetime import datetime, timedelta
from api import get_proximo_jogo
from utils import formatar_data_hora
import requests
from dotenv import load_dotenv
import os


# =========================
# CONTROLE DE NOTIFICAÇÃO
# =========================
def salvar_notificado(event_id):
    with open("notificado.txt", "w") as f:
        f.write(event_id)


def ja_notificado(event_id):
    try:
        with open("notificado.txt", "r") as f:
            return f.read() == event_id
    except FileNotFoundError:
        return False


#==========================
# Pushover
#==========================
load_dotenv()
def enviar_push(mensagem):
    requests.post(
        "https://api.pushover.net/1/messages.json",
        data={
            "token": os.getenv("pushover_token_key"),
            "user": os.getenv("pushover_user_key"),
            "message": mensagem,
        },
    )

# =========================
# MAIN
# =========================
def main():
    jogo = get_proximo_jogo()

    if not jogo:
        print("Nenhum jogo encontrado")
        return

    # converter data/hora para datetime
    dt_jogo = datetime.strptime(
        f"{jogo['data']} {jogo['hora']}",
        "%Y-%m-%d %H:%M:%S"
    )

    agora = datetime.now()
    diferenca = dt_jogo - agora

    #print(f"Agora: {agora}")
    #print(f"Jogo: {dt_jogo}")
    #print(f"Faltam: {diferenca}")

    # janela de 1 hora (com margem)
    #if timedelta(minutes=55) <= diferenca <= timedelta(minutes=65):
    if True:

        if ja_notificado(jogo["id"]):
            #print("Já notificado anteriormente.")
            return

        print("🔔 Hora de notificar!")

        data_formatada, hora_formatada = formatar_data_hora(
            jogo["data"], jogo["hora"]
        )

        mensagem = f"""
⚽ Dia de Corinthians!

🆚 {jogo["mandante"]} x {jogo["visitante"]}
🏆 {jogo["campeonato"]}
📅 {data_formatada}
⌚ {hora_formatada}
""".strip()

        #print(mensagem)
        enviar_push(mensagem)
        salvar_notificado(jogo["id"])

    else:
        print("Ainda não está na janela de notificação.")


if __name__ == "__main__":
    main()