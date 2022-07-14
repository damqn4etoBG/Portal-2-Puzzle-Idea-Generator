import random

color = '\033[95m'

#Elements
majorelements = ['Faith Plates','Light Bridges','Lasers','Funnels']
gels = ['Blue Gel','Orange Gel','No Gel']
cubes = ['1','2']
fields = ['Fizzler','Laser Field','Both']
fieldsnumber = ['1','2']
exitunlocked = ['Floor Button']

funnelbutton = 'Funnel Button (On the wall)'
laserrecirever = 'Laser Reciever'

#Choices
majorchoice = random.choice(majorelements)
gelchoice = random.choice(gels)
cubechoice = random.choice(cubes)
fieldschoice = random.choice(fields)
fieldsnumberchoice = random.choice(fieldsnumber)
exitunlockedchoice = random.choice(exitunlocked)

#Result
print(f"{color}Major: " + majorchoice)
print(f"{color}Gel: " + gelchoice)
print(f"{color}Cubes: " + cubechoice)
print(f"{color}Field: " + fieldschoice)

# Logic
if fieldschoice != 'Both':
    print(f"{color}Fields Number: " + fieldsnumberchoice)

if majorchoice == 'Funnels':
     print(f"{color}Exit is unlocked by: " + funnelbutton or exitunlockedchoice)
else:
    if majorchoice == 'Lasers':
         print(f"{color}Exit is unlocked by: " + laserrecirever)
    else:
        print(f"{color}Exit is unlocked by: " + exitunlockedchoice)