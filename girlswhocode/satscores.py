import school_scores
list_of_record = school_scores.get_all()

#print(list_of_record)

for item in list_of_record:
    print(item["GPA"]["B"]["Verbal"])
