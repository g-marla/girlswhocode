# Declare variables
myList = [2,3,1,3,5]   # Our inputs to the program
has_duplicates = False # initialize as false (why?)

# TODO: Sort 'myList' (Why do we sort first?)
myList.sort()

for index in range(len(myList)-1):
    if myList[index] == myList[index +1]:
        has_duplicates = True
# TODO: Loop through 'mylist' with a for-Loop

    # TODO: Check if adjacent elements of 'mylist' are the same

        # TODO: if they are the same, set has_duplicates to True

        # TODO: Exit out of the for-loop (no need to check rest of list)

print(has_duplicates) # Our outputs of the program
