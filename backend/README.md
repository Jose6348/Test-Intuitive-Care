# Teste Intuitive - Análise de Dados da ANS

Este projeto consiste em uma análise completa de dados da Agência Nacional de Saúde Suplementar (ANS), incluindo web scraping, transformação de dados e análise em banco de dados.


## Pré-requisitos

- Python 3.8 ou superior
- PostgreSQL 10.0 ou superior
- pip (gerenciador de pacotes Python)

## Instalação

1. Clone o repositório:
```bash
git clone [URL_DO_REPOSITORIO]
cd [Test-Intuitive-Care]
cd backend
```

2. Instale as dependências Python:
```bash
pip install -r requirements.txt
```

3. Configure o banco de dados PostgreSQL:
```bash
createdb intuitive
```

## Executando o Projeto

### 1. Web Scraping

Este módulo baixa os Anexos I e II do site da ANS e os compacta em um arquivo ZIP.

```bash
python file.py
```

O arquivo `anexos.zip` será gerado no diretório .

### 2. Transformação de Dados

Este módulo extrai dados do PDF do Anexo I e os converte para CSV.

```bash
python dados.py
```

O arquivo `Teste_Jorge.zip` será gerado no diretório .

### 3. Banco de Dados

#### 3.1. Download dos Dados

Execute os seguintes comandos para baixar os dados necessários:

```bash
# Criar diretórios
python testedb.py
```

#### 3.2. Processamento dos Dados

Execute o script Python para processar os arquivos CSV:

```bash
python preprocess_csv.py
```

#### 3.3. Importação para o Banco de Dados

Execute o script SQL para criar as tabelas :

```bash
psql -U [seu_usuario] -d [seu_banco] -f criar_tabelas.sql
```
#### 3.4. Importação para o Banco de Dados

Execute o script SQL para importar as tabelas :

```bash
psql -U [seu_usuario] -d [seu_banco] -f importacao_dados.sql
```

### 4. Análise dos Dados

Para executar as queries analíticas, use o PostgreSQL:

```bash
psql -U [seu_usuario] -d intuitive
```

#### Queries Disponíveis

1. Top 10 operadoras com maiores despesas no último trimestre:
```sql

# Para ver as maiores despesas do último trimestre

```bash
psql -U [seu_usuario] -d [seu_banco] -f consulta_trimestre.sql
```

2. Top 10 operadoras com maiores despesas no ano:
```sql

# Para ver as maiores despesas do ano todo

psql -U [seu_usuario] -d [seu_banco] -f consulta_anual.sql
```

## Estrutura do Banco de Dados

### Tabela: operadoras_ativas
- registro_ans (integer)
- cnpj (varchar(18))
- razao_social (text)
- nome_fantasia (text)
- modalidade (text)
- logradouro (text)
- numero (text)
- complemento (text)
- bairro (text)
- cidade (text)
- uf (char(2))
- cep (varchar(9))
- ddd (char(2))
- telefone (text)
- fax (text)
- endereco_eletronico (text)
- representante (text)
- cargo_representante (text)
- data_registro_ans (date)

### Tabela: demonstracoes_contabeis
- data (date)
- reg_ans (integer)
- cd_conta_contabil (integer)
- descricao (text)
- vl_saldo_inicial (numeric(15,2))
- vl_saldo_final (numeric(15,2))

## Notas

- Os dados são atualizados periodicamente no site da ANS
- O processamento dos dados pode levar alguns minutos, dependendo do tamanho dos arquivos
- Certifique-se de ter espaço suficiente em disco para os arquivos baixados e processados
- O banco de dados PostgreSQL deve estar configurado com encoding UTF-8 