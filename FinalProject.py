import random
import time
import sys

#Basic player information and item information
player_username = input("Please Type in Username to Start Your Text-based Adventure! >>> ")
player_health = 8
player_backpack = ' '
bat_clb_dmg = ' '
Club = 7
Large_sword = 14
black_pills = 40

#Definitions used for the rest of the game
def add_itm(x):
        print(" << Added " + (x) + " to Your Backpack >> ")

def whitespace(amount_of_times):
        for x in range(amount_of_times):
                print(" \n")

def attack_damage_callout(itm, damage):
        print("Your " + str(itm) + "'s damage = " + str(damage))

def death():
        print(" <<<  Restart the game to try and get a different ending. >>>")

def normalspace():
        time.sleep(.8)
        whitespace(1)


#Start of beginning
print(
        "=================== The Tale Of " + str(player_username) + " ==================="

)

normalspace()

print(" <<< Hint, use two word commands that are not complicated, and lowercase only. >>> ")

whitespace(4)
time.sleep(.8)

print(
        "You are facing the opposite side of a large metal treasure chest-esque box, you cannot see the contents."

)

#End of beginning
print(
        "Press 1 to open the chest."
        
)

player_input = input(">>>")
whitespace(1)

#Opened chest
if player_input == "1": 
        print("You move to the opposite side of the room, where the chest faces towards you.")
    
        normalspace()
    
        print(
                "You Found a Battered Club inside of the Chest, it seems to have remnants of \n intricate wood carving designs, that are now weared out and smoothed."

)
    
#Adding battered club to item list
player_backpack += "Battered Club"


normalspace()
add_itm("Battered Club")


normalspace()
attack_damage_callout(" Battered Club ", Club)
normalspace()



#surrounding check
print(
        "Looking up from the chest in front of you, you can see the large wooden door at \n 12 o'clock, and three windows on either side of you."
)
normalspace()

#Options
print("Press 1 or to go through the door, and 2 to inspect the window.")
player_input2 = input(">>>")

#Went through door beginning
if player_input2 == "1":
        print(
                "The door is very heavy and scrapes across the stone floor, and pushes outwards to \n reveal a hallway, dimly lit by candles."

)
        normalspace()
                
#Options for door
        print(
                "Press 1 to pick up candle, and press 2 to walk down the stone hallway"

)
        player_input3 = input(">>>")
                
#Picked up candle
        if player_input3 == "1":
                print(
                        "You picked up the candle, it won't be very good for fighting, but it lights the way down the hallway"

)
                normalspace()
                add_itm(" Candle ")
                normalspace()
                candle = True
                        
#Didn't pick up candle
        elif player_input3 == "2":
                print("You continue down the dark hallway.")
                candle = False

                normalspace()

        print(
                "When you get down the hallway, you see a very dark stairway to your right, a turn to your \n left, and a door directly in front of you"

)
        normalspace()
        
#Has Candle Hallway Options
        if candle == True:
                print("Press 1 to go through the stairway, 2 to take a left, and 3 to open door")
                        
                
