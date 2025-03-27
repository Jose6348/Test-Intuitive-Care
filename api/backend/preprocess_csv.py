import pandas as pd
import os
import numpy as np

def preprocess_csv(input_file, output_file):
    df = pd.read_csv(input_file, sep=';', decimal=',')
    
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    
    if 'regiao_de_comercializacao' in df.columns:
        df = df.drop('regiao_de_comercializacao', axis=1)
    
   
    if 'ddd' in df.columns:
        df['ddd'] = df['ddd'].astype(str).str.replace('.0', '').str.strip()
        # Substitui 'nan' por string vazia
        df['ddd'] = df['ddd'].replace('nan', '')
    
    if 'data' in df.columns:
        try:
            df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y')
        except:
            try:
                df['data'] = pd.to_datetime(df['data'])
            except:
                pass
        df['data'] = df['data'].dt.strftime('%Y-%m-%d')
    
    colunas_numericas = ['vl_saldo_inicial', 'vl_saldo_final']
    
    for col in df.columns:
        if col in colunas_numericas:
            df[col] = df[col].astype(str).str.strip()
            df[col] = df[col].str.replace('R$', '').str.replace(' ', '')
            df[col] = df[col].str.replace(',', '.')
            df[col] = pd.to_numeric(df[col], errors='coerce')
    
    df.to_csv(output_file, sep=';', decimal='.', index=False, na_rep='')

base_dir = '/Users/gransysdesenvolvimento/Documents/teste/Teste_Intuitive'

input_file = os.path.join(base_dir, 'relatorio_cadop_limpo.csv')
output_file = os.path.join(base_dir, 'relatorio_cadop_limpo_processed.csv')
if os.path.exists(input_file):
    preprocess_csv(input_file, output_file)

years = ['2023']  
quarters = ['1T', '2T', '3T', '4T']

for year in years:
    for quarter in quarters:
        input_file = os.path.join(base_dir, 'demonstracoes', year, f'{quarter}{year}_limpo.csv')
        output_file = os.path.join(base_dir, 'demonstracoes', year, f'{quarter}{year}_limpo_processed.csv')
        if os.path.exists(input_file):
            preprocess_csv(input_file, output_file) 