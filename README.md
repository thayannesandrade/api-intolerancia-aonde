
# API de Intolerância Religiosa

## Descrição

Esta é uma API desenvolvida com Flask para registrar e consultar casos de intolerância religiosa. A API permite cadastrar novos casos e listar os casos já registrados, oferecendo uma interface simples para manipulação de dados.

## Tecnologias Usadas

- Python
- Flask
- Flask-RESTx
- Flask-SQLAlchemy
- SQLite

## Requisitos

Antes de começar, certifique-se de que você tem o Python 3.x instalado em sua máquina. Além disso, você precisará das seguintes bibliotecas:

- Flask
- Flask-RESTx
- Flask-SQLAlchemy

## Instalação

1. **Clone o repositório**:

   ```bash
   git clone <https://github.com/thayannesandrade/api-intolerancia-aonde>
   cd <api-intolerancia-aonde>
   ```

2. **Crie um ambiente virtual** (opcional, mas recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows use: venv\Scripts\activate
   ```

3. **Instale as dependências**:

   ```bash
   pip install Flask Flask-RESTx Flask-SQLAlchemy
   ```

## Configuração do Banco de Dados

O banco de dados SQLite será criado automaticamente quando a aplicação for iniciada pela primeira vez. Não é necessário configurar manualmente.

## Execução do Projeto

1. **Execute a aplicação**:

   ```bash
   python app.py
   ```

2. **Acesse a API**:

   Abra seu navegador ou uma ferramenta como Postman e acesse:

   ```
   http://127.0.0.1:5000/
   ```

   Você deverá ver uma mensagem de boas-vindas.

## Endpoints Disponíveis

### 1. Rota Raiz

- **GET** `/`

  Resposta:

  ```json
  {
      "message": "Bem-vindo à API de Intolerância Aonde!"
  }
  ```

### 2. Listar Casos

- **GET** `/casos`

  Retorna uma lista de todos os casos cadastrados.

### 3. Cadastrar Novo Caso

- **POST** `/casos`

  **Corpo da Requisição** (JSON):

  ```json
  {
      "bairro": "Centro",
      "estado": "SP",
      "descricao": "Caso de intolerância religiosa ocorrido durante um evento.",
      "tipo_crime": "Intolerância religiosa",
      "data_ocorrencia": "2024-09-23"
  }
  ```

  Resposta (201 Created):

  ```json
  {
      "id": 1,
      "bairro": "Centro",
      "estado": "SP",
      "descricao": "Caso de intolerância religiosa ocorrido durante um evento.",
      "tipo_crime": "Intolerância religiosa",
      "data_ocorrencia": "2024-09-23"
  }
  ```

### 4. Obter Caso por ID

- **GET** `/casos/<id>`

  Substitua `<id>` pelo ID do caso que você deseja consultar.

  Resposta (200 OK):

  ```json
  {
      "id": 1,
      "bairro": "Centro",
      "estado": "SP",
      "descricao": "Caso de intolerância religiosa ocorrido durante um evento.",
      "tipo_crime": "Intolerância religiosa",
      "data_ocorrencia": "2024-09-23"
  }
  ```

## Testando a API

### Usando Postman

1. **Criando uma Nova Requisição**:
   - Selecione o método **POST** e insira a URL `http://127.0.0.1:5000/casos`.
   - Vá para a aba **Body**, selecione **raw** e escolha **JSON** no menu suspenso.
   - Insira o JSON desejado e clique em **Send**.

### Usando curl

Para cadastrar um novo caso pelo terminal, execute:

```bash
curl -X POST http://127.0.0.1:5000/casos \
-H "Content-Type: application/json" \
-d '{
    "bairro": "Centro",
    "estado": "SP",
    "descricao": "Caso de intolerância religiosa ocorrido durante um evento.",
    "tipo_crime": "Intolerância religiosa",
    "data_ocorrencia": "2024-09-23"
}'
```

## Contribuição

Se você deseja contribuir com este projeto, fique à vontade para enviar um Pull Request. Qualquer feedback ou sugestão é bem-vindo!

## Licença

Este projeto é licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para detalhes.
