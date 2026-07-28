from constantes import STATUS_ERRO, STATUS_PROCESSADO
from validacoes import validar_cliente


def processar_cliente(cliente: dict) -> dict:

    cliente_valido, mensagem_validacao = validar_cliente(cliente)

    nome = cliente.get("nome")
    cpf = cliente.get("cpf")

    if cliente_valido:
        return {
            "nome": nome,
            "cpf": cpf,
            "status": STATUS_PROCESSADO,
            "mensagem": "Cliente processado com sucesso",
        }

    return {
        "nome": nome,
        "cpf": cpf,
        "status": STATUS_ERRO,
        "mensagem": mensagem_validacao,
    }


def processar_clientes(clientes: list[dict]) -> list[dict]:
   
    resultados = []

    for cliente in clientes:
        resultado = processar_cliente(cliente)
        resultados.append(resultado)

    return resultados