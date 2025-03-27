# Teste Intuitive - Análise de Dados da ANS

Este projeto consiste em uma análise completa de dados da Agência Nacional de Saúde Suplementar (ANS), incluindo web scraping, transformação de dados e análise em banco de dados.

## Estrutura do Projeto

```
.
├── README.md
├── requirements.txt
├── web_scraping/
│   ├── download_anexos.py
│   └── anexos.zip
├── transformacao/
│   ├── extract_pdf.py
│   └── Teste_[nome].zip
└── banco_dados/
    ├── importacao_dados.sql
    ├── preprocess_csv.py
    ├── relatorio_cadop_limpo.csv
    └── demonstracoes/
        └── 2023/
            ├── 1T2023_limpo.csv
            ├── 2T2023_limpo.csv
            ├── 3T2023_limpo.csv
            └── 4T2023_limpo.csv
```

## Pré-requisitos

- Python 3.8 ou superior
- PostgreSQL 10.0 ou superior
- pip (gerenciador de pacotes Python)

## Instalação

1. Clone o repositório:
```bash
git clone [URL_DO_REPOSITORIO]
cd [NOME_DO_DIRETORIO]
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
mkdir -p demonstracoes/2023

# Download dos dados cadastrais das operadoras ativas
curl -o relatorio_cadop_limpo.csv https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/relatorio_cadop_limpo.csv

# Download das demonstrações contábeis de 2023
for trimestre in 1T 2T 3T 4T; do
    curl -o "demonstracoes/2023/${trimestre}2023_limpo.csv" "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/${trimestre}2023_limpo.csv"
done
```

#### 3.2. Processamento dos Dados

Execute o script Python para processar os arquivos CSV:

```bash
python preprocess_csv.py
```

#### 3.3. Importação para o Banco de Dados

Execute o script SQL para criar as tabelas e importar os dados:

```bash
psql -U [seu_usuario] -d intuitive -f importacao_dados.sql
```

### 4. Análise dos Dados

Para executar as queries analíticas, use o PostgreSQL:

```bash
psql -U [seu_usuario] -d intuitive
```

#### Queries Disponíveis

1. Top 10 operadoras com maiores despesas no último trimestre:
```sql
WITH UltimoTrimestre AS (
    SELECT 
        dc.reg_ans,
        oa.razao_social,
        ABS(dc.vl_saldo_final) as despesa
    FROM demonstracoes_contabeis dc
    JOIN operadoras_ativas oa ON dc.reg_ans = oa.registro_ans::integer
    WHERE dc.data >= '2023-10-01' 
    AND dc.data <= '2023-12-31'
    AND UPPER(dc.descricao) LIKE UPPER('%EVENTOS%SINISTROS%MEDICO HOSPITALAR%')
)
SELECT 
    razao_social as "Operadora",
    TO_CHAR(despesa, 'FM999,999,999,999.00') as "Despesa (R$)"
FROM UltimoTrimestre
ORDER BY despesa DESC
LIMIT 10;
```

2. Top 10 operadoras com maiores despesas no ano:
```sql
WITH DespesasAnuais AS (
    SELECT 
        dc.reg_ans,
        oa.razao_social,
        ABS(SUM(dc.vl_saldo_final)) as despesa_total
    FROM demonstracoes_contabeis dc
    JOIN operadoras_ativas oa ON dc.reg_ans = oa.registro_ans::integer
    WHERE EXTRACT(YEAR FROM dc.data) = 2023
    AND UPPER(dc.descricao) LIKE UPPER('%EVENTOS%SINISTROS%MEDICO HOSPITALAR%')
    GROUP BY dc.reg_ans, oa.razao_social
)
SELECT 
    razao_social as "Operadora",
    TO_CHAR(despesa_total, 'FM999,999,999,999.00') as "Despesa Total 2023 (R$)"
FROM DespesasAnuais
ORDER BY despesa_total DESC
LIMIT 10;
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