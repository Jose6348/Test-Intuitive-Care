\x auto
\pset border 2
\pset linestyle unicode
\pset null '[NULL]'

\echo '\n=== DATAS DISPONÍVEIS NA TABELA DEMONSTRAÇÕES CONTÁBEIS ===\n'
SELECT DISTINCT data 
FROM demonstracoes_contabeis 
ORDER BY data DESC 
LIMIT 5;

\echo '\n=== DESCRIÇÕES DE CONTAS CONTÁBEIS RELACIONADAS A SINISTROS ===\n'
SELECT DISTINCT descricao 
FROM demonstracoes_contabeis 
WHERE descricao ILIKE '%SINISTRO%' 
   OR descricao ILIKE '%EVENTO%' 
   OR descricao ILIKE '%ASSISTÊNCIA%'
ORDER BY descricao 
LIMIT 10;

\echo '\n=== AMOSTRA DE DADOS DE 2023 ===\n'
SELECT 
    d.data,
    d.reg_ans,
    d.descricao,
    d.vl_saldo_final
FROM 
    demonstracoes_contabeis d
WHERE 
    d.data >= '2023-01-01'
    AND d.data <= '2023-12-31'
LIMIT 5; 