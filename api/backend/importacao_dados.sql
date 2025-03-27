-- Importar operadoras ativas (arquivo limpo)
COPY operadoras_ativas (registro_ans, cnpj, razao_social, nome_fantasia, modalidade, logradouro, numero, complemento, bairro, cidade, uf, cep, ddd, telefone, fax, endereco_eletronico, representante, cargo_representante, data_registro_ans)
FROM '/Users/gransysdesenvolvimento/Documents/teste/Teste_Intuitive/relatorio_cadop_limpo_processed.csv'
WITH (
    FORMAT csv,
    HEADER true,
    ENCODING 'UTF8',
    DELIMITER ';',
    NULL '',
    QUOTE '"'
);

-- Demonstrativos Contábeis 2023
COPY demonstracoes_contabeis
FROM '/Users/gransysdesenvolvimento/Documents/teste/Teste_Intuitive/demonstracoes/2023/1T2023_limpo_processed.csv'
WITH (
    FORMAT csv,
    HEADER true,
    ENCODING 'UTF8',
    DELIMITER ';',
    NULL '',
    QUOTE '"',
    FORCE_NULL (data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
);

COPY demonstracoes_contabeis
FROM '/Users/gransysdesenvolvimento/Documents/teste/Teste_Intuitive/demonstracoes/2023/2T2023_limpo_processed.csv'
WITH (
    FORMAT csv,
    HEADER true,
    ENCODING 'UTF8',
    DELIMITER ';',
    NULL '',
    QUOTE '"',
    FORCE_NULL (data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
);

COPY demonstracoes_contabeis
FROM '/Users/gransysdesenvolvimento/Documents/teste/Teste_Intuitive/demonstracoes/2023/3T2023_limpo_processed.csv'
WITH (
    FORMAT csv,
    HEADER true,
    ENCODING 'UTF8',
    DELIMITER ';',
    NULL '',
    QUOTE '"',
    FORCE_NULL (data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
);

COPY demonstracoes_contabeis
FROM '/Users/gransysdesenvolvimento/Documents/teste/Teste_Intuitive/demonstracoes/2023/4T2023_limpo_processed.csv'
WITH (
    FORMAT csv,
    HEADER true,
    ENCODING 'UTF8',
    DELIMITER ';',
    NULL '',
    QUOTE '"',
    FORCE_NULL (data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
);
