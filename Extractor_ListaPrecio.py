import pandas as pd
import sys
import os
import cx_Oracle
from decouple import config


dir_Oracle= config('ORACLE_HOST')
puerto_Oracle= config('ORACLE_PORT')
serv_name_Oracle= config('ORACLE_DATABASE')
usu_Oracle = config('ORACLE_USER')
pwd_Oracle =  config('ORACLE_PASSWORD')

dsn = cx_Oracle.makedsn(dir_Oracle,puerto_Oracle,service_name=serv_name_Oracle)
conexionOra = cx_Oracle.connect(user=usu_Oracle, password=pwd_Oracle,  dsn=dsn)



def Obtener_Reporte(Lista_Precio,Sucursal):
    if Sucursal == "":
        Sucursal = "250"
    

    if Lista_Precio == "257":
        SQL = open("E:/Desarrollo/Art_Lista_Precios-/SQL/Query_Lista_Precio_PRO.sql","r").read()
        params = {'Lista_Precio':Lista_Precio,'Sucursal':Sucursal}
    elif Lista_Precio == "233":
        SQL = open("E:/Desarrollo/Art_Lista_Precios-/SQL/Query_Lista_Precio_BROU.sql","r").read()
        params = {'Lista_Precio':Lista_Precio}

    df = pd.read_sql_query(SQL,conexionOra,params=(params))
    #json = df.to_json(orient='records')

    #Lista_Precio_json = df.to_json()
    #print(json)


    return df

