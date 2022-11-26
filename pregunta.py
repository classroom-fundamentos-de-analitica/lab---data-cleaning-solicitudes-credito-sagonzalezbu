"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")
    #
    # Inserte su código aquí
    #
    df = df.dropna(axis = 0)
    df = df.drop_duplicates()
    df = df.drop(['Unnamed: 0'], axis=1)

    df['sexo'] = df.sexo.str.lower()

    df['tipo_de_emprendimiento'] = df.tipo_de_emprendimiento.str.lower()

    df['idea_negocio'] = df.idea_negocio.str.lower()
    df['idea_negocio'] = df.idea_negocio.str.replace(' ', '_')
    df['idea_negocio'] = df.idea_negocio.str.replace('-', '_')

    df['barrio'] = df.barrio.str.lower()
    df['barrio'] = df.barrio.str.replace(' ', '_')
    df['barrio'] = df.barrio.str.replace('-', '_')
    df['barrio'] = df.barrio.str.replace('.', '', regex=True)

    df.estrato = df.estrato.astype(int)

    df.comuna_ciudadano = df.comuna_ciudadano.astype(int)

    df.fecha_de_beneficio = pd.to_datetime(df.fecha_de_beneficio, infer_datetime_format=True, dayfirst=True, errors='ignore',)
    

    df['monto_del_credito'] = df.monto_del_credito.str.strip('$')
    df['monto_del_credito'] = df.monto_del_credito.str.replace(',', '')
    df['monto_del_credito'] = df.monto_del_credito.str.strip()
    df.monto_del_credito = df.monto_del_credito.astype(float)
    df.monto_del_credito = df.monto_del_credito.astype(int)

    df['línea_credito'] = df.línea_credito.str.replace(' ', '_')
    df['línea_credito'] = df.línea_credito.str.replace('-', '_')
    df['línea_credito'] = df.línea_credito.str.lower()
        
    df = df.drop_duplicates()
    df = df.dropna(axis = 0)
    
    return df