# Have a word/phrase
phrase = "girls who code"
guess = input("Enter a letter: ")
game_over = False
# Keep track of user's guesses
guessed_letters = []


#tell user how many spaces and letters they need to guess
display = ""
for letter in phrase:
    if letter in guessed_letters:
        display += letter
    elif letter == " ":
        display += "  "
    #the letter in our phrase has not been guessed yet
    else:
        display +="_ "
print(display)
# Allow user to give input to computer
guess = input("Enter a letter: ")
#Tell the user if they get the right letter

#Tell the user if they got the wrong letters
    #add the bad letter to our bad letter list
while game_over != True:
    if guess in phrase:
        print("You got a letter: {}".format(guess))
    else:
        print ("{} is not in the phrase.".format(guess))
    guessed_letters.append(guess)

    display = ""
    for letter in phrase:
        if letter in guessed_letters:
            display += letter
        elif letter == " ":
            display += "  "
        #the letter in our phrase has not been guessed yet
        else:
            display +="_ "
    print(display)

    if "_" in display:
        game_over = False
    else:
        game_over = True

print("END OF GAME")
# End the game if the user gets all the right letters in our word/phrase
