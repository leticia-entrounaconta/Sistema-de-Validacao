def carregar_clientes() -> list[dict]:

    clientes = [
        {
            "nome": "Ana Souza",
            "cpf": "12345678901",
            "idade": 28,
            "ativo": True,
            "possui_permissao": True,
        },
        {
            "nome": "Bruno Lima",
            "cpf": "98765432100",
            "idade": 17,
            "ativo": True,
            "possui_permissao": True,
        },
        {
            "nome": "",
            "cpf": "45678912300",
            "idade": 35,
            "ativo": True,
            "possui_permissao": True,
        },
        {
            "nome": "Carla Mendes",
            "cpf": "123",
            "idade": 42,
            "ativo": True,
            "possui_permissao": True,
        },
        {
            "nome": "Diego Santos",
            "cpf": "74185296300",
            "idade": 30,
            "ativo": False,
            "possui_permissao": True,
        },
        {
            "nome": "Fernanda Alves",
            "cpf": "85296374100",
            "idade": 26,
            "ativo": True,
            "possui_permissao": False,
        },
    ]

    return clientes