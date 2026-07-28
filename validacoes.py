from constantes import (
    IDADE_MINIMA,
    MENSAGEM_CLIENTE_VALIDO,
    MENSAGEM_NOME_INVALIDO,
    MENSAGEM_CPF_INVALIDO,
    MENSAGEM_IDADE_INVALIDA,
    MENSAGEM_CLIENTE_INATIVO,
    MENSAGEM_SEM_PERMISSAO,
)


def validar_nome(nome: str) -> bool: #str -> (string) aqui espera que esperamos receber um texto
                                     #bool -> retorna que a função deve voltar uma valor booleano (t/f)
    
    if not isinstance(nome, str): #verifica se o nome n é uma string
        return False

    nome = nome.strip() #remove os espaços do incio final de uma string

    if len(nome) < 3: #min 3 caracteres
        return False

    return True


def validar_cpf(cpf: str) -> bool:

    if not isinstance(cpf, str):
        return False

    if len(cpf) != 11:     #verificar cpf 11 caracteres
        return False

    if not cpf.isdigit(): #verificando se é apenas números
        return False

    return True


def validar_idade(
    idade: int,
    idade_minima: int = IDADE_MINIMA,
) -> bool:
   
    if not isinstance(idade, int):
        return False

    if idade < idade_minima:
        return False

    return True


def validar_cliente(cliente: dict) -> tuple[bool, str]: #a função retorna uma tupla com dois valores

    nome = cliente.get("nome")  #get buscar um valor dicionário por meio de sua chave
    cpf = cliente.get("cpf")
    idade = cliente.get("idade")
    ativo = cliente.get("ativo")
    possui_permissao = cliente.get("possui_permissao")

    if not validar_nome(nome):
        return False, MENSAGEM_NOME_INVALIDO

    if not validar_cpf(cpf):
        return False, MENSAGEM_CPF_INVALIDO

    if not validar_idade(
        idade,
        idade_minima=IDADE_MINIMA,
    ):
        return False, MENSAGEM_IDADE_INVALIDA

    if ativo is not True:
        return False, MENSAGEM_CLIENTE_INATIVO

    if possui_permissao is not True:
        return False, MENSAGEM_SEM_PERMISSAO

    return True, MENSAGEM_CLIENTE_VALIDO