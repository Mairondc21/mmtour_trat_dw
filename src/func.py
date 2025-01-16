import pandas as pd

def juntar_planilhas(excel_file: pd.ExcelFile) -> pd.ExcelFile:
    xls = pd.ExcelFile(excel_file)
    df_list = []
    column_name = ["Hora","Passageiro","Origem","Destino","Empresa","Motorista","Valor","Obs"]
    
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name=sheet_name, header=1, usecols="B:I", names=column_name)
        df["Data"] = sheet_name  # Adicionar o nome da planilha em uma nova coluna
        df["Data"] = df["Data"].astype(str) + "/1"
        df = df.dropna(subset=["Passageiro"])

        mover_data = df.pop("Data")
        df.insert(0, "Data", mover_data)
        df["Empresa"] = df["Empresa"].fillna("nao informado")
        df["Motorista"] = df["Motorista"].fillna("nao informado")

        df_list.append(df)
    df_concatenado = pd.concat(df_list, ignore_index=True)
    df_geral = df_concatenado.to_excel("dados/01/janeiro_teste.xlsx")

    return df_geral

def tratamentos_dl(excel_tratado: pd.ExcelFile):
    df = pd.read_excel(excel_tratado)

    #codificando a coluna passageiros
    tb_passageiros = df[["Passageiro","Origem","Destino"]]
    tb_passageiros['cod_passageiro'] = tb_passageiros["Passageiro"].rank(method='dense').astype(int)
    tb_passageiros['cod_origem'] = tb_passageiros["Origem"].rank(method='dense').astype(int)
    tb_passageiros['cod_destino'] = tb_passageiros["Destino"].rank(method='dense').astype(int)
    print(tb_passageiros.head())
    




"""
    De mes a mes farei uma nova codificacao, e depois de codificar os
    dados e fazer as tabelas no python vou pegar um arquivo de historicos,
    esse arquivo de historicos fara uma comparacao com os dados novos e os 
    ja processados, para que nao aconteca de um cod 2 que ja esta setado na 
    minha tabela tratada der conflito com o mesmo dado vindo com um outro codigo
"""

excel_01_antes_da_juncao = "./dados/teste/01_JANEIRO.xlsx"
excel_tratado_01 = "./dados/01/janeiro.xlsx"

#juntar_planilhas(excel_01_antes_da_juncao)

tratamentos_dl(excel_tratado_01)