#No candle Hallway Options
        elif candle == False:
                print("Press 2 to take a left, and 3 to open door")

        normalspace()
        player_input4 = input(">>>")
        normalspace()
                

                                
        def hallway_end_options():
                        
        #Option 2
                if player_input4 == "2":
                        print(
                                "You take a left and are meeted with another door, you open it and see a large \n table with a sign reading 'Take one'. On the table there is a large sword and a small blue pouch."
                                
)
                        normalspace()
                        print("Press 1 to take the large sword, 2 to take the small blue pouch, and 3 to take both")

                        player_input_5a = input(">>>")
                        
                        if player_input_5a == "1":
                                print("You take the large sword and leave the small blue pouch on the table, \n obeying the sign.")


                                player_backpack += "Large Sword"


                                normalspace()
                                add_itm(" Large Sword ")


                                normalspace()
                                attack_damage_callout("Large Sword", Large_sword)
                                normalspace()
                                print("Items in backpack: " + player_backpack)

                                normalspace()
                                
                        elif player_input_5a == "2":
                                print("You take the small blue pouch and open the contents, there are 3 small black \n tablets in the pouch that are vaguely mecidine esque.")

                                normalspace()

                                print("press 1 to take the pills")

                                player_input6 = input(">>>")
                                
                                if player_input6 == "1":
                                      print("You take the pills and feel a strange sensation go through your body, as if \n you are much stronger than before.")

                                      normalspace()
                                      add_itm(" Black Pills ")
                                      black_pillpower = True


                                      normalspace()
                                      attack_damage_callout("Black Pills", black_pills)
                                      normalspace()

                        elif player_input_5a == "3":
                                print("You swipe both of the objects on the table, but before you can celebrate your rule-breaking, \n the wall on the left of you springs forward, and you are squished to death.")
                                normalspace()
                                print (
                                        "======= Congratulations! You are a theif and didn't follow the clear rules. ========"

        )
                                normalspace()
                                death()
                                sys.exit()

                                

                                      

                        print("There is a door on the other side of the room, and you go through the door.")

                        normalspace()

                        print("On the other side of the door, you spot a giant, three-headed walrus that looks menacingly \n at you. ")

                        normalspace()
                        print("You try to sprint back to the door, but it is now just a stone wall, undisturbed by any doorway \n that may have been there.")

                        normalspace()
                        normalspace()

                        print("The walrus lunges, and you have seconds before all six of it's gigantic tusks impale you.")

                        if black_pillpower == True:
                              print(
                                      "You use your incredible strength from the special black pills taken and bruteforce shove \n the walrus back on its own attack, smashing its blubbery body into the other side of the room with a sickening \n *thunk*."

)
                              normalspace()
                              print("The walrus is dead, and you have defeated the castle's only inhabitant.")

                              normalspace()
                              normalspace()

                              print (
                        "======= Congratulations! You have defeated the final boss and have won the game! ========"

)
                              normalspace()
                              death()
                              sys.exit()

                        else:
                              print("You try to use your sword against the walrus, but the giant amount of blubber that rushes \n towards you breaks the blade and kills you.")

                              print (
                        "======= Congratulations! You have been defeated by the final boss. ========"

)
                              normalspace()
                              death()
                              sys.exit()

                              

                                
        #Option 3
                elif player_input4 == "3":
                        print(
                                "Opening the door allows you to make out a low growl directly ahead of you, \n then a pair of bright yellow eyes blink into existence out of the open door. A giant tiger pounces \n on you and makes "  + player_username + " his lunch."

)                        
                        print (
                        "======= Congratulations! You were eaten by a hungry tiger and are now digesting in it's stomach. ========"

)
                normalspace()
                death()
                sys.exit()




#Options for candle
        if candle == True:
                if player_input4 == "1":
                        print(
                                "You go up the stairway with the candle lighting you way, and find a open door \n at the top of the stairwell."

)
                        print("Press one to go through the door")

                        player_input5 = input(">>>")

                        if player_input5 == "1":
                                print(
                                        "Going through the door reveals a large helicopter that is unlocked. You \n strangely know how to perfectly fly a helicopter, and fly it out of the building, which looks \n like a castle from the helicopter. You return to civilization."

)



                                print (
                                        "======= Congratulations! You escaped the castle and went back to society, this is one of the good endings. ========"

)
                                normalspace()
                                death()
                                sys.exit()

        
        hallway_end_options()                           

                                
                        
#Went through window beginning               
elif player_input == "2":
        normalspace()
        print( "The windows are dirty and are hard to see out of.")


        normalspace()
        print("Press 1 to open the window.")

        player_input = input(">>>")
                
#Death number 1 (Window)
if player_input == "1":
        normalspace()
        print("You push the window and AHHHHHHHH!")
        time.sleep(2)

        whitespace(3)

        print (
                "======= Congratulations! You fell to your death by pushing the window too hard and falling in. ========"

)
        normalspace()
        death()
        sys.exit()
