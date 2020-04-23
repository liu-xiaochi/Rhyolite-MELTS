# -*- coding: utf-8 -*-
# This python script generate melts files from an excel file.
import pandas as pd

# read excel file
excelname = 'input.xlsx'
sheetname = 'Sheet1'
df = pd.read_excel(excelname, sheet_name=sheetname)
print(df)

def convert_excel_melts(i, elements):
    with open('input/input_'+str(i+1).zfill(4)+'.melts', 'w') as f: # zfillで0埋め．桁数は任意のものを．
        f.write('Title: '+str(i+1)+'\n')
        for element in elements:
            f.write('Initial Composition: '+element+' '+str(df[element][i])+'\n')
        f.write('Initial Temperature: '+str(df['InitialTempC'][i])+'\n')
        f.write('Final Temperature: '+str(df['FinalTempC'][i])+'\n')
        f.write('Initial Pressure: '+str(df['InitialPbar'][i])+'\n')
        f.write('Final Pressure: '+str(df['FinalPbar'][i])+'\n')
        f.write('Increment Temperature: '+str(df['dT'][i])+'\n')
        f.write('Increment Pressure: '+str(df['dP'][i])+'\n')
        f.write('dp/dt: '+str(df['dP/dT'][i])+'\n')
        f.write('log fo2 Path: '+str(df['fO2'][i]))
        f.close()

# list of input elements
elements = ['SiO2', 'TiO2', 'Al2O3', 'FeO', 'MnO', 'MgO', 'CaO', 'Na2O', 'K2O', 'P2O5', 'H2O']
# Need "input" directory in advance
for i in range(3):
    convert_excel_melts(i, elements)