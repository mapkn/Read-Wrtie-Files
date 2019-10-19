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

path = '//apw-grskfs01/GVAR2/Global Risk Management/shock_records/Shock/'
#file = 'SHOCK_RECORD_20171201_30Nov2017_Succeeded_1.csv'
file = 'erm_sr_bond_extraction_14Dec2017_Succeeded_2.csv'


######## Deal with Windows directory string###########

#Outputs
#path2 = '\\\\apw-grskfs01/GVAR2\\Global Risk Management\\shock_records\\Shock'
path2='H:\\DESKTOP\\To Delete'
file2 = 'Output.csv'

path = '/'.join(path.split('\\'))

################################################

fullpath=path+file

#df_input=pd.read_csv('//FS002/patemi$/Python/Equities Input.csv', encoding='latin-1')
df_input=pd.read_csv(fullpath, encoding='latin-1', low_memory=False)

#df_input=pd.read_csv(fullpath, encoding='latin-1', low_memory=False)

# Skip rows
#df_input=pd.read_csv(fullpath, encoding='latin-1', low_memory=False, skiprows=2)

#########################Saving dataframe to csv ##################
df=df_input[df_input['MHI_SECURITY_ID']=='100001911241']
#df=df_input[df_input['POSITION_ID']==100001920719]
#df=df_input[df_input['M_ORIGIN_RE']==1951]


df.to_csv(os.path.join(path2,file2))


########################################################
