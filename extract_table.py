import pdfplumber
import pandas as pd
 
pdf_file = "G:/My Drive/EdTech/apps/students_list_app/data/ENSEIGNEMENT-PRIVES-RERCONNUS_Post-primaire_2.pdf"
with pdfplumber.open(pdf_file) as pdf:
    lst = [p.extract_table() for p in pdf.pages]

flat_list = [item for sublist in lst for item in sublist]
df = pd.DataFrame(flat_list)
df.columns = df.iloc[0]
df = df[1:]
print(df)
