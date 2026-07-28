from dados import carregar_clientes


def main() -> None:

    clientes = carregar_clientes()

    print(clientes)


if __name__ == "__main__":
    main()