# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 12:15:28 2017

@author: patemi
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 12:59:13 2017

@author: patemi
"""
import pandas as pd
import os.path
from functools import reduce 

path = '\\\\apw-grskfs01\\GVAR2\\Global Risk Management\\MHI EONIA_SONI Snap Correction'
file = 'UAT.MarketArchive.2018-04-20.ada'

items=['OIS_EUR,1W']


#fullpath=path+file

#df_input=pd.read_csv('//FS002/patemi$/Python/Equities Input.csv', encoding='latin-1')
df_input=pd.read_table(os.path.join(path,file), skiprows=3)


allcols=[]

for item in items:
    cols = [col for col in df_input.columns if item.upper() in col.upper()]
    allcols.append(cols)

allcols=reduce(lambda x,y: x+y, allcols)



df_output=df_input.copy()
df_output.loc[:,allcols]=df_input.loc[:,allcols]


