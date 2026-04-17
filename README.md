# 🌦️ Pipeline ETL Weather: OpenWeatherMap & Apache Airflow
Este projeto consiste em um pipeline de dados ponta a ponta (ETL) que extrai informações meteorológicas em tempo real da API OpenWeatherMap, realiza transformações de limpeza e normalização, e carrega os dados em um data warehouse PostgreSQL orquestrado pelo Apache Airflow em ambiente conteinerizado.

## 🏗️ Arquitetura do Projeto
O pipeline segue a estrutura clássica de Engenharia de Dados:

* **Extract:** Consumo da API REST OpenWeatherMap (JSON).
* **Transform:** Processamento com Python/Pandas (Limpeza, conversão de tipos e fuso horário).
* **Load:** Persistência em Banco de Dados Relacional (PostgreSQL).
* **Orchestration:** Gerenciamento de fluxo e retentativas via Apache Airflow (DAGs).
* **Infrastructure:** Ambiente isolado via Docker Compose e otimizado via WSL2.

## 🛠️ Tecnologias Utilizadas
* Linguagem: Python 3.10+
* Orquestração: Apache Airflow
* Processamento de Dados: Pandas
* Banco de Dados: PostgreSQL 16
* Infraestrutura: Docker & Docker Compose
* Gerenciador de Pacotes: uv (Astral)
* Ambiente de Desenvolvimento: WSL2 (Ubuntu 22.04)

## 📁 Estrutura de Pastas
```bash
pipeline-weather/
├── config/             # Configurações e Variáveis de Ambiente (.env)
├── dags/               # Definições das DAGs do Airflow
├── data/               # Camada de armazenamento local (JSON/Parquet)
├── logs/               # Logs de execução do Airflow
├── src/                # Scripts Python do Pipeline (Extract, Transform, Load)
├── docker-compose.yml  # Configuração dos containers (Postgres/Airflow)
├── main.py             # Script de execução manual/teste
└── pyproject.toml      # Gerenciamento de dependências (uv)
```

## 🚀 Como Executar o Projeto

1. **Pré-requisitos**
    * Docker Desktop instalado e integrado ao WSL2.
    * Chave de API do OpenWeatherMap.

2. **Configuração do Ambiente**\
Crie um arquivo .env na pasta raiz (ou config/) seguindo o modelo:
```bash
api_key=SUA_CHAVE_AQUI
database=weather_data
user=tualatim
password=281256
host=localhost
AIRFLOW_UID=1000
```

3. **Otimização de Recursos (WSL2)**\
Para evitar travamentos de memória (Vmmem), este projeto utiliza uma configuração otimizada no .wslconfig:
```bash
[wsl2]
memory=4GB
processors=4
swap=4GB

[experimental]
autoMemoryReclaim=dropcache
sparseVhd=true
```

4. **Inicialização**\
No terminal do WSL2, execute:
```bash
# Subir infraestrutura
docker compose up -d

# Instalar dependências locais (opcional para dev)
uv sync
```
Acesse a interface do Airflow em: localhost:8080 (usuário/senha padrão: airflow).

## 📊 Detalhes Técnicos
**Transformação de Dados**\
* **Normalização:** Conversão de estruturas aninhadas de JSON para colunas flat.
* **Data/Hora:** Tratamento de timestamps UNIX para datetime no fuso horário America/Sao_Paulo.
* **Persistência:** Uso de SQLAlchemy para integração robusta entre Python e Postgres.

## Autor

**Vinícius Gomes Marques**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/vinicius-gomes-marques)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/vini-gm)

## 📜 Licença
Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.