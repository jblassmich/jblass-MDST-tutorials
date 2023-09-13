import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("../data/states_edu.csv")
df.head()
# print(df['GRADES_ALL_G'].isna().sum())

# Data cleanup begins here

# Renaming various columns
df.set_index('PRIMARY_KEY')
df.rename({
    'GRADES_PK_G':'ENROLL_PREK',
    'GRADES_KG_G':'ENROLL_KINDER',
    'GRADES_4_G':'ENROLL_4',
    'GRADES_8_G':'ENROLL_8',
    'GRADES_12_G':'ENROLL_12',
    'GRADES_1_8_G':'ENROLL_PRIMARY',
    'GRADES_9_12_G':'ENROLL_HS',
    'GRADES_ALL_G':'ENROLL_ALL',
    'ENROLL':'ENROLL_ALL_EST'
    },
    axis=1,inplace=True)

# My plan is to focus on the correlation between increases in total 
# enrollment, and increases in 8th grade math scores, so I'm dropping any rows 
# that don't have 'AVG_MATH_8_SCORE' values and filling rows with nan 'ENROLL_ALL'
# values with the sum of the other enrollment data

df.dropna(subset=['AVG_MATH_8_SCORE'], inplace=True)
df['ENROLL_ALL'] = df['ENROLL_ALL'].fillna(df["ENROLL_PREK"]+df["ENROLL_PRIMARY"]+df["ENROLL_HS"])
print(df['YEAR'].unique())

states = df.groupby('STATE')
print(states)








# year2019df = df[df['YEAR'] == 2019]
# year2000df = df[df['YEAR'] == 2000]
# ENROLL_DATA_2000 = dict()
# year2019df['2000_ENROLLMENT_DATA'] len(year2019df.index)
# for i in range(len(year2019df.index)):
#     for k in range(len(year2019df.index)):
#         if year2019df.iloc[i]['STATE'] == year2000df.iloc[k]['STATE']:
#             ENROLL_DATA_2000[i] == year2000df.iloc[k]['ENROLL_ALL']

            # year2019df.iloc[i]['ENROLL_ALL_2000'] = year2000df.iloc[k]['ENROLL_ALL']
# year2019df['2000_ENROLL_ALL'] = year2000df['ENROLL_ALL'].tolist()
# print(ENROLL_DATA_2000)
# print(year2019df.head())
# print(year2000df.iloc[0]['STATE'])
