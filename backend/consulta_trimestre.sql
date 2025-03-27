-- Configuração para melhor visualização no terminal
\x auto
\pset border 2
\pset linestyle unicode
\pset null '[NULL]'

-- Título da consulta
\echo '\n=== TOP 10 OPERADORAS COM MAIORES DESPESAS EM SINISTROS (3º TRIMESTRE 2023) ===\n'

-- Consulta para encontrar as 10 operadoras com maiores despesas em sinistros no último trimestre disponível
SELECT 
    o.registro_ans as "Registro ANS",
    o.razao_social as "Razão Social",
    TO_CHAR(ABS(SUM(d.vl_saldo_final)), 'L999G999G999G999G999D99') as "Despesa Total (R$)"
FROM 
    operadoras_ativas o
    INNER JOIN demonstracoes_contabeis d ON o.registro_ans = d.reg_ans
WHERE 
    d.data = '2023-07-01' -- data do 3º trimestre de 2023
    AND (
        d.descricao LIKE '%CONTRAPRESTAÇÕES DE CORRESPONSABILIDADE CEDIDA DE ASSISTÊNCIA A SAÚDE%'
        OR d.descricao LIKE '%CONTRAPRESTAÇÕES DE CORRESPONSABILIDADE CEDIDA DE ASSISTÊNCIA MÉDICO-HOSPITALAR%'
        OR d.descricao LIKE '%RECUPERAÇÃO DE OUTRAS DESPESAS OPERACIONAIS DE ASSISTÊNCIA A SAÚDE%'
        OR d.descricao LIKE '%RECUPERAÇÃO DE OUTRAS DESPESAS OPERACIONAIS DE ASSISTÊNCIA MÉDICO-HOSPITALAR%'
    )
GROUP BY 
    o.registro_ans,
    o.razao_social
ORDER BY 
    ABS(SUM(d.vl_saldo_final)) DESC
LIMIT 10; 