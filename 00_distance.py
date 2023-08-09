#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pprint import pprint
# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2


distances = dict()
moscow = sites['Moscow']
london = sites['London']
paris = sites['Paris']
m_l = ((moscow[0] - london[0])**2 + (moscow[1] - london[1])**2)**0.5
m_p = ((moscow[0] - paris[0])**2 + (moscow[1] - paris[1])**2)**0.5
l_p = ((london[0] - paris[0])**2 + (london[1] - paris[1])**2)**0.5
distances['Moscow'] = {}
distances['Moscow']['London'] = m_l
distances['Moscow']['Paris'] = m_p
distances['London'] = {}
distances['London']['Moscow'] = m_l
distances['London']['Paris'] = l_p
distances['Paris'] = {}
distances['Paris']['Moscow'] = m_p
distances['Paris']['London'] = l_p

pprint(distances)
print()
print(distances['Moscow']['Paris'])



