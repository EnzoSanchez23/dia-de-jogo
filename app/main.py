from datetime import datetime, timedelta
from api import get_proximo_jogo
from utils import formatar_data_hora
import requests
from dotenv import load_dotenv
import os


# =========================
# Pushover
# =========================
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

    print(f"Faltam: {diferenca}")

    # janela de notificação (ajustada)
    if timedelta(minutes=55) <= diferenca <= timedelta(minutes=60):

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

        enviar_push(mensagem)

    else:
        print("Fora da janela de notificação.")


if __name__ == "__main__":
    main()