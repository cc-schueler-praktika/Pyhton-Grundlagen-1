from math import sqrt
import sys

try:
    note_1
except: 
    print('❌ Du hast die Variable note_1 nicht definiert.')
    sys.exit()
    
try:
    note_2
except: 
    print('❌ Du hast die Variable note_2 nicht definiert.')
    sys.exit()

try:
    note_3
except: 
    print('❌ Du hast die Variable note_3 nicht definiert.')
    sys.exit()

try:
    durchschnitt
except: 
    print('❌ Du hast die Variable durchschnitt nicht definiert.')
    sys.exit()
    
try:
    note_4
except: 
    print('❌ Du hast die Variable note_4 nicht definiert.')
    sys.exit()

try:
    assert note_4 == 4 * durchschnitt - note_1 - note_2 - note_3, 'Du hast die vierte Note nicht richtig berechnet. Überprüfe deine Rechnung.'    
except AssertionError as inst:
    print ("❌ " + str(inst))
    sys.exit()
 
print("✅ Sehr gut!")