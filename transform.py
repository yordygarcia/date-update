import pandas as pd

import warnings
warnings.filterwarnings('ignore')

def update_date(df, column):
  df[column] = df[column].astype(str).str.slice(0,10)

  #df con fechas correctas
  df_1 = df[~ ( df[column].str.contains('/') )]

  #por corregir
  fechas = df[df[column].str.contains('/')][column].str.strip()

  dia = fechas.str.extract(r'(\d+)')[0].str.zfill(2)
  mes = fechas.str.extract(r'(/.*/)')[0].astype(str).str.replace('/','').str.zfill(2)
  anio = fechas.str.extract(r'(\d+\Z)')[0]

  fechas_corregidas = anio + '-' + mes + '-' + dia

  #df con fechas incorrectas
  df_2 = df[ df[column].str.contains('/') ]
  df_2[column] = fechas_corregidas

  #concatena dfs
  df_final = pd.DataFrame()
  df_final = df_final.append([df_1, df_2] , ignore_index=True)

  return df_final



















    




