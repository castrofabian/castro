import statistics
import sys
print("""

**Guess **That **number**
guess a number between 1 and 100

""")
playAmount = 0
nom_of_tries = 0
number = int(100)
guess_nuber = int(40)


game_data = []


def solu_tion(high_score):
    if playAmount > 3:
        
        me_dian2 = statistics.median(high_score)
        me_an2 = statistics.mean(high_score)
        
        print ('Your mean is {}'.format(me_an2))
        print ('Your median is {}'.format(me_dian2))
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
            game_data.append(guess)
            nom_of_tries += 1
            print('Try again')

        elif guess == guess_nuber:
            print ('number of tries {}'.format(nom_of_tries))
            new_cop = game_data.copy()

            #call solution
            solu_tion(new_cop)

            #mean, median, mode 
            t = game_data.copy()
            me_an = statistics.mean(t)
            me_dian = statistics.median(t)
            
            #get mean median and mode of high score
            

            playyy = str(input(" 'y' to keep playing 'x' to exit >>"))

            if playyy == "x":
                sys.exit()
            elif playyy == "y":
                playAmount += 1
                continue
                
            

    
             
            
            
            

            
        



