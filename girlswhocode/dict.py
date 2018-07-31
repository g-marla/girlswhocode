# Write a function that would print a given dict in sorted order
#def pretty_print_dict(dictionary):
    #for key, value in sorted(dictionary.items()) :
        #print(key, value)

# Key = student name; value = disney character
#students = {
#"Annamarie" : "Baymax",
#"Adriana" : "Rapunzel",
#"Sydney" : "Ariel",
#"Lisette" : "Mulan",
#}
#pretty_print_dict(students)

#def translate_shorthand(dictionary):
#    for key, value in lexicon.items():
#        print (key, value)

#lexicon = {
#"imo" : "in my opinion",
#"aitr" : "adult in the room",
#"gwcsip" : "girls who code summer immersion program",
#"bfflmnw" : "best friends for life no matter what",
#}

#translate_shorthand(lexicon)

#story = """
#Stacy was texting her friend. She said lol noobs suck smh. imo wow is better.
#are you going to gwcsip?
#"""

#story_list = story.split()
#print(story_list)
#new_story_list = []
# Go through each word of our story
#for word in story_list:
    #the word is a shorthadn
#    if word in lexicon.keys():
#        new_story_list.append(lexicon[word])
#    #The word is NOT a shortand
#    else:
#        new_story_list.append(word)
#print(new_story_list)
#print(" ".join(new_story_list))


def letter_frequency(word):
    frequency = {} # dictionary holds count of each letter

    for char in word:
        if char in frequency.keys():
            frequency[char] = frequency[char] + 1
        else:
            frequency[char] = 1
    print(frequency)

letter_frequency("pen pineapple apple pen")
