from dados import carregar_clientes
from processamento import processar_clientes
from relatorios import exibir_resultados, exibir_resumo, gerar_resumo


def main() -> None:
    """
    Executa o fluxo principal do sistema de processamento de clientes.

    Returns:
        None.
    """

    print("INICIANDO PROCESSAMENTO DE CLIENTES")

    clientes = carregar_clientes()

    resultados = processar_clientes(clientes)

    exibir_resultados(resultados)

    resumo = gerar_resumo(resultados)

    exibir_resumo(resumo)

    print("PROCESSAMENTO FINALIZADO")


if __name__ == "__main__":
    main()