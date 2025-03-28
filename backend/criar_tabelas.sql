CREATE TABLE operadoras_ativas (
    registro_ans        INTEGER,
    cnpj                VARCHAR(18),
    razao_social        TEXT,
    nome_fantasia       TEXT,
    modalidade          TEXT,
    logradouro          TEXT,
    numero              TEXT,
    complemento         TEXT,
    bairro              TEXT,
    cidade              TEXT,
    uf                  CHAR(2),
    cep                 VARCHAR(9),
    ddd                 CHAR(2),
    telefone            TEXT,
    fax                 TEXT,
    endereco_eletronico TEXT,
    representante       TEXT,
    cargo_representante TEXT,
    data_registro_ans   DATE
);

CREATE TABLE demonstracoes_contabeis (
    data                DATE,
    reg_ans             INTEGER,
    cd_conta_contabil   INTEGER,
    descricao           TEXT,
    vl_saldo_inicial    NUMERIC(15,2),
    vl_saldo_final      NUMERIC(15,2)
);
