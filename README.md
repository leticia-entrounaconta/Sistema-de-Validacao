# Sistema de Validação de Clientes

Projeto desenvolvido em Python para praticar funções, validações, organização do código em módulos e processamento de listas de clientes.

O sistema carrega uma lista de clientes, valida os dados obrigatórios, registra o resultado de cada processamento e apresenta um resumo no terminal.

## Funcionalidades

O programa realiza as seguintes validações:

- Nome preenchido e com pelo menos três caracteres;
- CPF com exatamente 11 números;
- Idade mínima de 18 anos;
- Cliente ativo;
- Cliente com permissão de acesso.

Ao final, o sistema apresenta:

- Resultado individual de cada cliente;
- Quantidade total de clientes;
- Quantidade de clientes processados;
- Quantidade de clientes com erro;
- Percentual de sucesso.

## Estrutura do projeto

```text
sistema_clientes/
├── main.py
├── dados.py
├── validacoes.py
├── processamento.py
├── relatorios.py
└── constantes.py