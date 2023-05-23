# login-Backend-python

## Sobre
É uma API para um futuro projeto front-end que irei desenvolver usando framework Flask

## Porque?
Treinar python no backend e expandir minhas linguagem para poder usar python

## 🚀 Instalação do projeto
<details>
  <summary>Instalação e execução</summary>
  
  #### 1 - Clone o repositório
  - Use o comando ```git clone git@github.com:JoaoVMarques/login-backend.git```
  - Entre na pasta ```cd login-backend```

  #### 2 - Criar o ambiente virtual
  - Inicie o ambiente virtual ```python3 -m venv .venv && source .venv/bin/activate```
  
  #### 3 - Instalar as dependencias
  - Para instalar as dependencias ```python3 -m pip install -r dev-requirements.txt```

  #### 4 - Inicie o banco de dados
  - Para iniciar o banco de dados siga os passos de **Iniciando e configurando o banco de dados**
  
  #### 5 - Iniciar o servidor
  - Para iniciar o servidor ```python3 -m login_backend```

</details>


## 🐋 Banco de dados Docker
<details>
  <summary>Iniciando e configurando o banco de dados</summary>

  ⚠️ O docker precisa estar instalado e  estar na versão 1.29 ou superior ⚠️ [documentação para instalar o docker](https://docs.docker.com/compose/install/)

  para iniciar o banco de dados use o comando ```docker compose up -d```

  - ⚙️ configurações padrões do banco de dados
  ```
  host: localhost
  port: 3306
  user: root
  password: password
  ```

</details>

## 🏆 Objetivos
- [x] Fazer a API funcionar
- [ ] Criar o sistema de logar em uma conta existente
- [ ] Sistema de criar uma conta
- [ ] Bonus: Tentar remover uma conta criada

## Parte Tecnica
<details>
  <summary><strong>🛠️ Ferramentas Utilizadas</strong></summary><br />

  - [Python](https://www.python.org/) Montar o projeto
  - [VsCode](https://code.visualstudio.com/) Editor de codigo fonte
</details>

<details>
  <summary><strong>🧰 Dependencias</strong></summary><br />
  
  - Todas as dependencias estão dentro de ```dev-requirements.txt```
  - [Flask](https://flask.palletsprojects.com/en/2.2.x/) Framework para o servidor 
  - [SQLAlchemy](https://www.sqlalchemy.org/) ORM
  - [pymysql](https://pypi.org/project/pymysql/) conectar o python com mysql
  - [Flake8](https://flake8.pycqa.org/en/latest/) Linter
  - [Pytest](https://docs.pytest.org/en/7.2.x/) Testes
  - [Pytest-cov](https://pytest-cov.readthedocs.io/en/latest/) Porcentagem de testes
  - [flask-expects-json](https://pypi.org/project/flask-expects-json/) Validar schemas do json
  - [mysql-connector-python](https://pypi.org/project/mysql-connector-python/) Conectar com o banco de dados
  
</details>
