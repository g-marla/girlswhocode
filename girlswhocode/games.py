#TODO: import the random module since you  will need it in your game functions
import random

#TODO: define function guess_the_num
def guess_the_num():
    game_over = False
    answer = random.randint(1, 20)
    print(answer)
    guess = int(input("Guess a number between 1 and 20: "))
    while game_over != True:
        if guess != answer:
            guess = int(input("Try again: "))
        elif guess == answer:
            print("Great job! You guessed correctly.")
            game_over = True

def evenorodd():
    computer_value = random.randint(1,10)
    print("{}".format(computer_value))
    user_input = input("Is this numver even or odd? ")
    if ((computer_value%2) == 0) and (user_input == "even"):
        print("YA DID IT! YOU SO SMORT\n")
    elif ((computer_value%2) != 0) and (user_input == "odd"):
            print("YA DID IT! YOU SO SMORT\n")
    else:
        print("You're wrong.")

guess_the_num() 


#TODO: use random.randint to get a number between 1 and 20

#TODO: ask user to input their guess

    #TODO: loop to keep giving the player three guesses until they've guessed correctly

        #TODO: give the player cues if the guess is not correct

    #TODO: let the player know if the guess is correct

#TODO: define function rock_paper_scissors
#def rock_paper_scissors():

#TODO: define function madlibs
#def madlibs():

#TODO: define function riddle
#def riddle():
