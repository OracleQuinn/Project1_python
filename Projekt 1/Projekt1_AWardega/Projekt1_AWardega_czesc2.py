#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 15:05:03 2022

@author: agneswardega
"""

import pandas as pd
import random

#Odczyt danych z pliku CSV do DataFrame
data_frame = pd.read_csv('OneDrive - Uniwersytet Ekonomiczny w Katowicach/UE sem. V/Programowanie w języku Python/Ćwiczenia/Projekt 1/EURUSD_H4.csv', nrows=2500)

'''
Należy wygenerować sztuczny zestaw danych o takiej samej wielkości, jak zestaw bazowy. Jednocześnie należy kierować się następującymi założeniami:
1. w pierwszym wierszu dla danych znajdują się elementy losowe z zakresu ⟨mini, maxi⟩, gdzie mini jest wartością minimalną i-tego atrybutu, a wartość maxi jest wartością maksymalną i-tego atrybutu;

2. losowe wartości w poszczególnych kolumnach nie mogą wyjść poza wskazany zakres ⟨mini, maxi⟩, dlai = 1, 2, ..., k gdzie k jest liczbą atrybutów z wyłączeniem atrybutu decyzyjnego;

3. zmiana wartości dla poszczególnych atrybutów w kolejnych wierszach musi być w zakresie ⟨prevv al − prevv al· 1%; prevv al + prevv al· 1%⟩;

4. w przypadku, gdy wynikiem będzie wartość poza zakresem max (lub min) należy jako nową wartość przyjąć właśnie dany zakres;

5. po wygenerowaniu tablicy należy policzyć korelację pomiędzy każdą z kolumn z pierwszego zestawu oraz odpowiadającym kolumnom z
drugiego zestawu (tj. korelacja pomiędzy pierwszymi kolumnami, korelacja pomiędzy drugimi kolumnami i tak dalej). 

Działamy tylko na kolumnach liczbowych - czyli atrybut decyzyjny pomijamy.
'''
ids = []

columns = ['Close', 'SMA14', 'SMA50', 'SMA14IND', 'SMA50IND', 'Bulls', 'CCI', 'DM', 'OSMA', 'RSI', 'Stoch']

minClose = data_frame['Close'].min()
maxClose = data_frame['Close'].max()
minSMA14 = data_frame['SMA14'].min()
maxSMA14 = data_frame['SMA14'].max()
minSMA50 = data_frame['SMA50'].min()
maxSMA50 = data_frame['SMA50'].max()
minSMA14IND = data_frame['SMA14IND'].min()
maxSMA14IND = data_frame['SMA14IND'].max()
minSMA50IND = data_frame['SMA50IND'].min()
maxSMA50IND = data_frame['SMA50IND'].max()
minBulls = data_frame['Bulls'].min()
maxBulls = data_frame['Bulls'].max()
minCCI = data_frame['CCI'].min()
maxCCI = data_frame['CCI'].max()
minDM = data_frame['DM'].min()
maxDM = data_frame['DM'].max()
minOSMA = data_frame['OSMA'].min()
maxOSMA = data_frame['OSMA'].max()
minRSI = data_frame['RSI'].min()
maxRSI = data_frame['RSI'].max()
minStoch = data_frame['Stoch'].min()
maxStoch = data_frame['Stoch'].max()

randomData = {
    'Close': [random.uniform(minClose, maxClose)],
    'SMA14': [random.uniform(minSMA14, maxSMA14)],
    'SMA50': [random.uniform(minSMA50, maxSMA50)],
    'SMA14IND': [random.uniform(minSMA14IND, maxSMA14IND)],
    'SMA50IND': [random.uniform(minSMA50IND, maxSMA50IND)],
    'Bulls': [random.uniform(minBulls, maxBulls)],
    'CCI': [random.uniform(minCCI, maxCCI)],
    'DM': [random.uniform(minDM, maxDM)],
    'OSMA': [random.uniform(minOSMA, maxOSMA)],
    'RSI': [random.uniform(minRSI, maxRSI)],
    'Stoch': [random.uniform(minStoch, maxStoch)],
}

for i in range(2499):
    fixedId = i + 1
    ids.append(fixedId)
    randomData['Close'].append(random.uniform(randomData['Close'][i] - randomData['Close'][i] * 0.01, randomData['Close'][i] + randomData['Close'][i] * 0.01))
    randomData['SMA14'].append(random.uniform(randomData['SMA14'][i] - randomData['SMA14'][i] * 0.01, randomData['SMA14'][i] + randomData['SMA14'][i] * 0.01))
    randomData['SMA50'].append(random.uniform(randomData['SMA50'][i] - randomData['SMA50'][i] * 0.01, randomData['SMA50'][i] + randomData['SMA50'][i] * 0.01))
    randomData['SMA14IND'].append(random.uniform(randomData['SMA14IND'][i] - randomData['SMA14IND'][i] * 0.01, randomData['SMA14IND'][i] + randomData['SMA14IND'][i] * 0.01))
    randomData['SMA50IND'].append(random.uniform(randomData['SMA50IND'][i] - randomData['SMA50IND'][i] * 0.01, randomData['SMA50IND'][i] + randomData['SMA50IND'][i] * 0.01))
    randomData['Bulls'].append(random.uniform(randomData['Bulls'][i] - randomData['Bulls'][i] * 0.01, randomData['Bulls'][i] + randomData['Bulls'][i] * 0.01))
    randomData['CCI'].append(random.uniform(randomData['CCI'][i] - randomData['CCI'][i] * 0.01, randomData['CCI'][i] + randomData['CCI'][i] * 0.01))
    randomData['DM'].append(random.uniform(randomData['DM'][i] - randomData['DM'][i] * 0.01, randomData['DM'][i] + randomData['DM'][i] * 0.01))
    randomData['OSMA'].append(random.uniform(randomData['OSMA'][i] - randomData['OSMA'][i] * 0.01, randomData['OSMA'][i] + randomData['OSMA'][i] * 0.01))
    randomData['RSI'].append(random.uniform(randomData['RSI'][i] - randomData['RSI'][i] * 0.01, randomData['RSI'][i] + randomData['RSI'][i] * 0.01))
    randomData['Stoch'].append(random.uniform(randomData['Stoch'][i] - randomData['Stoch'][i] * 0.01, randomData['Stoch'][i] + randomData['Stoch'][i] * 0.01))

ids.append(2500)
random_data_frame = pd.DataFrame(randomData, columns=columns, index=ids)

korelacjaClose = random_data_frame['Close'].corr(data_frame['Close'])
korelacjaSMA14 = random_data_frame['SMA14'].corr(data_frame['SMA14'])
korelacjaSMA50 = random_data_frame['SMA50'].corr(data_frame['SMA50'])
korelacjaSMA14IND = random_data_frame['SMA14IND'].corr(data_frame['SMA14IND'])
korelacjaSMA50IND = random_data_frame['SMA50IND'].corr(data_frame['SMA50IND'])
korelacjaBulls = random_data_frame['Bulls'].corr(data_frame['Bulls'])
korelacjaCCI = random_data_frame['CCI'].corr(data_frame['CCI'])
korelacjaDM = random_data_frame['DM'].corr(data_frame['DM'])
korelacjaOSMA = random_data_frame['OSMA'].corr(data_frame['OSMA'])
korelacjaRSI = random_data_frame['RSI'].corr(data_frame['RSI'])
korelacjaStoch = random_data_frame['Stoch'].corr(data_frame['Stoch'])

random_data_frame.to_csv('OneDrive - Uniwersytet Ekonomiczny w Katowicach/UE sem. V/Programowanie w języku Python/Ćwiczenia/Projekt 1//Projekt1_czesc2.csv')