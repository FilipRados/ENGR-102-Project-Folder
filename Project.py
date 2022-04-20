#Kill program
import sys
#Random number generator
import random
#Pause program
import time

def shop():
    #Visual
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("------------------------------------------------------------")

    #Determine player stat values
    player_file=open("player_stats_original.txt","r")
    player_stats=player_file.read()
    player_stats_list=player_stats.split()
    for i in range(len(player_stats_list)):
        player_values=player_stats_list[i].split(':')
        if "Name" in player_values:
            player_name=player_values[1]
        elif "Health" in player_values:
            player_health=int(player_values[1])
            player_original_health=player_health
        elif "Attack" in player_values:
            player_attack=int(player_values[1])
        elif "Defense" in player_values:
            player_defense=int(player_values[1])
            player_original_defense=player_defense
        elif "Gold" in player_values:
            player_gold=int(player_values[1])
        elif "Exp" in player_values:
            player_exp=int(player_values[1])
        elif "Level" in player_values:
            player_level=int(player_values[1])
    player_file.close()   
    
    
    
    #Prompt
    print("Welcome to the shop...what would you like to purchase?")    
    
    #Determine items for sale
    shop_listings=0
    if player_level in [1,2,3]:
        #Open shop1 file and read data in this line
        shop_listings=1
    elif player_level in [4,5,6]:
        #Open shop2 file and read data in this line
        shop_listings=2
    
    #Display items for sale
    if shop_listings==1:
        print("first shop printed out as a list")
        print("0) Leave Shop")
    elif shop_listings==2:
        print("second shop printed out as a list")
        print("0) Leave Shop")
    
    
    #Input buy option
    player_buys=input("Please enter your option as an integer: ")
    
    #Check valid input
    while player_buys not in ['1','2']:
        print("That was not a valid input")
        player_buys=input("Please enter your option as an integer: ")

    #Not Done vvvv
    print("Remove gold on this line")
    print("Add item to player inventory")
    print("add value to stats")
    print("write to stats file with all values")
    
def fight(a):
    #Visual
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("------------------------------------------------------------")
    
    #Prompt
    print("An enemy has appeared!!!\n")
    
    #Get enemy values
    fighter_stats=a.split('\n')
    for i in range(len(fighter_stats)):
        fighter_values=fighter_stats[i].split(':')
        if "Name" in fighter_values:
            enemy_name=fighter_values[1]
        elif "Health" in fighter_values:
            enemy_health=int(fighter_values[1])
        elif "Attack" in fighter_values:
            enemy_attack=int(fighter_values[1])
        elif "Defense" in fighter_values:
            enemy_defense=int(fighter_values[1])
        elif "Gold" in fighter_values:
            enemy_gold=int(fighter_values[1])
        elif "Exp" in fighter_values:
            enemy_exp=int(fighter_values[1])

    
    #Get player values
    player_file=open("player_stats.txt","r")
    player_stats=player_file.read()
    player_file.close()
    player_stats=player_stats.split('\n')
    for i in range(len(player_stats)):
        player_values=player_stats[i].split(':')
        if "Name" in player_values:
            player_name=player_values[1]
        elif "Health" in player_values:
            player_health=int(player_values[1])
            player_original_health=player_health
        elif "Attack" in player_values:
            player_attack=int(player_values[1])
        elif "Defense" in player_values:
            player_defense=int(player_values[1])
            player_original_defense=player_defense
        elif "Gold" in player_values:
            player_gold=int(player_values[1])
        elif "Exp" in player_values:
            player_exp=int(player_values[1])
        elif "Level" in player_values:
            player_level=int(player_values[1])

            
    #The fight
    time.sleep(2)
    fighting=True
    while fighting==True:
        #Visual
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("------------------------------------------------------------")
        
        #Display initial enemy health
        print(enemy_name+"\nHealth: {:.2f}".format(enemy_health))
        
        print("\n"+player_name+"\nHealth: {:.2f}".format(player_health))
        
        #Prompt the player with a choice
        print("\nIt is your turn...choose carefully")
        print("1) Attack\n2) Defend\n0) Run")
        action=input("Please enter your action as an integer: ")
        
        #Check input until valid
        while action not in ['1','2','0']:
            print("That was not a valid input")
            action=input("Please enter your action as an integer: ")
        
        #Possible actions
        if action=='1':
            damage=player_attack/enemy_defense
            enemy_health-=damage
            #Check for enemy death
            if enemy_health<=0:
                fighting=False
                enemy_health=0
        elif action=='2':
            damage=player_attack/(enemy_defense*1.5)
            enemy_health-=damage
            player_defense*=1.5
            #Check for enemy death
            if enemy_health<=0:
                fighting=False
                enemy_health=0
        elif action=='0':
            fighting=False
            main_menu()
        
        #Visual
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("------------------------------------------------------------")

        #Computer actions
        print("It is the enemies turn...")
        x=random.random()
        if 0.0<=x<=0.6:
            print("The enemy has attacked you!!!")
            time.sleep(2)
            damage=enemy_attack/player_defense
            player_health-=damage
            #Check for player death
            if player_health<=0:
                fighting=False
                player_health=0
        elif 0.6<x<=1.0:
            print("The enemy is focusing on defense...")
            time.sleep(2)
            damage=enemy_attack/(player_defense*1.5)
            player_health-=damage
            enemy_defense*=1.5
            #Check for player death
            if player_health<=0:
                fighting=False
                player_health=0
    
    #Visual
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("------------------------------------------------------------")
    
    #Outcome of both actions
    print(enemy_name+"\nHealth: {:.2f}".format(enemy_health))
    print("\n"+player_name+"\nHealth: {:.2f}".format(player_health))
        
    #Both fighters die
    if enemy_health==0 and player_health==0:
        print("\nBoth combatents have died")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("Your body was found and taken back to town...")
        time.sleep(2)
        print("A preist has revived you!!!")
        time.sleep(2)
        main_menu()
    
    #Only the player dies
    elif enemy_health!=0 and player_health==0:
        print("\nYou have died")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("The enemy has left the vicinity")
        time.sleep(1)
        print("Your body was found and taken back to town...")
        time.sleep(2)
        print("A preist has revived you!!!")
        time.sleep(2)
        main_menu()
    
    #Only the enemy dies
    elif enemy_health==0 and player_health!=0:
        print("\nThe enemy has been slayed")
        time.sleep(2)
        print("Go pick up your rewards...")
        
        #Add rewards
        player_exp+=enemy_exp
        player_gold+=enemy_gold
        
        #Write new player stats to player file
        player_file=open("player_stats.txt","w")
        player_stats="Name:"+player_name+"\n"+"Health:"+str(player_original_health)+"\n"+"Attack:"+str(player_attack)+"\n"+"Defense:"+str(player_original_defense)+"\n"+"Gold:"+str(player_gold)+"\n"+"Exp:"+str(player_exp)+"\n"+"Level:"+str(player_level)
        player_file.write(player_stats)
        player_file.close()
                
        time.sleep(3)
        main_menu()

