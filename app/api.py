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