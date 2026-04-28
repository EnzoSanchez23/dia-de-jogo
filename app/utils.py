from datetime import datetime


def formatar_data_hora(data, hora):
    dt = datetime.strptime(f"{data} {hora}", "%Y-%m-%d %H:%M:%S")

    data_formatada = dt.strftime("%d/%m/%Y")
    hora_formatada = dt.strftime("%H:%M")

    return data_formatada, hora_formatada