def forest():
    x=random.random()
    if 0.0<=x<=0.8:
        goblin_normal=open("goblin_normal.txt","r")
        goblin_stats=goblin_normal.read()
        goblin_normal.close()
        fight(goblin_stats)
    elif 0.8<x<=1.0:
        goblin_rare=open("goblin_rare.txt","r")
        goblin_stats=goblin_rare.read()
        goblin_rare.close()
        fight(goblin_stats)      

def location():
    #Visual
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("------------------------------------------------------------")
    
    #Determine player level
    player_file=open("player_stats_original.txt","r")
    player_stats=player_file.read()
    player_stats_list=player_stats.split()
    for i in range(len(player_stats_list)):
        player_values=player_stats_list[i].split(':')
        if "Level" in player_values:
            player_level=int(player_values[1])
    player_file.close()   
    
    #Prompt open locations based on level
    if player_level in [1,2,3]:
        #Prompt and request location
        print("Choose any action from the list below")
        print("1) Town\n2) Forest")
        location=input("Please enter your action as an integer: ")
        
        #Check valid input
        while location not in ['1','2']:
            print("That was not a valid input")
            location=input("Please enter your action as an integer: ")
        
        #Possibilities    
        if location=='1':
            main_menu()
        elif location=='2':
            forest()
        
    elif player_level in [4,5,6]:
        print("Choose any action from the list below")
        print("1) Town\n2) Forest\n3) Desert")
        location=input("Please enter your action as an integer: ")
        
    elif player_level in [7,8,9]:
        print("Choose any action from the list below")
        print("1) Town\n2) Forest\n3) Desert\n4) Swamp")
        location=input("Please enter your action as an integer: ")
        
    elif player_level>=10:
        print("Choose any action from the list below")
        print("1) Town\n2) Forest\n3) Desert\n4) Swamp\n5) Ruins")
        location=input("Please enter your action as an integer: ")

def main_menu():
    #Visual
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("------------------------------------------------------------")
    
    #Menu
    print("Choose any action from the list below")
    print("1) Inventory\n2) Shop\n3) Location\n0) Exit Game (No Save Feature For Alpha.0.0.1...yet...i think i know how)")
    main_choice=input("Please enter your action as an integer: ")

    #Check input until valid
    while main_choice not in ['0','1','2','3']:
        print("That was not a valid input")
        main_choice=input("Please enter your action as an integer: ")

    #Possibilities    
    if main_choice=='1':
        print("hi")
    elif main_choice=='2':
        shop()
    elif main_choice=='3':
        location()
    elif main_choice=='0':
        sys.exit()

##############################################################################################################################################################################
#Visual
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("------------------------------------------------------------")

#Start Sequence
print("ENGR102-Project")
print("By: David Aleman, Colton Crain, Filip Rados, Phillip Reyes\n\n")
print("Evolution\nVersion: Alpha.0.0.1")
start=input("\nPlease press enter to start your adventure…")

#Open player file data
player_file=open("player_stats_original.txt","r")
player_stats=player_file.read()
player_file.close()

#Request name and add to the player file
char_name=input("Please enter your characters name: ")
player_file=open("player_stats.txt","w")
player_stats=player_stats.replace('x',char_name,1)
player_file.write(player_stats)
player_file.close()

#Open main menu
main_menu()




















