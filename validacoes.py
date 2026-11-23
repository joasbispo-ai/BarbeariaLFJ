from datetime import datetime, timedelta

HORARIOS_PADRAO = [
    "09:00", "09:40", "10:20", "11:00", "11:40",
    "13:30", "14:10", "14:50", "15:30", "16:10",
    "16:50", "17:30", "18:10", "18:50"
]

DIAS_SEMANA = {
    0: "Seg",
    1: "Ter",
    2: "Qua",
    3: "Qui",
    4: "Sex",
    5: "Sáb",
    6: "Dom"
}


def ler_texto_obrigatorio(mensagem):
    """Garante que o usuário não deixe campos obrigatórios em branco."""
    while True:
        valor = input(mensagem).strip()
        if valor:
            return valor
        print("Erro: Este campo não pode ficar vazio. Tente novamente.")


def ler_valor_monetario(mensagem):
    """Valida se o preço digitado é um número positivo."""
    while True:
        entrada = input(mensagem).strip().replace(",", ".")
        try:
            valor = float(entrada)
            if valor > 0:
                return valor
            print("Erro: O valor do serviço deve ser maior que zero.")
        except ValueError:
            print("Erro: Digite um valor numérico válido (ex: 35.00).")


def ler_id_valido(mensagem):
    """Garante que o ID informado seja um número inteiro positivo."""
    while True:
        entrada = input(mensagem).strip()
        if entrada.isdigit() and int(entrada) > 0:
            return int(entrada)
        print("Erro: Informe um ID numérico válido.")


def escolher_data_calendario(dias_a_frente=14):
    """Exibe opções de datas a partir de hoje e retorna um objeto date."""
    hoje = datetime.now().date()
    opcoes_datas = [hoje + timedelta(days=i) for i in range(dias_a_frente)]

    while True:
        print("\n--- SELECIONE A DATA (CALENDÁRIO) ---")
        for idx, d in enumerate(opcoes_datas, start=1):
            dia_semana = DIAS_SEMANA[d.weekday()]
            rotulo_extra = " (Hoje)" if d == hoje else ""
            print(f"{idx:2d} - {d.strftime('%d/%m/%Y')} ({dia_semana}){rotulo_extra}")

        escolha = input("Escolha o número da data: ").strip()
        if escolha.isdigit():
            indice = int(escolha) - 1
            if 0 <= indice < len(opcoes_datas):
                return opcoes_datas[indice]

        print("Erro: Selecione um número válido da lista de datas.")


def escolher_horario(data_escolhida):
    """Exibe opções de horários e impede escolher horário passado no dia de hoje."""
    agora = datetime.now()
    horarios_disponiveis = []

    for h_str in HORARIOS_PADRAO:
        hora, minuto = map(int, h_str.split(":"))
        dt_opcao = datetime(
            year=data_escolhida.year,
            month=data_escolhida.month,
            day=data_escolhida.day,
            hour=hora,
            minute=minuto
        )
        if data_escolhida == agora.date() and dt_opcao <= agora:
            continue
        horarios_disponiveis.append(h_str)

    if not horarios_disponiveis:
        print("\nNão há mais horários disponíveis para a data selecionada.")
        return None

    while True:
        print(f"\n--- HORÁRIOS DISPONÍVEIS ({data_escolhida.strftime('%d/%m/%Y')}) ---")
        for idx, horario in enumerate(horarios_disponiveis, start=1):
            print(f"{idx:2d} - {horario}")

        escolha = input("Escolha o número do horário: ").strip()
        if escolha.isdigit():
            indice = int(escolha) - 1
            if 0 <= indice < len(horarios_disponiveis):
                return horarios_disponiveis[indice]

        print("Erro: Selecione um número válido da lista de horários.")