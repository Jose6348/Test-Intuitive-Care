from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import os
import numpy as np

app = FastAPI()

# Configuração do CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
    expose_headers=["*"]
)

# Variável global para armazenar o DataFrame
df_global = None

# Carregar os dados do CSV
def load_operators():
    global df_global
    
    # Se já estiver carregado, retorna o DataFrame existente
    if df_global is not None:
        return df_global
        
    try:
        print("Tentando carregar o arquivo CSV...")
        current_dir = os.getcwd()
        print(f"Diretório atual: {current_dir}")
        
        # Lista todos os arquivos no diretório atual
        files = os.listdir(current_dir)
        print(f"Arquivos no diretório: {files}")
        
        csv_path = os.path.join(current_dir, 'relatorio_cadop_limpo_processed.csv')
        print(f"Tentando abrir o arquivo: {csv_path}")
        
        if not os.path.exists(csv_path):
            print(f"Arquivo não encontrado em: {csv_path}")
            return None
            
        # Tenta ler o CSV com diferentes encodings se necessário
        try:
            df_global = pd.read_csv(csv_path, sep=';', encoding='latin-1')
        except UnicodeDecodeError:
            print("Tentando com encoding utf-8...")
            df_global = pd.read_csv(csv_path, sep=';', encoding='utf-8')
            
        print(f"CSV carregado com sucesso. Shape: {df_global.shape}")
        print(f"Colunas disponíveis: {df_global.columns.tolist()}")
        print(f"Primeiras linhas do DataFrame:\n{df_global.head()}")
        
        return df_global
    except Exception as e:
        print(f"Erro ao carregar dados: {str(e)}")
        print(f"Tipo do erro: {type(e)}")
        import traceback
        print(f"Traceback completo: {traceback.format_exc()}")
        return None

# Função para limpar valores NaN
def clean_nan(value):
    if pd.isna(value) or value is None:
        return ""
    return str(value)

# Função para calcular relevância
def calculate_relevance(row, query):
    relevance = 0
    query = query.lower()
    
    # Maior peso para correspondências exatas
    if query == str(row['registro_ans']).lower():
        relevance += 100
    if query == str(row['cnpj']).lower():
        relevance += 100
        
    # Peso alto para correspondências no início do texto
    if str(row['nome_fantasia']).lower().startswith(query):
        relevance += 80
    if str(row['razao_social']).lower().startswith(query):
        relevance += 80
        
    # Peso médio para correspondências em qualquer parte
    if query in str(row['nome_fantasia']).lower():
        relevance += 60
    if query in str(row['razao_social']).lower():
        relevance += 60
        
    # Peso menor para correspondências em outros campos
    if query in str(row['modalidade']).lower():
        relevance += 40
    if query in str(row['cidade']).lower():
        relevance += 30
    if query in str(row['uf']).lower():
        relevance += 20
        
    return relevance

# Rota de busca
@app.get("/api/search")
async def search_operators(query: str = None):
    print(f"Recebida requisição de busca para: {query}")
    
    if not query:
        return []
    
    df = load_operators()
    if df is None:
        raise HTTPException(status_code=500, detail="Erro ao carregar dados do CSV")
    
    try:
        # Converte query para minúsculo para busca case-insensitive
        query = query.lower()
        
        # Busca por múltiplos campos
        mask = (
            df['razao_social'].str.lower().str.contains(query, na=False) |
            df['nome_fantasia'].str.lower().str.contains(query, na=False) |
            df['registro_ans'].astype(str).str.lower().str.contains(query, na=False) |
            df['cnpj'].astype(str).str.lower().str.contains(query, na=False) |
            df['modalidade'].str.lower().str.contains(query, na=False) |
            df['cidade'].str.lower().str.contains(query, na=False) |
            df['uf'].str.lower().str.contains(query, na=False)
        )
        
        # Filtrar resultados e calcular relevância
        results = df[mask].copy()
        print(f"Número de resultados encontrados: {len(results)}")
        
        if len(results) > 0:
            results['relevance'] = results.apply(lambda row: calculate_relevance(row, query), axis=1)
            results = results.sort_values('relevance', ascending=False).head(10)
            results = results.to_dict('records')
            print(f"Top 10 resultados mais relevantes selecionados")
        else:
            results = []
            print("Nenhum resultado encontrado")
            
        # Formatar os resultados
        formatted_results = []
        for result in results:
            formatted_results.append({
                'id': clean_nan(result['registro_ans']),
                'nome': clean_nan(result['nome_fantasia']) or clean_nan(result['razao_social']),
                'razao_social': clean_nan(result['razao_social']),
                'cnpj': clean_nan(result['cnpj']),
                'modalidade': clean_nan(result['modalidade']),
                'porte': clean_nan(result.get('porte', '')),
                'uf': clean_nan(result['uf']),
                'municipio': clean_nan(result['cidade'])
            })
        
        return formatted_results
    except Exception as e:
        print(f"Erro ao processar busca: {str(e)}")
        print(f"Tipo do erro: {type(e)}")
        import traceback
        print(f"Traceback completo: {traceback.format_exc()}")
        raise HTTPException(status_code=500, detail=f"Erro ao processar busca: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001) 