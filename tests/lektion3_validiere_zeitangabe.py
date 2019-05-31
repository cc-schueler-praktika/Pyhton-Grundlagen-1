from math import sqrt
import sys

try:
    stunden
except: 
    print('❌ Du hast die Variable stunden nicht definiert.')
    sys.exit()
    
try:
    minuten
except: 
    print('❌ Du hast die Variable minuten nicht definiert.')
    sys.exit()

try:
    sekunden
except: 
    print('❌ Du hast die Variable sekunden nicht definiert.')
    sys.exit()

try:
    sekunden_gesamt
except: 
    print('❌ Du hast die Variable sekunden_gesamt nicht definiert.')
    sys.exit()

try:
    assert sekunden_gesamt == stunden * 3600 + minuten * 60 + sekunden, 'Du hast die Sekunden nicht richtig berechnet. Überprüfe deine Rechnung.'    
except AssertionError as inst:
    print ("❌ " + str(inst))
    sys.exit()
 
print("✅ Sehr gut!")