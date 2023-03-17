"""
    @Author => Aman Raj
    @Encoding => UTF-8
    @File Created => 02/02/2023
"""
import pandas as pd
import sqlite3 as sql
import os

class Converter_Sql(object):
    def convert(self, file, to_file:str, table:str=r"SELECT * FROM data_base",specific_size:int=2e+8):
        connect = sql.connect(file)
        files = pd.read_sql(table, connect)
        size = int(os.path.getsize(file))
        if size >= int(specific_size):
            files.to_pickle(str(to_file) + '.pkl')
        else:
            files.to_csv(str(to_file) + '.csv')
