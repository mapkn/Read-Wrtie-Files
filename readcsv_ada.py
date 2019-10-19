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
import numpy as np

from datetime import datetime, timedelta
from functools import reduce 


items=[':SprdCurve.BND_EURO_Corp_A,',
':SprdCurve.BND_EURO_Corp_AA,',
':SprdCurve.BND_EURO_Corp_BBB,',
':SprdCurve.BND_EURO_Fin_A,',
':SprdCurve.BND_EURO_Fin_AA,',
':SprdCurve.BND_EURO_Fin_BBB,',
':SprdCurve.BND_GB_Corp_A,',
':SprdCurve.BND_GB_Corp_BBB,',
':SprdCurve.BND_GB_Fin_A,',
':SprdCurve.BND_GB_Fin_AAA,',
':SprdCurve.BND_GB_Fin_BBB,',
':SprdCurve.SUP_EUR,']


def from_excel_ordinal(ordinal, epoch=datetime(1900, 1, 1)):
    # Adapted from above, thanks to @Martijn Pieters 

    ord=float(ordinal)    
    if ord > 59:
        ord -= 1  # Excel leap year bug, 1900 is not a leap year!
    inDays = int(ord)
    frac = ord - inDays
    inSecs = int(round(frac * 86400.0))
    return epoch + timedelta(days=inDays - 1, seconds=inSecs) # epoch is day 1

from_excelordinal=np.vectorize(from_excel_ordinal)

path = '\\\\apw-grskfs01\\GVAR2\\Global Risk Management\\StressedVaR Period Change'
file = 'MarketArchiveSt.2018-03-13_PRD2.csv'




df_input=pd.read_csv(os.path.join(path,file), encoding='latin-1', low_memory=False, parse_dates=[0])
df_input=df_input.set_index('DATE')
df_input.index=from_excelordinal(df_input.index)

allcols=[]

#cols = [col for col in df_input.columns if 'SUP_EUR' in col.upper()]

for item in items:
    cols = [col for col in df_input.columns if item.upper() in col.upper()]
    allcols.append(cols)
#cols = [col for col in df_input.columns if items in col.upper()]

allcols=reduce(lambda x,y: x+y, allcols)

#cols = df_input.columns[df_input.columns.str.contains('BND_EURO_CORP')]
#col=df_input.columns.values
df_filtered=df_input.filter(items=allcols, axis=1)

#for item in items:
#    df_filtered=df_input.filter(like=item, axis=1)

#df_filtered=df_input.filter(like='EURO_CORP', axis=1)
#df_filtered.plot();


# compute 1st differences of dataframe data
df_diff=df_filtered.diff(periods=1)

#df_diff.plot.scatter(x='DATE', y='');


x=df_diff.describe(percentiles=[0.01,0.025,0.975,0.99])
x.to_clipboard()

#df_diff_0=df_diff.astype(bool).sum(axis=0)

df_diff_0=(df_diff==0).astype(int).sum(axis=0)

#print(df_diff.describe())

#df_diff.hist(bins=20)




