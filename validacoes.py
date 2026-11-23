def ler_texto_obrigatorio(mensagem):
    """Garante que o usuário não deixe campos obrigatórios em branco."""
    while True:
        valor = input(mensagem).strip()
        if valor:
            return valor
        print("Erro: Este campo não pode ficar vazio. Tente novamente.")
        
def ler_valor_monetario(mensagem):
    """Valida se o preço digitado é número positivo."""
    while True:
        entrada - input(mensagem).strip()replace(",", ".")
        try:
            valor = float(entrada)
            if valor >= 0:
                return valor
            print("Erro: O valor do serviço deve ser maior que zero.")
        except ValueError:
            print("Erro: Digite um valor numérico válido (ex: 35.00).")
def ler_id_valido(mensagem):
    """"Garante que o ID informado seja um número inteiro positivo."""
    while True:
        entrada = input(mensagem).strip()
        if entrada.isdigit() and int(entrada) > 0:
            return int(entrada)
        print("Erro: Digite um ID válido (número inteiro positivo).")