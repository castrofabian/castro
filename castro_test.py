import statistics
import sys
import random

print("""

**Guess **That **number**
guess a number between 1 and 100

""")
playAmount = 0
nom_of_tries = 0
number = int(100)
guess_nuber = int(random.randrange(1, 100))



game_data = []

game_data2 = game_data.copy()




def solu_tion(high_score):

    me_dian2 = statistics.median(high_score )
    me_an2 = statistics.mean(high_score)
    modee = statistics.mode(high_score)
        
    print ('Your mean is {}'.format(me_an2))
    print("....................................")
    print("....................................")
    print ('Your median is {}'.format(me_dian2))
    print("....................................")
    print("....................................")
    print ('Your mode is {}'.format(modee))
    print("....................................")
    print("....................................")
    print(" Good job ")

    
    

    
while True:
    try:
        
        guess = int(input("enter your guess: "))
        
    except ValueError:
        print("Error: Invalid input, input a valid integer.")
        continue

    else:
        #check if "guess" is less than or == 100
        if guess not in range(int(100)):
            print("guess a number between 1 and 100")
            continue
            

        elif guess != guess_nuber:
            # tell user whether to go highrt or lower 
            if guess_nuber >  guess:
                print("<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>")
                print("Aim higher")
                print("<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>")
            elif guess_nuber < guess:
                print("/n <<<<<<<<<<<<<<<>>>>>>>>>>>>>>>")
                print("Aim Lower")
                print("/n <<<<<<<<<<<<<<<>>>>>>>>>>>>>>>")

            #game_data.append(guess)
            nom_of_tries =  nom_of_tries + 1
            print('Try again')

        elif guess == guess_nuber:
            nom_of_tries =  nom_of_tries + 1
            print ('number of tries {}'.format(nom_of_tries))
            new_cop = game_data.copy()
            game_data.append(nom_of_tries)

            
            #get mean median and mode of high score
            

            playyy = str(input(" 'y' to keep playing 'x' to exit >>")).lower()

            if playyy == "x":
                print("<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>")
                print("number of tries {}".format(nom_of_tries))
                print("<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>")

                #print game data
                print('game data : {}'.format(game_data))
                print("/n <<<<<<<<<<<<<<<>>>>>>>>>>>>>>>")
                solu_tion(game_data)
                sys.exit()

            elif playyy == "y":
                print(" ..........................")
                print("nom of Atempts {}".format(nom_of_tries))
                nom_of_tries = 0
            
                print(" ..........................")
                playAmount += 1
                guess_nuber = int(random.randrange(1, 100))

                continue
                
            

    
             
            
            
            

            
        



