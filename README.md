[![Latest Version](https://img.shields.io/github/v/release/alexjosesilva/crm_postogasolinas_Logus_mvc?include_prereleases)](https://github.com/alexjosesilva/crm_postogasolinas_Logus_mvc/releases/tag/1.0)
[![License](https://img.shields.io/github/license/alexjosesilva/logus-microservice-gas-station)]([https://github.com/seu-usuario/seu-repositorio/blob/master/LICENSE](https://github.com/alexjosesilva/logus-microservice-gas-station/blob/master/LICENSE))

# Vertical Logística

## Visão Geral

Este projeto implementa um serviço RESTful para processar arquivos desnormalizados de pedidos, transformando-os em uma estrutura JSON normalizada.

## Instalação

1. Clone o repositório.
2. Navegue até a pasta raiz do projeto:
    ```bash
    cd /caminho/para/vertical-logistica
    ```
3. Crie um ambiente virtual:
    ```bash
    python -m venv venv
    ```
4. Ative o ambiente virtual:
    - No Windows:
      ```bash
      .\venv\Scripts\activate
      ```
    - No MacOS/Linux:
      ```bash
      source venv/bin/activate
      ```
5. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
6. Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:
    ```env
    FLASK_ENV=development
    FLASK_APP=app.py
    SECRET_KEY=supersecretkey
    ```

## Uso

1. Com o ambiente virtual ativado, execute a aplicação:
    ```bash
    python app.py
    ```
2. Envie um arquivo para o endpoint `/upload` via uma requisição POST.

## Estrutura do Projeto

- `app.py`: Ponto de entrada da aplicação.
- `models.py`: Lógica de processamento de dados.
- `utils.py`: Funções auxiliares.
- `requirements.txt`: Dependências do projeto.
- `.env`: Variáveis de ambiente.
- `README.md`: Documentação do projeto.
- `venv/`: Ambiente virtual.

## Exemplo de Requisição

```bash
curl -X POST -F 'file=@caminho/do/arquivo.txt' http://127.0.0.1:5000/upload
