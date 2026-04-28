import requests
from datetime import datetime
from dotenv import load_dotenv
import os

# =========================
# CONFIG
# =========================
load_dotenv()
API_KEY = os.getenv("api_sportsdb")
TEAM_ID = "134284"  # Corinthians


# =========================
# BUSCAR PRÓXIMO JOGO
# =========================
def get_proximo_jogo():
    url = f"https://www.thesportsdb.com/api/v1/json/{API_KEY}/eventsnext.php?id={TEAM_ID}"

    res = requests.get(url)
    data = res.json()

    eventos = data.get("events")

    if not eventos:
        return None

    jogo = eventos[0]

    # prioridade para horário local
    data_str = jogo.get("dateEventLocal") or jogo.get("dateEvent")
    hora_str = jogo.get("strTimeLocal") or jogo.get("strTime")

    return {
        "campeonato": jogo.get("strLeague"),
        "mandante": jogo.get("strHomeTeam"),
        "visitante": jogo.get("strAwayTeam"),
        "data": data_str,
        "hora": hora_str,
    }


# =========================
# FORMATAR DATA E HORA
# =========================
def formatar_data_hora(data, hora):
    # transformar string em datetime
    dt = datetime.strptime(f"{data} {hora}", "%Y-%m-%d %H:%M:%S")

    # formatar
    data_formatada = dt.strftime("%d/%m/%Y")
    hora_formatada = dt.strftime("%H:%M")

    return data_formatada, hora_formatada


# =========================
# MAIN
# =========================
def main():
    jogo = get_proximo_jogo()

    if not jogo:
        print("Nenhum jogo encontrado")
        return

    data_formatada, hora_formatada = formatar_data_hora(
        jogo["data"], jogo["hora"]
    )

    mensagem = f"""
⚽ Dia de Corinthians!

🆚 {jogo["mandante"]} x {jogo["visitante"]}
🏆 {jogo["campeonato"]}
📅 {data_formatada}
⌚ {hora_formatada}

📺 Transmissão:
""".strip()

    print(mensagem)


# =========================
# EXECUÇÃO
# =========================
if __name__ == "__main__":
    main()