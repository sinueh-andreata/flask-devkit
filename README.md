
## FLASK DEVKIT

O flask devkit é um boilerplate de código python utilizando o framework "Flask", o boilerplate é estruturado em arquitetura em camadas, pré configurações do framework e de containers docker.

## Requisitos

- Python instalado
- Docker instalado

## Instalação

- Baixe o zip e descompacte
- Abra o diretório do boilerplate

Siga as instruções do arquivo ".evn.dev.example"

```bash
# Arquivo .env para desenvolvimento
# COPIE ESTE ARQUIVO PARA .env.dev E CONFIGURE COM SEUS VALORES REAIS

# Configurações de segurança
SECRET_KEY=sua_chave_secreta_muito_forte_aqui_min_32_caracteres
SECURITY_PASSWORD_SALT=seu_salt_de_senha_aqui_min_32_caracteres

# Config do banco de dados
DB_HOST=host.docker.internal
DB_NAME=nome_do_seu_db
DB_USER=nome_do_seu_usuario
DB_PASSWORD=senha_forte_do_usuario_mysql

# import secrets
# print(secrets.token_hex())
```


## Rodando localmente

Rode no terminal

```bash
  docker-compose -f docker-compose.dev.yml build
```

Depois que terminar a build Rode

```bash
  docker-compose -f docker-compose.dev.yml up
```

Agora é só codar
## Stack utilizada

**Front-end:** HTML, TailwindCSS e JavaScript

**Back-end:** Python, Flask, Docker, Docker compose

**Banco de Dados:** MySQL
