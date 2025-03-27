import pdfplumber
import pandas as pd
import zipfile

pdf = pdfplumber.open("anexo_I.pdf")

all_rows = []  
header = None  

for page in pdf.pages[2:]:
    tables = page.extract_tables()
    if not tables:
        continue  

    for table in tables:
        if header is None:
            header = [ (cell.strip() if cell else "") for cell in table[0] ]  
            for row in table[1:]:
                clean_row = [ (cell.strip() if cell else "") for cell in row ]
                all_rows.append(clean_row)
        else:
            start_index = 0
            first_row = [ (cell.strip() if cell else "") for cell in table[0] ]
            if first_row == header:
                start_index = 1
            for row in table[start_index:]:
                clean_row = [ (cell.strip() if cell else "") for cell in row ]
                all_rows.append(clean_row)

pdf.close()

df = pd.DataFrame(all_rows, columns=header)

df.dropna(how="all", inplace=True)

df.drop_duplicates(inplace=True)

df.columns = [col.strip() for col in df.columns]

col_rename_map = {
    "OD": "Seg. Odontológica",
    "AMB": "Seg. Ambulatorial",
    "HCO": "Seg. Hospitalar Com Obstetrícia",
    "HSO": "Seg. Hospitalar Sem Obstetrícia",
    "REF": "Plano Referência",
    "PAC": "Procedimento de Alta Complexidade",
    "DUT": "Diretriz de Utilização"
}
new_columns = []
for col in df.columns:
    if col in col_rename_map:
        new_columns.append(col_rename_map[col])
    elif col.split(" ")[0] in col_rename_map:  
        base = col.split(" ")[0]
        new_name = col_rename_map.get(base, base)
        suffix = col[len(base):]
        new_columns.append(new_name + suffix)
    else:
        new_columns.append(col)
df.columns = new_columns

csv_filename = "rol_procedimentos.csv"
df.to_csv(csv_filename, index=False)

zip_filename = "Teste_Jorge.zip"
with zipfile.ZipFile(zip_filename, mode="w", compression=zipfile.ZIP_DEFLATED) as zipf:
    zipf.write(csv_filename, arcname=csv_filename)
