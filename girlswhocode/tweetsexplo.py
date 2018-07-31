import json


file = open("tweets.json", "r")
data = json.load(file) #load file onto json object

for d in data: #data is a list, d is dictionary
    #for info_category, info in d.items():
        #print(info_category, info)
    #d is our dictionary about our tweet

    #for user_mention in d["user_mentions"]:
        #print(user_mention["screen_name"])

    print(d["retweet_count"])

    break
