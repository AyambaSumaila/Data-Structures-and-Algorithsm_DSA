#Implement a linear search algorithm to search for an element and return 
# the index of the element if it is in the list 

#define a function called linear_search

def linear_search(my_arr, target):
    
    for i, j in enumerate(my_arr):
        if j == target:
            return i 
        
    return -1 


#Test it with sample 

arr=[12, 4, 14, 7, 17, 10]

target=7 

print("The position for the element x is : ", linear_search(arr, target))