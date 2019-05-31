from math import sqrt
import sys

try:
    zahl_1
except: 
    print('❌ Du hast die Variable zahl_1 nicht definiert.')
    sys.exit()
    
try:
    zahl_2
except: 
    print('❌ Du hast die Variable zahl_2 nicht definiert.')
    sys.exit()

try:
    summe
except: 
    print('❌ Du hast die Variable summe nicht definiert.')
    sys.exit()
    
try:
    assert type(summe) is int, 'Die Summe ist nicht vom Datentyp Integer. Sie soll aber eine Zahl sein.'
except AssertionError as inst:
    print ("❌ " + str(inst))
    sys.exit()   

try:
    assert summe == int(zahl_1) + int(zahl_2), 'Du hast die Summe nicht richtig berechnet. Überprüfe deine Rechnung.'    
except AssertionError as inst:
    print ("❌ " + str(inst))
    sys.exit()
 
print("✅ Sehr gut!")