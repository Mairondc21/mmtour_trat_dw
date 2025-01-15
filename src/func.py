import pandas as pd

def juntar_planilhas(excel_file):
    xls = pd.ExcelFile(excel_file)
    df_list = []
    
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name=sheet_name, header=1, usecols="B:I")
        df["Data"] = sheet_name  # Adicionar o nome da planilha em uma nova coluna
        df["Data"] = df["Data"].astype(str) + "/1"
        df = df.dropna(subset=["Passageiro"])

        mover_data = df.pop("Data")
        df.insert(0, "Data", mover_data)
        df["Empresa"] = df["Empresa"].fillna("nao informado")
        df["Motorista"] = df["Motorista"].fillna("nao informado")

        df_list.append(df)
    df_concatenado = pd.concat(df_list, ignore_index=True)
    df_geral = df_concatenado.to_excel("dados/01/janeiro.xlsx")

    return df_geral
    







excel_01 = r'E:/MMTurismo/AGENDAMENTOS E CADASTRO/AGENDA/01 - JANEIRO  -  AGENDAMENTOS .xls'

juntar_planilhas(excel_01)