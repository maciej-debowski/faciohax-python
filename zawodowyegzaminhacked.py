# Legalne cheaty do zawodowyegzamin.pl
# Autor: Maciej Dębowski 2 TEP

link = input("link: ")
import requests
import math
from htmldom import htmldom
data = {
    'send': 40, 
    'q1': 'A',
    'q2': 'A',
    'q3': 'A',
    'q4': 'A',
    'q5': 'A',
    'q6': 'A',
    'q7': 'A',
    'q8': 'A',
    'q9': 'A',
    'q10': 'A',
    'q11': 'A',
    'q12': 'A',
    'q13': 'A',
    'q14': 'A',
    'q15': 'A',
    'q16': 'A',
    'q17': 'A',
    'q18': 'A',
    'q19': 'A',
    'q20': 'A',
    'q21': 'A',
    'q22': 'A',
    'q23': 'A',
    'q24': 'A',
    'q25': 'A',
    'q26': 'A',
    'q27': 'A',
    'q28': 'A',
    'q29': 'A',
    'q30': 'A',
    'q31': 'A',
    'q32': 'A',
    'q33': 'A',
    'q34': 'A',
    'q35': 'A',
    'q36': 'A',
    'q37': 'A',
    'q38': 'A',
    'q39': 'A',
    'q40': 'A',
}

print(f" Zczytuje odpowiedzi z: {link}")

r = requests.post(url = link, data = data)
text = r.text

dom = htmldom.HtmlDom()
dom = dom.createDom(text)

labels = dom.find( "label" )

x = 1
y = -1
for label in labels:
    y+=1
    a = label.attr( "style" )
    b = a.split("background: ")
    if b[0] == 'Undefined Attribute': continue
    if b[1].split(";")[0] == "#66ff99":
        alphabet = 'ABCD'
        print(f"{x}. {alphabet[y % 4]}")
        x+=1
