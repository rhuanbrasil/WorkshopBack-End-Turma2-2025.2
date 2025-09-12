# Workshop 2025.2: Do Básico ao Django com APIs

Bem-vindo ao meu repositório de projetos do workshop de Python! Este espaço documenta minha jornada de aprendizado ao longo de 6 dias intensivos, cobrindo desde os fundamentos da linguagem até a criação de aplicações web com Django e a integração com APIs externas.

Cada pasta numerada corresponde a um dia do workshop e contém o código e os desafios desenvolvidos.

## Estrutura do Repositório

O workshop foi dividido nos seguintes tópicos diários:

### 📂 `dia-01/` - Comandos Básicos de Python
Neste primeiro dia, o foco foi a introdução à sintaxe fundamental do Python. Os scripts abordam:
- Variáveis e tipos de dados (strings, inteiros, floats, booleanos).
- Operadores aritméticos e lógicos.
- Estruturas de controle de fluxo (if, elif, else).
- Laços de repetição (for, while).

### 📂 `dia-02/` - POO e Métodos em Python
O segundo dia foi dedicado à Programação Orientada a Objetos (POO), um pilar do desenvolvimento de software moderno. Os projetos demonstram:
- Criação de classes e objetos.
- Definição de atributos e métodos.
- Conceitos de encapsulamento, herança e polimorfismo.

### 📂 `dia-03/` - Django MVT e Tratamento de Erros
Neste dia, iniciamos o desenvolvimento web com o framework Django. O projeto aborda:
- A arquitetura Model-View-Template (MVT).
- Configuração de um projeto Django, rotas (URLs), views e templates.
- Implementação de boas práticas para tratamento de exceções e erros (`try...except`).

### 📂 `dia-04/` - Consumir API de CEP
O foco foi a integração com serviços externos. O projeto consiste em:
- Fazer requisições HTTP para uma API pública de consulta de CEP (ViaCEP).
- Tratar a resposta JSON e exibir os dados de endereço de forma amigável no template.

### 📂 `dia-04/(apenas alterado dia 5)` - Consumir API de CEP com Funções CRUD
Evoluindo o projeto anterior, adicionamos persistência de dados. A aplicação agora permite:
- **C**reate (Criar): Salvar um novo endereço consultado no banco de dados.
- **R**ead (Ler): Listar todos os endereços salvos.
- **U**pdate (Atualizar): Modificar as informações de um endereço existente.
- **D**elete (Deletar): Remover um endereço do banco de dados.

### 📂 `dia-06/` - CRUD com APIRest à Escolha
 apliquei todos os conceitos aprendidos para construir uma aplicação completa que consome uma API de minha escolha (**[The Star Wars API - SWAPI]**). A aplicação implementa um CRUD completo para gerenciar os dados obtidos da API.

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** Python 3
- **Framework Web:** Django e DjangoRest_framework
- **Banco de Dados:** SQLite 3
- **Bibliotecas:** `requests` (para requisições HTTP)

---

## 🚀 Como Rodar os Projetos

Siga as instruções abaixo para configurar e executar os projetos em sua máquina local.

### Pré-requisitos
- [Python 3.8+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)

### 1. Clone o Repositório
```bash
git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
cd seu-repositorio
```

Os projetos dos primeiros dias são scripts simples em Python.

```bash
# Navegue até a pasta do dia desejado
cd dia-01/

# Execute o script Python
python nome_do_arquivo.py
```

Os projetos a partir do terceiro dia são aplicações Django e exigem um ambiente virtual e a instalação de dependências.

```bash

# 1. Navegue até a pasta de um dos projetos Django
# Exemplo para o projeto do dia 5:
cd dia-05/

# 2. Crie e ative um ambiente virtual
# No Windows
python -m venv venv
venv\Scripts\activate

# No macOS/Linux
python3 -m venv venv
source venv/bin/activate

# 3. Instale as dependências do projeto
pip install -r requirements.txt

# 4. Aplique as migrações do banco de dados
python manage.py migrate

# 5. Inicie o servidor de desenvolvimento
python manage.py runserver
Após executar o último comando, a aplicação estará disponível em seu navegador no endereço https://www.google.com/search?q=http://127.0.0.1:8000/
