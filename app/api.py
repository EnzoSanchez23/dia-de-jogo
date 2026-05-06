import requests
from datetime import datetime
from dotenv import load_dotenv
import os

# =========================
# CONFIG
# =========================
load_dotenv() #Carrega o .env
API_KEY = os.getenv("API_SPORTSDB") #Pega a key pelo .env
TEAM_ID = os.getenv("TEAM_ID")

if not TEAM_ID:
    raise ValueError("TEAM_ID não definido no .env")

# =========================
# BUSCAR PRÓXIMO JOGO
# =========================
def get_proximo_jogo():
    url = f"https://www.thesportsdb.com/api/v1/json/{API_KEY}/eventsnext.php?id={TEAM_ID}"

    res = requests.get(url)
    data = res.json() #Tranforma a resposta em um JSON

    eventos = data.get("events") #Dentro do JSON, ele pega a CHAVE "events"

    if not eventos:
        return None

    jogo = eventos[0] #Dentro da CHAVE "events", ele pega o indice 0 da lista (dic -> list -> dic)

    # prioridade para horário local
    data_str = jogo.get("dateEventLocal") or jogo.get("dateEvent")
    hora_str = jogo.get("strTimeLocal") or jogo.get("strTime")

    return {
        "id": jogo.get("idEvent"),
        "campeonato": jogo.get("strLeague"),
        "mandante": jogo.get("strHomeTeam"),
        "visitante": jogo.get("strAwayTeam"),
        "data": data_str,
        "hora": hora_str,
    }