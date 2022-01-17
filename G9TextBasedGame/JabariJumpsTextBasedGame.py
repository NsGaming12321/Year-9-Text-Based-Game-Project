import random
import os
import time

health = 3
maxhealth = 3
#total damage taken = damage taken / defense
defense = 0
#from armour here is list of pieces
#leather shirt - 5 defense
#nathans armour - 80 defense
confidence = 0
intelligence = 0
armourType = "no","leather shirt","nathans armour"
armourTypeNum = 0
level = 1
spaceNum = 2
firstkeyunlocked = False
bushHeartFound = False
fightbully = False
madeFriend = False
secondkeyfound = False
padcovered = False
thirdkeyfound = False

map1 = """
|--------|              |--------------------------------------------------|
|  13  n |              |                                                  |
|        |              |  8 >--<               7                3  >--<   |
|n       |              |           ~~~~~~~~~~~~~~~~~~~~~~~~~~~     >--<   |
|  12  n ----------------      |--- ~~~~~~~~~~~~~~~~~~~~~~~~~~~     >--<   |
|            n   |         9   |    ~~~~~~~~~~~~2~~~~~~~~~~~~~~  4  >--<   |
|    n    11     |             |    ~~~~~~~~~~~~~~~~~~~~~~~~~~~     >--<   |
|  n          n  =   10        |    ~~~~~~~~~~~~~~~~~~~~~~~~~~~     >--<   |
|      n         |         1                    6                5  >--<   |
|   n        n   |                   #########################             |   
|--------------------------------------------------------------------------|
"""
#heart in bushes (6)
#= is a gate, inspect the chair at 8 to get the key-
#behind 12's rock, there is a leather shirt (+5 defense)!
#by unlocking the gate, you gain 1 intelligence and 1 confidence
#by jumping, you gain 1 confidence (repeats infitely)

map2 = """
|--------------------------|
|     ,--<|    . . . .     |
|      6  |  . [][][][] .  |
|I 5      |    . . .  . 9  |
|---   ---|----------      |
|                          |
|      7         +   { }   |
|           |              |
|]4        \|   +    `     |
|        2 \|      8  `    |
|,,3       \|    `   +     |
|,,     1   |              |
|----||---------------------
"""

#in one of the boots, there is a heart
#the painting of Jabari's mom allows the father to call Jabari for dinner
#by playing with the toys, jabari gains 1 intelligence (repeats infinetely)

map3 = """
|-----||------------------------|
|     6           4             |
|]            */  */  */   /    |
|]                              |
|             8/  */   /7 */ 5  |
|    |                          |
|    | 2      1/   /  */  */    |
|    |                 3        |
|-------------------------------|
"""

#behind the teachers desk, there is a heart
#by being in class until the end of the day, you gain 10 intelligence
#if you attempt to leave class, you get caught and loose half your confidence and half your inteligence
#by talking with Nathan(3), you gain 3 conifidence and 1 intelligence. The class then ends with you making a friend

map4 = """
----------------------------------------
       O                         [][][]
      -|-      3         2          1
       /\                        [][][]
----------------------------------------
"""

#heart in lockers
#jabari is confronted with a bully, he can either get a teacher or fight the bully
#if jabari beats the bully (15 intelligence), only he gets in trouble and loose half your confidence and half your intelligence
#if jabari looses the fight (< 15 inteligence) you lose half your confidence
#if jabari gets a teacher, he gets 10 inteligence and 3 confidence

map5 = """
|------------------------------------------------------|
|       |                        |                     |
|   1   |    <>     <>     <>    |         6           |
|       |                        |                     |
|---||--|                        |                     |
|            2      3      4    5=                     |
|                                |         8           |
|-----------------------------------------||-----------|
|       16   |  14    |    12    |                     |
|            |        |          |         9      [|   |
|   17    |     |          |     =11              [| 10|
|    -O    | 15  |   13     |     |                     |
|------------------------------------------------------|
"""

#to get in the cave. you need nathans armour.
#to get into the cave, you need 30 confience
#for the dungeon puzzle, you need 20 intelligence

def drawMap(mapNum):
    if(mapNum == 1):
        print(map1)
    if(mapNum == 2):
        print(map2)
    if(mapNum == 3):
        print(map3)
    if(mapNum == 4):
        print(map4)
    if(mapNum == 5):
        print(map5)

