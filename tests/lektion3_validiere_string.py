from math import sqrt
import sys

try:
    eingabe
except: 
    print('❌ Du hast die Variable eingabe nicht definiert.')
    sys.exit()
    
    
try:
    konvertierte_eingabe
except: 
    print('❌ Du hast die Variable konvertierte_eingabe nicht definiert.')
    sys.exit()

try:
    assert konvertierte_eingabe[0].isupper(), 'Der erste Buchstabe der Benutzereingabe ist nicht in einen Großbuchstaben konvertiert.'    
except AssertionError as inst:
    print ("❌ " + str(inst))
    sys.exit()
    
try:
    assert konvertierte_eingabe == eingabe.capitalize() + '!', 'Du hast kein Ausrufezeichen an die Eingabe angehängt.'
except AssertionError as inst:
    print ("❌ " + str(inst))
    sys.exit()
 
print("✅ Sehr gut!")