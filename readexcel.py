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



path='G:\\\Market Risk Management\\Mitul\\Murex Curve Changes May 2018'
file1 = 'SR_Bonds_GPSREC.xlsx'
sheet='Sheet1'

# Read Excel

df_input1=pd.read_excel(os.path.join(path,file1), sheetname = sheet, encoding='latin-1')




########## Pivot Tables


df=df_input1.loc[df_input1['MARKETDATA_NAME']=='EUR SOVEREIGN GERMANY']
df_Pivot=df.pivot_table(index='SHIFT__VALUE', columns='GRID__POINT', values='PV_CHANGE_UAT', aggfunc='sum')

############################


# Excel Writer

writer = pd.ExcelWriter('output.xlsx')
df_Pivot.to_excel(writer,'Sheet1')
df_Pivot.to_excel(writer,'Sheet2')
writer.save()

