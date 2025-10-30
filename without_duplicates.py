# project-5b

# Author: Gabriel Venegas
# GitHub username: GVenegas1
# Date: 10/29/2025
# Description: Using the function 'without_duplicates', it takes a list
#and returns a new list with the same values but removing any duplicates

def without_duplicates(items):
    """Returns a new list of values as the input list but with out
        any duplication. """

    #create an empty list to store values
    new_list = []
    #loop through each item in the original list
    for item in items:
        #check if item is in new_list
        if item not in new_list:
            #add item if it's not already in new_list
            new_list.append(item)
    #after the loop, returns the list without duplicates
    return new_list

#example used
#my_list = [1, 2.0, 2, 3.5, 1.0]
#result = without_duplicates(my_list)
#print("Original list:", my_list)
#print("List without duplicates:", result)


