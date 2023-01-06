#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 17:06:17 2022

@author: agneswardega
"""

import pandas as pd
import numpy

#Wczytaj dane do formatu DataFrame wybierając tylko 2500 obiektów z pliku
data_frame = pd.read_csv('OneDrive - Uniwersytet Ekonomiczny w Katowicach/UE sem. V/Programowanie w języku Python/Ćwiczenia/Projekt 1/EURUSD_H4.csv', nrows=2500)

#Usuń kolumny oznaczone jako SMA14IND oraz SMA50IND;
data_frame.pop('SMA14IND')
data_frame.pop('SMA50IND')

# Dla kolumny Close policz liczbę wystąpień danych pustych. Napraw
# dane w taki sposób, że pusta wartość zastępowana jest wartością
# uśrednioną dwóch sąsiednich elementów;
data_frame['Close'] = data_frame['Close'].interpolate()

# W przypadku danych pustych w kolumnach SMA14 i SMA50 –
# napraw wartości puste dowolną metodą;
data_frame['SMA14'] = data_frame['SMA14'].fillna(14)
data_frame['SMA50'] = data_frame['SMA50'].fillna(50)

# Dla wszystkich pozostałych atrybutów wypełnij wartości puste
# zerami;
data_frame = data_frame.fillna(0)

# Wyznacz korelację pomiędzy SMA14 i SMA50;
corrSMA14SMA50 = data_frame['SMA14'].corr(data_frame['SMA50'])

# Wyznacz korelację pomiędzy Close oraz SMA14 a także pomiędzy
# Close oraz SMA50. Usuń kolumnę, dla której wartość korelacji była
# większa;
corrCloseSMA14 = data_frame['Close'].corr(data_frame['SMA14'])

corrCloseSMA50 = data_frame['Close'].corr(data_frame['SMA50'])

if corrCloseSMA14 > corrCloseSMA50:
    data_frame.pop('SMA14')
else:
    data_frame.pop('SMA50')

# Podaj liczbę elementów ujemnych dla atrybutu CCI;
cciLessThan0 = (data_frame['CCI'] < 0).sum()

# Podaj informację o wartości maksymalnej i minialnej dla każdego
# atrybutu;
dataMax = data_frame.max()

dataMin = data_frame.min()

# Przeprowadź normalizację dwóch wybranych atrybutów;
atrybuty = ['Bulls', 'CCI'] #dwa atrybuty do normalizacji

#Normalizacja zodnie ze wzorem
for atrybut in atrybuty:
    max = data_frame[atrybut].max()
    min = data_frame[atrybut].min()
    data_frame[atrybut] = (data_frame[atrybut] - min) / (max - min)

# Przeprowadź dyskretyzację dwóch wybranych atrybutów (podział
# odpowiednio na 2 i 4 kategorie);
seriaRSI = pd.cut(pd.Series(numpy.array(data_frame['RSI'])), 2, labels=['Lower', 'Upper'])
seriaDM = pd.cut(pd.Series(numpy.array(data_frame['DM'])), 4, labels=['Lower', 'Medium', 'Higher', 'Upper'])

# Dane po preprocessingu zapisz do pliku w formacie JSON.
data_frame.to_json('OneDrive - Uniwersytet Ekonomiczny w Katowicach/UE sem. V/Programowanie w języku Python/Ćwiczenia/Projekt 1//Projekt1_czesc1.json')