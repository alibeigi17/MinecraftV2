#set up game
import random

username = input("type your name:")
print('hello ' + username + ' start your journey')

while(True):
    #moving
    answer = input("type in n,e,s,w:")
    if answer == 'w':
        print('\t' + username + ' moved west ')
    
    elif answer == 'e':
        print('\t' + username + ' moved east ')
    elif answer == 's':
        print ('\t' + username + ' moved south ')
    elif answer == 'n':
        print('\t' + username +  ' moved north ')
    else:
        print('\t' + 'error')
    #good/bad things
    number = random.randint(1, 10)
     
    if number == 1:
        print('\t' + username + ' found a stick')
    elif number == 9:
        print('\t' + username + ' found some gold')
    elif number == 5:
        print('\t' + username + ' fell')
    elif number == 8:
        ('\t' + username + ' ran into a cactus')
    elif number == 7:
        print('\t' + username + ' found a sword')
    elif number == 6:
        print('\t' + username + ' found some fish')
#inventory
        
        

     

