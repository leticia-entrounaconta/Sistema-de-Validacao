from constantes import STATUS_ERRO, STATUS_PROCESSADO


def exibir_resultados(resultados: list[dict]) -> None:
    

    for resultado in resultados: #percorrendo cada resultado
        nome = resultado.get("nome")
        cpf = resultado.get("cpf")
        status = resultado.get("status")
        mensagem = resultado.get("mensagem")

        if not nome:        #tratando nome vazio
            nome = "Não informado"

        print("-" * 50)
        print(f"Cliente: {nome}")
        print(f"CPF: {cpf}")        #inserir variável dentro do texto 
        print(f"Status: {status}")
        print(f"Mensagem: {mensagem}")


def gerar_resumo(resultados: list[dict]) -> dict:
    

    total = len(resultados)
    processados = 0
    erros = 0

    for resultado in resultados:
        status = resultado.get("status")

        if status == STATUS_PROCESSADO:
            processados += 1
        elif status == STATUS_ERRO:
            erros += 1

    if total > 0:
        percentual_sucesso = processados / total * 100
    else:
        percentual_sucesso = 0.0

    return {
        "total": total,
        "processados": processados,
        "erros": erros,
        "percentual_sucesso": percentual_sucesso,
    }


def exibir_resumo(resumo: dict) -> None:
    

    total = resumo.get("total", 0)
    processados = resumo.get("processados", 0)
    erros = resumo.get("erros", 0)
    percentual_sucesso = resumo.get("percentual_sucesso", 0.0)

    print("=" * 50)
    print("RESUMO DO PROCESSAMENTO")
    print("=" * 50)
    print(f"Total de clientes: {total}")
    print(f"Processados com sucesso: {processados}")
    print(f"Clientes com erro: {erros}")
    print(f"Percentual de sucesso: {percentual_sucesso:.2f}%")
    print("=" * 50)