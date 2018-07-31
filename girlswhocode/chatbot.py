# --- Define your functions below! ---
def intro():
    print("Welcome! My name is Tajin.")

def greeting():
    print("Nice weather we're having.")

def dating():
    print("I work as a lyricist for DJ Kass and do money origami in my free time.")
    print("I'm a catch.")
    rep = input("So, come here often?")
    print("I'll get the milk bags.")
def is_valid_input(response, all_valid_inputs):
    valid_input = ["Hi","<3", "looking good", ";)", "ribbit", "Hello", "What's up","Forecast?","Peace of wisdom?" "Kiss?"]
    if response in all_valid_inputs:
        return True
    else:
        return False
def ribbit():
    print("""                 -----.
                            /7  .  (
                           /   .-.  \
                          /   /   \  \
                         / `  )   (   )
                        / `   )   ).  \
                      .'  _.   \_/  . |
     .--.           .' _.' )`.        |
    (    `---...._.'   `---.'_)    ..  \
     \            `----....___    `. \  |
      `.           _ ----- _   `._  )/  |
        `.       /"  \   /"  \`.  `._   |
          `.    ((O)` ) ((O)` ) `.   `._\
            `-- '`---'   `---' )  `.    `-.
               /                  ` \      `-.
             .'                      `.       `.
            /                     `  ` `.       `-.
     .--.   \ ===._____.======. `    `   `. .___.--`     .''''.
    ' .` `-. `.                )`. `   ` ` \          .' . '  8)
   (8  .  ` `-.`.               ( .  ` `  .`\      .'  '    ' /
    \  `. `    `-.               ) ` .   ` ` \  .'   ' .  '  /
     \ ` `.  ` . \`.    .--.     |  ` ) `   .``/   '  // .  /
      `.  ``. .   \ \   .-- `.  (  ` /_   ` . / ' .  '/   .'
        `. ` \  `  \ \  '-.   `-'  .'  `-.  `   .  .'/  .'
          \ `.`.  ` \ \    ) /`._.`       `.  ` .  .'  /
    LGB    |  `.`. . \ \  (.'               `.   .'  .'
        __/  .. \ \ ` ) \                     \.' .. \__
 .-._.-'     '"  ) .-'   `.                   (  '"     `-._.--.
(_________.-====' / .' /\_)`--..__________..-- `====-. _________)""")

dating_prompt = ["<3", "looking good", ";)"]
# Put your main program below!

def main():
    valid_input = ["Hi","<3", "looking good", ";)", "ribbit",  "Hello", "Hey", "What's up","Forecast?","Peace of wisdom?", "Kiss?"]
    intro()
    while True:
        answer = input("Tell me something. ")
        if is_valid_input(answer, valid_input):
            if answer in ["Hi", "Hello", "What's up","Forecast?", "Hey"]:
                greeting()
            elif answer in dating_prompt:
                dating()
            elif answer in ["ribbit", "Peace of wisdom?", "Kiss?"]:
                ribbit()
        else:
            print("Yo no comprender.")
            print("These are the inputs I understand: ")
            for vi in valid_input:
                print (vi)




# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
