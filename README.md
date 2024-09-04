# Comparador de Colunas de Planilhas com Streamlit e Docker

Esta aplicação permite comparar colunas de duas planilhas carregadas pelo usuário. Ela mostra um preview das tabelas enviadas e identifica as linhas onde os valores das colunas selecionadas são inconsistentes.

## Funcionalidades

- Carregamento de duas planilhas (`.csv` ou `.xlsx`).
- Visualização prévia das tabelas carregadas.
- Seleção de colunas de cada planilha para comparação.
- Notificação sobre a consistência ou inconsistência dos valores.
- Exibição das linhas com inconsistências para fácil identificação.

## Tecnologias Utilizadas

- [Python](https://www.python.org/) 3.9
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Docker](https://www.docker.com/)

## Pré-requisitos

- Docker e Docker Compose instalados na sua máquina.
- Planilhas `.csv` ou `.xlsx` para realizar os testes.

## Como Executar a Aplicação

### Passo 1: Clone o Repositório

```bash
git clone https://github.com/seuusuario/nome-do-repositorio.git
cd nome-do-repositorio
```

### Passo 2: Build da Imagem com Docker

Execute o comando para construir a imagem da aplicação:

```bash
docker-compose up --build
```

### Passo 3: Acesse a Aplicação

Após a construção e inicialização, acesse a aplicação no navegador através do link:

```
http://localhost:8501
```

## Estrutura do Projeto

- `app.py`: Código principal da aplicação Streamlit.
- `Dockerfile`: Configuração da imagem Docker.
- `docker-compose.yml`: Orquestração da aplicação com Docker Compose.
- `requirements.txt`: Lista de dependências Python.

## Utilização da Aplicação

1. **Upload de Planilhas**: Faça o upload das duas planilhas que deseja comparar.
2. **Visualização**: Veja uma prévia das tabelas carregadas para confirmar se os dados foram importados corretamente.
3. **Seleção de Colunas**: Escolha as colunas que deseja comparar de cada planilha.
4. **Comparação**: Clique em "Comparar Colunas" para verificar se os valores coincidem ou identificar as linhas inconsistentes.

## Exemplo de Uso

1. Faça o upload de duas planilhas contendo dados semelhantes.
2. Visualize as primeiras linhas das planilhas.
3. Selecione a coluna "Instalação" em ambas as planilhas.
4. Clique no botão "Comparar Colunas" para verificar as inconsistências.

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença

Este projeto está licenciado sob a Licença MIT 
