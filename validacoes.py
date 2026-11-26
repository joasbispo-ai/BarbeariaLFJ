"""

MÓDULO DE VALIDAÇÃO DE ENTRADAS (RF06) - BARBEARIA LFJ

RESUMO PARA A EQUIPE - COMO ESTE ARQUIVO FUNCIONA:

1. Primeira Barreira Contra Dados Inválidos:
   - Todas as funções usam loops (`while True`) que repetem a pergunta até o
     usuário digitar algo válido. Isso evita erros no Python e evita que dados
     inconsistentes sejam enviados para o MySQL Workbench.

2. Validação de Texto Obrigatório (`ler_texto_obrigatorio`):
   - Aplica `.strip()` para remover espaços em branco nas pontas. Se o usuário
     apertar Enter ou digitar apenas espaços, o campo é considerado vazio e
     a pergunta é repetida.

3. Validação de Valor Monetário (`ler_valor_monetario`):
   - Aceita tanto vírgula quanto ponto decimal (ex: `35,00` ou `35.00`),
     converte para `float` dentro de um `try / except ValueError` e exige que
     o valor seja maior que zero (`> 0`).

4. Validação de ID (`ler_id_valido`):
   - Garante que o identificador informado seja composto apenas por dígitos e
     represente um número inteiro positivo (`> 0`), evitando erros ao buscar,
     atualizar ou excluir agendamentos.

"""


def ler_texto_obrigatorio(mensagem):
    """
    Solicita uma informação textual e exige que não fique em branco.
    Remove espaços extras nas extremidades com .strip().
    """
    while True:
        # Lê a entrada do usuário e remove espaços antes e depois do texto
        valor = input(mensagem).strip()

        # Strings não vazias são avaliadas como True em Python
        if valor:
            return valor

        print("Erro: Este campo não pode ficar vazio. Tente novamente.")


def ler_valor_monetario(mensagem):
    """
    Lê um valor financeiro e converte para float positivo.
    Troca vírgula por ponto para facilitar a digitação no padrão brasileiro.
    """
    while True:
        # Normaliza vírgula para ponto e remove espaços extras
        entrada = input(mensagem).strip().replace(",", ".")

        try:
            valor = float(entrada)

            # Impede valores zerados ou negativos para preços de serviços
            if valor > 0:
                return valor

            print("Erro: O valor do serviço deve ser maior que zero.")
        except ValueError:
            # Captura entradas com letras ou símbolos inválidos para conversão float
            print("Erro: Digite um valor numérico válido (ex: 35.00 ou 35,00).")


def ler_id_valido(mensagem):
    """
    Garante que o ID informado seja um número inteiro positivo.
    Evita falhas ao consultar ou alterar registros na tabela 'agendamentos'.
    """
    while True:
        entrada = input(mensagem).strip()

        # .isdigit() retorna True apenas se todos os caracteres forem dígitos numéricos (0-9)
        if entrada.isdigit() and int(entrada) > 0:
            return int(entrada)

        print("Erro: Informe um ID numérico válido.")