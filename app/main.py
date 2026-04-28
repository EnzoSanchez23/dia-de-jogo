from api import get_proximo_jogo
from utils import formatar_data_hora


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

🏆 {jogo["campeonato"]}
🆚 {jogo["mandante"]} x {jogo["visitante"]}
📅 {data_formatada}
⌚ {hora_formatada}

""".strip()

    print(mensagem)


if __name__ == "__main__":
    main()