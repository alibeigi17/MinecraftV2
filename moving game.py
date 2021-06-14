#set up game
import random

inventory =[]
username = input("type your name:")
print('hello ' + username + ' start your journey')

while(True):
    #moving
    answer = input("type in n,e,s,w or i:")
    if answer == 'w':
        print('\t' + username + ' moved west ')
    
    elif answer == 'e':
        print('\t' + username + ' moved east ')
    elif answer == 's':
        print ('\t' + username + ' moved south ')
    elif answer == 'n':
        print('\t' + username +  ' moved north ')
    elif answer == 'i':
        print(inventory)
    else:
        print('\t' + 'error')
    #good/bad things
    number = random.randint(1, 10)
     
    if number == 1:
        print('\t' + username + ' found a stick')
        inventory.append("stick")
    elif number == 9:
        print('\t' + username + ' found some gold')
        inventory.append("gold")
    elif number == 5:
        print('\t' + username + ' fell')
    elif number == 8:
        ('\t' + username + ' ran into a cactus')
    elif number == 7:
        print('\t' + username + ' found a sword')
        inventory.append("sword")
    elif number == 6:
        print('\t' + username + ' found some fish')
        inventory.append("fish")


        
        

     