while(level <= 5):
    if(level == 1):
        time.sleep(2)
        os.system('clear')
        print("Welcome To Jabari's Adventure!")
        time.sleep(2)
        print("Type \"Start\" to start!")
        userInput = input()
        while("start" not in userInput.lower()):
            print("Invalid Response, please try again")
            userInput = input()
        os.system('clear')
        print("Your at the pool with your father and sister")
        time.sleep(2)
        print("You just jumped off the diving board for the first time!")
        time.sleep(2)
        print()
        print("Task: Explore the pool area")
        time.sleep(2)
        print()
        print("Type \"help\" for help on some commands you can use")
        while(level == 1):
            userInput = input()
            if("help map" in userInput.lower()):
                drawMap(1)
                print("This is the map of the current stage you are on. Here you can see a bunch of numbers and some decoration. Each number represents a location you can be at. Type \"map\" to see what number you are currently on!")
                print()
            elif("help check health" in userInput.lower()):
                print("This shows the current amount of health you currently have. You can increase this by finding a heart. A heart fills up your heath and increases your max health")
                print()
            elif("help check max health" in userInput.lower()):
                print("This shows the current amount of health you currently have. You can increase this by finding hearts in different stages. 1 Heart = 5 Health")
                print()
            elif("help check defense" in userInput.lower()):
                print("This shows the current amount of defense you currently have. You can increase defense by upgrading your armor")
                print()
            elif("help check confidence" in userInput.lower()):
                print("This is your confidence level. You can increase this by doing this that make your more confident activities e.g. jumping off the diving board. A lot of things rely on confidence in this game so make sure yours stays high.")
                print()
            elif("help check intelligence" in userInput.lower()):
                print("This is your intelligence level. You can increase this by doing this that make you smarter e.g. playing with toys. A lot of things rely on intelligence in this game so make sure yours stays high.")
                print()
            elif("help check inspect" in userInput.lower()):
                print("This command allows you to inspect things depending on which space your on. Each space has its own inspection area, so make sure to visit them all!")
            elif("help" in userInput.lower()):
                print()
                print("Here are some commands you can try. Type \"help command\" to get help with that specific command")
                time.sleep(2)
                print()
                print("map")
                print("move left")
                print("move right")
                print("move up")
                print("move down")
                print("check health")
                print("check max health")
                print("check defense")
                print("check confidence")
                print("check intelligence")
                print("inspect")
                print()
            elif("map" in userInput.lower()):
                drawMap(level)
                print("You are on space:",spaceNum)
            elif("move left" in userInput.lower()):
                if(spaceNum == 2):
                    print("You get out of the pool from the left side")
                    spaceNum = 9
                elif(spaceNum == 7):
                    print("You move towards the lonely chair")
                    spaceNum = 8
                elif(spaceNum == 6):
                    print("You move right next to the diving board")
                    spaceNum = 1
                elif(spaceNum == 5):
                    print("You move towards bushes")
                    spaceNum = 6
                elif(spaceNum == 4):
                    print("You jumped back in the pool")
                    spaceNum = 2
                elif(spaceNum == 3):
                    print("You moved left")
                    spaceNum = 7
                elif(spaceNum == 9):
                    print("You move towards a gate")
                    spaceNum = 10
                elif(spaceNum == 1):
                    print("You have moved towards a gate")
                    spaceNum = 10
                elif(spaceNum == 10 and firstkeyunlocked == True):
                    print("You unlocked the gate and went through. You see a bunch of rocks around you")
                    spaceNum = 11
                elif(spaceNum == 10 and firstkeyunlocked == False):
                    print("The gate is locked. Find the key")
                elif(spaceNum == 11):
                    print("You navigate through rocks")
                    spaceNum = 12
                else:
                    print("You can't move this way")
                print()
            elif("move right" in userInput.lower()):
                if(spaceNum == 7):
                    spaceNum = 3
                    print("You move over to some chairs")
                elif(spaceNum == 2):
                    spaceNum = 4
                    print("You get out of the pool on the right")
                elif(spaceNum == 6):
                    spaceNum = 5
                    print("You move over to some chairs")
                elif(spaceNum == 8):
                    spaceNum = 7
                    print("You moved to the right")
                elif(spaceNum == 9):
                    spaceNum = 2
                    print("You got back in the pool")
                elif(spaceNum == 1):
                    spaceNum = 6
                    print("You moved over to some bushes")
                elif(spaceNum == 10):
                    spaceNum = 1
                    print("You moved towards the diving board")
                elif(spaceNum == 11):
                    print("You navigate back through the rocks")
                    spaceNum = 10
                elif(spaceNum == 12):
                    print("You navigate further back through the rocks")
                    spaceNum = 11
                else:
                    print("You can't move this way")
                print()
            elif("move up" in userInput.lower()):
                if(spaceNum == 12):
                    print("You reach a dead end but notice something behind one of the rocks")
                    spaceNum = 13
                elif(spaceNum == 11):
                    print("You continue to navigate through the rocks")
                    spaceNum = 12
                elif(spaceNum == 10):
                    print("You moved up")
                    spaceNum = 9
                elif(spaceNum == 1):
                    print("You moved up")
                    spaceNum = 9
                elif(spaceNum == 9):
                    print("You move over to one singular chair")
                    spaceNum = 8
                elif(spaceNum == 6):
                    print("You jump back into the water")
                    spaceNum = 2
                elif(spaceNum == 2):
                    print("You hop out of the pool")
                    spaceNum = 7
                elif(spaceNum == 5):
                    print("You continue to move down the row of chairs")
                    spaceNum = 4
                elif(spaceNum == 4):
                    print("You continue to move down the row of chairs")
                    spaceNum = 3
                else:
                    print("You can't move this way")
                print()
            elif("move down" in userInput.lower()):
                if(spaceNum == 13):
                    print("You start to navigate back through the rocks")
                    spaceNum = 12
                elif(spaceNum == 12):
                    print("You continue to navigate back through the rocks")
                    spaceNum = 11
                elif(spaceNum == 10):
                    print("You move back towards the diving board")
                    spaceNum = 1
                elif(spaceNum == 9):
                    print("You move back towards the diving board")
                    spaceNum = 1
                elif(spaceNum == 8):
                    print("You moved down")
                    spaceNum = 9
                elif(spaceNum == 7):
                    print("You jump back into the pool")
                    spaceNum = 2
                elif(spaceNum == 2):
                    print("You get out of the water and go over to some bushes")
                    spaceNum = 6
                elif(spaceNum == 3):
                    print("You move along some chairs")
                    spaceNum = 4
                elif(spaceNum == 4):
                    print("You move along some chairs")
                    spaceNum = 5
                else:
                    print("You can't move this way")
                print()
            elif("inspect" in userInput.lower()):
                if(spaceNum == 2):
                    print("You go underwater to see if there is anything to collect. Sadly, you don't find anything")
                if(spaceNum == 1):
                    print("You climb up the diving board and jump off. You gained 1 Confience")
                    print("You are now in the pool")
                    confidence += 1
                    spaceNum = 2
                if(spaceNum == 3):
                    print("You take a look at a chair, but don't find anything")
                if(spaceNum == 4):
                    print("You take a look at a chair, but don't find anything")
                if(spaceNum == 5):
                    print("You take a look at a chair, but don't find anything")
                if(spaceNum == 6):
                    if(bushHeartFound == False):
                        print("You look in the bushes and find a heart! You gained 1 Max Health")
                        maxhealth += 1
                    else:
                        print("You already found the heart here")
                if(spaceNum == 7):
                    print("There is nothing to inspect over here")
                if(spaceNum == 8):
                    if(firstkeyunlocked == False):
                        print("You found a key!")
                        firstkeyunlocked = True
                    else:
                        print("You already found the key here")
                if(spaceNum == 9):
                    print("There is nothing to inspect here")
                if(spaceNum == 10):
                    print("You see a gate, but it looks like it requires a key")
                if(spaceNum == 11):
                    print("You see many rocks surround your presence")
                if(spaceNum == 12):
                    print("You can see the end of the rocky graveyard")
                if(spaceNum == 13):
                    print("You find a Leather Shirt behind the rock! You gained 5 defense")
                    armourTypeNum = 1
                    print("Your dad begins to call you. He says that we are going")
                    time.sleep(1)
                    print("You get in the car and leave the pool")
                    print("LEVEL 1 CLEARED!")
                    level = 2
                    mapnum = 2
            elif("check health" in userInput.lower()):
                print("Your current health is:",health)
                print()
            elif("check max health" in userInput.lower()):
                print("Your current max health is:",maxhealth)
                print()
            elif("check defense" in userInput.lower()):
                print("Your current defense level is:",defense)
                print("You have",armourType[armourTypeNum],"armour")
                print()
            elif("check confidence" in userInput.lower()):
                print("Your current confidence is:",confidence)
                print()
            elif("check intelligence" in userInput.lower()):
                print("Your current intelligence is:",intelligence)
                print()
            else:
                print("Invalid Response, please try again")
                print()
    if(level == 2):
        time.sleep(2)
        os.system('clear')
        time.sleep(2)
        print("You make it home with your father and sister")
        time.sleep(2)
        print("Your father says that dinner will be ready soon")
        time.sleep(2)
        print()
        print("Task: Explore your house")
        time.sleep(2)
        print()
        print("Type \"help\" for help on some commands you can use")
        spaceNum = 1
        while(level == 2):
            userInput = input()
            if("help map" in userInput.lower()):
                drawMap(mapnum)
                print("This is the map of the current stage you are on. Here you can see a bunch of numbers and some decoration. Each number represents a location you can be at. Type \"map\" to see what number you are currently on!")
                print()
            elif("help check health" in userInput.lower()):
                print("This shows the current amount of health you currently have. You can increase this by finding a heart. A heart fills up your heath and increases your max health")
                print()
            elif("help check max health" in userInput.lower()):
                print("This shows the current amount of health you currently have. You can increase this by finding hearts in different stages. 1 Heart = 5 Health")
                print()
            elif("help check defense" in userInput.lower()):
                print("This shows the current amount of defense you currently have. You can increase defense by upgrading your armor")
                print()
            elif("help check confidence" in userInput.lower()):
                print("This is your confidence level. You can increase this by doing this that make your more confident activities e.g. jumping off the diving board. A lot of things rely on confidence in this game so make sure yours stays high.")
                print()
            elif("help check intelligence" in userInput.lower()):
                print("This is your intelligence level. You can increase this by doing this that make you smarter e.g. playing with toys. A lot of things rely on intelligence in this game so make sure yours stays high.")
                print()
            elif("help check inspect" in userInput.lower()):
                print("This command allows you to inspect things depending on which space your on. Each space has its own inspection area, so make sure to visit them all!")
            elif("help" in userInput.lower()):
                print()
                print("Here are some commands you can try. Type \"help command\" to get help with that specific command")
                time.sleep(2)
                print()
                print("map")
                print("move left")
                print("move right")
                print("move up")
                print("move down")
                print("check health")
                print("check max health")
                print("check defense")
                print("check confidence")
                print("check intelligence")
                print("inspect")
                print()
            elif("move left" in userInput.lower()):
                if(spaceNum == 1):
                    spaceNum = 3
                    print("You move over towards some boots")
                elif(spaceNum == 2):
                    spaceNum = 4
                    print("You walk over to a painting")
                elif(spaceNum == 6):
                    spaceNum = 5
                    print("You move towards a table in the corner of the room")
                elif(spaceNum == 8):
                    spaceNum = 7
                    print("You moved upwards and left")
                else:
                    print("You can't move this way")
                print()
            elif("move right" in userInput.lower()):
                if(spaceNum == 3):
                    spaceNum = 1
                    print("You walk back to the entrance of the house")
                elif(spaceNum == 4):
                    spaceNum = 2
                    print("You walk back over to the coat hangers")
                elif(spaceNum == 5):
                    spaceNum = 6
                    print("You walk over to your fathers bed")
                elif(spaceNum == 7):
                    spaceNum = 8
                    print("You walk over to the toy area")
                else:
                    print("You can't move this way")
                print()
            elif("move up" in userInput.lower()):
                if(spaceNum == 1):
                    spaceNum = 2
                    print("You move over towards the coat hangers")
                elif(spaceNum == 2):
                    spaceNum = 7
                    print("You move over towards a picture")
                elif(spaceNum == 3):
                    spaceNum = 7
                    print("You moved up")
                elif(spaceNum == 4):
                    spaceNum = 7
                    print("You moved up")
                elif(spaceNum == 7):
                    spaceNum = 5
                    print("You walk into your fathers room and notice a table")
                elif(spaceNum == 5):
                    spaceNum = 6
                    print("You walk over to your fathers bed")
                elif(spaceNum == 8):
                    spaceNum = 9
                    print("You walk into the dining room. In the corner you can see your father cooking dinner")
                else:
                    print("You can't move this way")
                print()
            elif("move down" in userInput.lower()):
                if(spaceNum == 2):
                        spaceNum = 1
                        print("You move back to the entrance of your home")
                elif(spaceNum == 4):
                        spaceNum = 3
                        print("You move over towards some boots")
                elif(spaceNum == 7):
                        spaceNum = 2
                        print("You move back over towards the coat hangers")
                elif(spaceNum == 5):
                        spaceNum = 7
                        print("You moved down")
                elif(spaceNum == 6):
                        spaceNum = 5
                        print("You move back beside the table")
                elif(spaceNum == 9):
                        spaceNum = 8
                        print("You moved over towards the toys")
                else:
                    print("You can't move this way")
                print()
            elif("inspect" in userInput.lower()):
                if(spaceNum == 1):
                        print("You are right beside the entrance to the house, but there is nothing to inspect")
                elif(spaceNum == 2):
                        print("You inspect the coat hangers. They look very old")
                elif(spaceNum == 3):
                        print("You look inside one of the boots and find a heart. You gained 1 Max Health")
                        maxhealth+=1
                elif(spaceNum == 4):
                        print("You look at the photo. It seems to be your mother. You start to wonder where she went, and how she dissapeared")
                        print("You father calls you for dinner")
                        print("LEVEL 2 CLEARED")
                        mapnum = 3
                        level = 3
                elif(spaceNum == 5):
                        print("You look at the table but there is nothing there")
                elif(spaceNum == 6):
                        print("Your father seems to have had a rough time sleeping last night")
                elif(spaceNum == 7):
                        print("There is nothing to inspect")
                elif(spaceNum == 8):
                        print("You start to play with your toys. You gained 1 Intelligence")
                        intelligence+=1
                elif(spaceNum == 9):
                        print("You try to sniff out what your father is making for dinner but you can't quite figure it out")
            elif("map" in userInput.lower()):
                drawMap(level)
                print("You are on space:",spaceNum)
            elif("check health" in userInput.lower()):
                print("Your current health is:",health)
                print()
            elif("check max health" in userInput.lower()):
                print("Your current max health is:",maxhealth)
                print()
            elif("check defense" in userInput.lower()):
                print("Your current defense level is:",defense)
                print("You have",armourType[armourTypeNum],"armour")
                print()
            elif("check confidence" in userInput.lower()):
                print("Your current confidence is:",confidence)
                print()
            elif("check intelligence" in userInput.lower()):
                print("Your current intelligence is:",intelligence)
                print()
            else:
                print("Invalid Response, please try again")
                print()
    if(level == 3):
        time.sleep(2)
        os.system('clear')
        print("You go to bed after dinner")
        time.sleep(2)
        print("You wake up to remember its the first day of school")
        time.sleep(2)
        print("You walk to school and enter your first class")
        time.sleep(2)
        print("You teacher leaves the classroom but she said that she will be back soon")
        print()
        print("Task: Explore the classroom")
        time.sleep(2)
        print()
        print("Type \"help\" for help on some commands you can use")
        spaceNum = 4
        while(level == 3):
            userInput = input()
            if("help map" in userInput.lower()):
                drawMap(3)
                print("This is the map of the current stage you are on. Here you can see a bunch of numbers and some decoration. Each number represents a location you can be at. Type \"map\" to see what number you are currently on!")
                print()
            elif("help check health" in userInput.lower()):
                print("This shows the current amount of health you currently have. You can increase this by finding a heart. A heart fills up your heath and increases your max health")
                print()
            elif("help check max health" in userInput.lower()):
                print("This shows the current amount of health you currently have. You can increase this by finding hearts in different stages. 1 Heart = 5 Health")
                print()
            elif("help check defense" in userInput.lower()):
                print("This shows the current amount of defense you currently have. You can increase defense by upgrading your armor")
                print()
            elif("help check confidence" in userInput.lower()):
                print("This is your confidence level. You can increase this by doing this that make your more confident activities e.g. jumping off the diving board. A lot of things rely on confidence in this game so make sure yours stays high.")
                print()
            elif("help check intelligence" in userInput.lower()):
                print("This is your intelligence level. You can increase this by doing this that make you smarter e.g. playing with toys. A lot of things rely on intelligence in this game so make sure yours stays high.")
                print()
            elif("help check inspect" in userInput.lower()):
                print("This command allows you to inspect things depending on which space your on. Each space has its own inspection area, so make sure to visit them all!")
            elif("help" in userInput.lower()):
                print()
                print("Here are some commands you can try. Type \"help command\" to get help with that specific command")
                time.sleep(2)
                print()
                print("map")
                print("move left")
                print("move right")
                print("move up")
                print("move down")
                print("check health")
                print("check max health")
                print("check defense")
                print("check confidence")
                print("check intelligence")
                print("inspect")
                print()
            elif("map" in userInput.lower()):
                drawMap(level)
                print("You are on space:",spaceNum)
            elif("move left" in userInput.lower()):
                if(spaceNum == 4):
                    spaceNum = 6
                    print("You move towards the exit of the classroom. You can probably slip out")
                elif(spaceNum == 5):
                    spaceNum == 7
                    print("You move towards an empty desk")
                elif(spaceNum == 7):
                    spaceNum == 8
                    print("You move towards another empty desk")
                elif(spaceNum == 3):
                    spaceNum = 1
                    print("You move towards yet another empty desk")
                elif(spaceNum == 1):
                    spaceNum = 2
                    print("You move right next to your teachers desk")
                else:
                    print("You can't move this way")
                print()
            elif("move right" in userInput.lower()):
                if(spaceNum == 2):
                    spaceNum = 1
                    print("You move back over towards an empty desk")
                elif(spaceNum == 1):
                    spaceNum = 3
                    print("You move towards a desk with somebody")
                elif(spaceNum == 8):
                    spaceNum = 7
                    print("You move back towards an empty desk")
                elif(spaceNum == 7):
                    spaceNum = 5
                    print("You move to a desk with a person sitting on it")
                elif(spaceNum == 6):
                    spaceNum = 4
                    print("You move back to your desk")
                else:
                    print("You can't move that way")
                print()
            elif("move up" in userInput.lower()):
                if(spaceNum == 2):
                    spaceNum = 6
                    print("You move towards the exit of the classroom. You can probably slip out")
                if(spaceNum == 1):
                    spaceNum = 8
                    print("You move towards an empty desk")
                if(spaceNum == 3):
                    spaceNum = 7
                    print("You move towards an empty desk")
                if(spaceNum == 8 or spaceNum == 7 or spaceNum == 5):
                    spaceNum = 4
                    print("You move back towards your own desk")
                else:
                    print("You can't move that way")
                print()
            elif("move down" in userInput.lower()):
                if(spaceNum == 6):
                    spaceNum = 2
                    print("You move back over towards the teachers desk")
                elif(spaceNum == 4):
                    spaceNum = 8
                    print("You move over towards an empty desk")
                elif(spaceNum == 8):
                    spaceNum = 1
                    print("You move over towards another empty desk")
                elif(spaceNum == 7 or spaceNum == 5):
                    spaceNum = 3
                    print("You move over towards a desk with somebody")
                else:
                    print("You can't move this way")
                print()
            elif("inspect" in userInput.lower()):
                if(spaceNum == 1):
                    print("There is nothing inside the desk")
                elif(spaceNum == 2):
                    print("You look inside your teachers desk and find a heart. You gained 1 Max Health")
                    maxhealth+=1
                elif(spaceNum == 3):
                    print("You get into a conversation with a boy named Nathan. Before you know it class is finished and you have a new friend. You gained 3 Confidence and 1 Intelligence")
                    confidence+=3
                    intelligence+=1
                    madeFriend = True
                    print("You gained 10 Intelligence for staying in class until the end of the day")
                    time.sleep(2)
                    print("LEVEL 3 CLEARED")
                    level = 4
                    mapnum = 4
                elif(spaceNum == 4):
                    print("This is your desk. There is nothing inside")
                elif(spaceNum == 5):
                    print("You attempt to look in another persons desk but they catch you trying to look")
                elif(spaceNum == 6):
                    print("You leave class but get caught by your teacher")
                    print("You lost half your intelligence and confidence")
                    intelligence/=2
                    confidence/=2
                    print("LEVEL 3 CLEARED")
                    level = 4
                    mapnum = 4
                elif(spaceNum == 7):
                    print("There is nothing inside this desk")
                elif(spaceNum == 8):
                    print("There is nothing inside this desk")
            elif("check health" in userInput.lower()):
                print("Your current health is:",health)
                print()
            elif("check max health" in userInput.lower()):
                print("Your current max health is:",maxhealth)
                print()
            elif("check defense" in userInput.lower()):
                print("Your current defense level is:",defense)
                print("You have",armourType[armourTypeNum],"armour")
                print()
            elif("check confidence" in userInput.lower()):
                print("Your current confidence is:",confidence)
                print()
            elif("check intelligence" in userInput.lower()):
                print("Your current intelligence is:",intelligence)
                print()
            else:
                print("Invalid Response, please try again")
                print()
    if(level == 4):
        time.sleep(2)
        os.system('clear')
        print("You come back to school the next day and are walking down the hallway to get to class")
        time.sleep(2)
        print()
        print("Task: Get to class")
        time.sleep(2)
        print()
        print("Type \"help\" for help on some commands you can use")
        spaceNum = 1
        while(level == 4):
            userInput = input()
            if("help map" in userInput.lower()):
                drawMap(3)
                print("This is the map of the current stage you are on. Here you can see a bunch of numbers and some decoration. Each number represents a location you can be at. Type \"map\" to see what number you are currently on!")
                print()
            elif("help check health" in userInput.lower()):
                print("This shows the current amount of health you currently have. You can increase this by finding a heart. A heart fills up your heath and increases your max health")
                print()
            elif("help check max health" in userInput.lower()):
                print("This shows the current amount of health you currently have. You can increase this by finding hearts in different stages. 1 Heart = 5 Health")
                print()
            elif("help check defense" in userInput.lower()):
                print("This shows the current amount of defense you currently have. You can increase defense by upgrading your armor")
                print()
            elif("help check confidence" in userInput.lower()):
                print("This is your confidence level. You can increase this by doing this that make your more confident activities e.g. jumping off the diving board. A lot of things rely on confidence in this game so make sure yours stays high.")
                print()
            elif("help check intelligence" in userInput.lower()):
                print("This is your intelligence level. You can increase this by doing this that make you smarter e.g. playing with toys. A lot of things rely on intelligence in this game so make sure yours stays high.")
                print()
            elif("help check inspect" in userInput.lower()):
                print("This command allows you to inspect things depending on which space your on. Each space has its own inspection area, so make sure to visit them all!")
            elif("help" in userInput.lower()):
                print()
                print("Here are some commands you can try. Type \"help command\" to get help with that specific command")
                time.sleep(2)
                print()
                print("map")
                print("move left")
                print("move right")
                print("move up")
                print("move down")
                print("check health")
                print("check max health")
                print("check defense")
                print("check confidence")
                print("check intelligence")
                print("inspect")
                print()
            elif("map" in userInput.lower()):
                drawMap(level)
                print("You are on space:",spaceNum)
            elif("move up" in userInput.lower() or "move down" in userInput.lower()):
                print("You can't move this way")
            elif("move left" in userInput.lower()):
                if(spaceNum == 1):
                    spaceNum = 2
                    print("You move down the hallway. You see a big person standing near the end")
                elif(spaceNum == 2):
                    spaceNum = 3
                    print("You now stand beside the big person")
                else:
                    print("You can't move this way")
                print()
            elif("move right" in userInput.lower()):
                if(spaceNum == 3):
                    spaceNum = 2
                    print("You move back down the hallway")
                elif(spaceNum == 2):
                    spaceNum = 1
                    print("You move back towards some lockers")
                else:
                    print("You can't move this way")
                print()
            elif("inspect" in userInput.lower()):
                if(spaceNum == 1):
                    print("You look in the lockers and find a heart. You gained 1 Max Health")
                    maxhealth+=1
                elif(spaceNum == 2):
                    print("There is nothing to inspect here")
                elif(spaceNum == 3):
                    print("The person challenges you to a fight. Do you accept?")
                    userInput = input()
                    if("yes" in userInput.lower()):
                        if(intelligence >= 15):
                            print("You beat the bully but then get reported on. You get in big trouble and lose half your confidence and half your intelligence")
                            intelligence/=2
                            confidence/=2
                            print("LEVEL 4 CLEARED")
                            level = 5
                        else:
                            print("You lose the fight and lose half your confidence and inteligence")
                            print("LEVEL 4 CLEARED")
                            level = 5
                    elif("no" in userInput.lower()):
                        print("You get a teacher and the teacher takes care of the situation. You gained 10 Intelligence and 3 Confidence")
                        intelligence+=10
                        confidence+=3
                        print("LEVEL 4 CLEARED")
                        level = 5
            elif("check health" in userInput.lower()):
                print("Your current health is:",health)
                print()
            elif("check max health" in userInput.lower()):
                print("Your current max health is:",maxhealth)
                print()
            elif("check defense" in userInput.lower()):
                print("Your current defense level is:",defense)
                print("You have",armourType[armourTypeNum],"armour")
                print()
            elif("check confidence" in userInput.lower()):
                print("Your current confidence is:",confidence)
                print()
            elif("check intelligence" in userInput.lower()):
                print("Your current intelligence is:",intelligence)
                print()
            else:
                print("Invalid Response, please try again")
                print()
    if(level == 5):
        os.system('clear')
        print("You walk home from school and see a huge cave on the way")
        time.sleep(2)
        print("You take a look at the cave and accidentaly fall in")
        if(madeFriend == True):
            print("Lucky for you, you're not alone. You friend Nathan is with you")
        time.sleep(2)
        print("When you fall down the cave, you take 2 Hearts of damage")
        time.sleep(2)
        health-=2
        print("Without the leather shirt, you would be dead")
        print()
        print("Task: Explore the cave")
        time.sleep(2)
        print()
        print("Type \"help\" for help on some commands you can use")
        spaceNum = 1
        while(level == 5):
            userInput = input()
            if("help map" in userInput.lower()):
                drawMap(3)
                print("This is the map of the current stage you are on. Here you can see a bunch of numbers and some decoration. Each number represents a location you can be at. Type \"map\" to see what number you are currently on!")
                print()
            elif("help check health" in userInput.lower()):
                print("This shows the current amount of health you currently have. You can increase this by finding a heart. A heart fills up your heath and increases your max health")
                print()
            elif("help check max health" in userInput.lower()):
                print("This shows the current amount of health you currently have. You can increase this by finding hearts in different stages. 1 Heart = 5 Health")
                print()
            elif("help check defense" in userInput.lower()):
                print("This shows the current amount of defense you currently have. You can increase defense by upgrading your armor")
                print()
            elif("help check confidence" in userInput.lower()):
                print("This is your confidence level. You can increase this by doing this that make your more confident activities e.g. jumping off the diving board. A lot of things rely on confidence in this game so make sure yours stays high.")
                print()
            elif("help check intelligence" in userInput.lower()):
                print("This is your intelligence level. You can increase this by doing this that make you smarter e.g. playing with toys. A lot of things rely on intelligence in this game so make sure yours stays high.")
                print()
            elif("help check inspect" in userInput.lower()):
                print("This command allows you to inspect things depending on which space your on. Each space has its own inspection area, so make sure to visit them all!")
            elif("help" in userInput.lower()):
                print()
                print("Here are some commands you can try. Type \"help command\" to get help with that specific command")
                time.sleep(2)
                print()
                print("map")
                print("move left")
                print("move right")
                print("move up")
                print("move down")
                print("check health")
                print("check max health")
                print("check defense")
                print("check confidence")
                print("check intelligence")
                print("inspect")
                print()
            elif("map" in userInput.lower()):
                drawMap(level)
                print("You are on space:",spaceNum)
            elif("move down" in userInput.lower()):
                if(spaceNum == 1):
                    spaceNum = 2
                    print("You moved down")
                elif(spaceNum == 6):
                    spaceNum = 8
                    if(padcovered == False):
                        print("You get off of the pad and move towards the gate. As you get off, the gate closes")
                    else:
                        print("You move down towards the open gate")
                elif(spaceNum == 8 and padcovered == True):
                    spaceNum = 9
                    if(madeFriend == True):
                        print("You go through the gate but just as you do, Nathan accidentaly falls of the pad and you get squished. You took 0.5 Damage")
                        health-=0.5
                    else:
                        print("The rock you moved starts rolling off of the pad. The gate squishes you for 0.5 Damage")
                        health-=0.5
                elif(spaceNum == 8 and padcovered == False):
                    print("The gate is closed")
                else:
                    print("You can't move this way")
                print()
            elif("move right" in userInput.lower()):
                if(spaceNum == 2):
                    spaceNum = 3
                    print("You moved right")
                elif(spaceNum == 1):
                    spaceNum = 2
                    print("You moved right")
                elif(spaceNum == 3):
                    spaceNum = 4
                    print("You moved right")
                elif(spaceNum == 4):
                    spaceNum = 5
                    print("You moved right beside a gate")
                elif(spaceNum == 5 and secondkeyfound == True):
                    print("You move through the gate")
                    spaceNum = 8
                elif(secondkeyfound == False and spaceNum == 5):
                    print("Find the key")
                elif(spaceNum == 9):
                    spaceNum = 10
                    print("You move to behind a mirror")
                elif(spaceNum == 11):
                    spaceNum = 9
                    print("You moved right")
                else:
                    print("You can't move this way")
                print()
            elif("move up" in userInput.lower()):
                if(spaceNum == 8):
                    spaceNum = 6
                    print("You move onto a stone pad. The gate in front of you opens")
                elif(spaceNum == 9):
                    spaceNum = 8
                    print("You move back through the gate")
                else:
                    print("You can't move this way")
                print()
            elif("move left" in userInput.lower()):
                if(spaceNum == 2):
                    spaceNum = 1
                    print("You move back towards where you fell in")
                elif(spaceNum == 3):
                    spaceNum = 2
                    print("You moved left")
                elif(spaceNum == 4):
                    spaceNum = 3
                    print("You moved left")
                elif(spaceNum == 5):
                    spaceNum = 4
                    print("You moved left")
                elif(spaceNum == 8):
                    spaceNum = 5
                    print("You move back through the gate")
                elif(spaceNum == 6):
                    spaceNum = 5
                    print("You move back through the gate")
                elif(spaceNum == 10):
                    spaceNum = 9
                    print("You moved left")
                elif(spaceNum == 9):
                    spaceNum = 11
                    print("You moved left")
                elif(spaceNum == 11):
                    if(thirdkeyfound == True):
                        spaceNum = 12
                        print("You move through a series of walls")
                    else:
                        print("Find the key")
                elif(spaceNum == 12):
                    spaceNum = 13
                    print("You continue to move left")
                elif(spaceNum == 13):
                    spaceNum = 14
                    print("You continue to move left")
                elif(spaceNum == 14):
                    spaceNum = 15
                    print("You continue to move left")
                elif(spaceNum == 15):
                    spaceNum = 16
                    print("You continue to move left")
                elif(spaceNum == 16):
                    spaceNum = 17
                    print("You get past all of the walls, then you spot a familiar person in the corner crying")
                else:
                    print("You can't move this way")
                print()
            elif("inspect" in userInput.lower()):
                if(spaceNum == 1):
                    print("You can see the place where you fell in, way above your head")
                elif(spaceNum == 2):
                    print("There is nothing behind this rock")
                elif(spaceNum == 3):
                    print("You found a key behind this rock")
                    secondkeyfound = True
                elif(spaceNum == 4):
                    print("There is nothing behind this rock")
                elif(spaceNum == 5):
                    print("Its a gate that requires a key")
                elif(spaceNum == 6):
                    if(madeFriend == True):
                        print("You tell Nathan to stand on the pad while you make a run for the gate")
                        padcovered = True
                    else:
                        print("You push a rock onto the pad, the gate opens")
                        padcovered = True
                elif(spaceNum == 8):
                    print("Its a gate!")
                elif(spaceNum == 9):
                    print("There is nothing to inspect here")
                elif(spaceNum == 10):
                    print("You find another key behind the mirror")
                    thirdkeyfound = True
                elif(spaceNum == 11):
                    print("How shocking, its a gate!")
                elif(spaceNum == 17):
                    print("You stare at the figure in the corner, she stares you back. Then she says your name")
                    print("Mom: Jabari is that really you")
                    print()
                    print("LEVEL 5 CLEARED")
                    print()
                    print("THE END, thanks for playing")
                    level = 6
                else:
                    print("There is nothing to inspect here")
            elif("check health" in userInput.lower()):
                print("Your current health is:",health)
                print()
            elif("check max health" in userInput.lower()):
                print("Your current max health is:",maxhealth)
                print()
            elif("check defense" in userInput.lower()):
                print("Your current defense level is:",defense)
                print("You have",armourType[armourTypeNum],"armour")
                print()
            elif("check confidence" in userInput.lower()):
                print("Your current confidence is:",confidence)
                print()
            elif("check intelligence" in userInput.lower()):
                print("Your current intelligence is:",intelligence)
                print()
            else:
                print("Invalid Response, please try again")
                print()