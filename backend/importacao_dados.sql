-- Importar operadoras ativas (arquivo limpo)
\copy operadoras_ativas (registro_ans, cnpj, razao_social, nome_fantasia, modalidade, logradouro, numero, complemento, bairro, cidade, uf, cep, ddd, telefone, fax, endereco_eletronico, representante, cargo_representante, data_registro_ans) FROM PROGRAM 'cut -d";" -f1-18,20 relatorio_cadop.csv | sed "s/\"//g"' WITH (FORMAT csv, HEADER true, ENCODING 'UTF8', DELIMITER ';', NULL '', QUOTE '"');

-- Demonstrativos Contábeis 2023
\copy demonstracoes_contabeis FROM PROGRAM 'sed -e "s/,/./g" -e "s/\"//g" demonstracoes/2023/1T2023.csv' WITH (FORMAT csv, HEADER true, ENCODING 'UTF8', DELIMITER ';', NULL '', QUOTE '"', FORCE_NULL (data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final));

\copy demonstracoes_contabeis FROM PROGRAM 'sed -e "s/,/./g" -e "s/\"//g" demonstracoes/2023/2T2023.csv' WITH (FORMAT csv, HEADER true, ENCODING 'UTF8', DELIMITER ';', NULL '', QUOTE '"', FORCE_NULL (data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final));

\copy demonstracoes_contabeis FROM PROGRAM 'sed -e "s/,/./g" -e "s/\"//g" demonstracoes/2023/3T2023.csv' WITH (FORMAT csv, HEADER true, ENCODING 'UTF8', DELIMITER ';', NULL '', QUOTE '"', FORCE_NULL (data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final));

\copy demonstracoes_contabeis FROM PROGRAM 'sed -e "s/,/./g" -e "s/\"//g" demonstracoes/2023/4T2023.csv' WITH (FORMAT csv, HEADER true, ENCODING 'UTF8', DELIMITER ';', NULL '', QUOTE '"', FORCE_NULL (data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final));
