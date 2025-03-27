-- Configuração para melhor visualização no terminal
\x auto
\pset border 2
\pset linestyle unicode
\pset null '[NULL]'

-- Verificar datas disponíveis
\echo '\n=== DATAS DISPONÍVEIS NA TABELA DEMONSTRAÇÕES CONTÁBEIS ===\n'
SELECT DISTINCT data 
FROM demonstracoes_contabeis 
ORDER BY data DESC 
LIMIT 5;

-- Verificar descrições de contas contábeis
\echo '\n=== DESCRIÇÕES DE CONTAS CONTÁBEIS RELACIONADAS A SINISTROS ===\n'
SELECT DISTINCT descricao 
FROM demonstracoes_contabeis 
WHERE descricao ILIKE '%SINISTRO%' 
   OR descricao ILIKE '%EVENTO%' 
   OR descricao ILIKE '%ASSISTÊNCIA%'
ORDER BY descricao 
LIMIT 10;

-- Verificar se há dados para 2023
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