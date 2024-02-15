

def merge_sort(unsort_list):
    if(unsort_list) == 1:
        return unsort_list
    
    mid_point =int(len(unsort_list)/2)
    first_half=unsort_list[:mid_point]
    second_half=unsort_list[mid_point:]
    
    half_a=merge_sort(first_half)
    half_b = merge_sort(second_half)
    
    return merge(half_a, half_b)

def merge(first_sublist, second_sublist):
    i = j=0 
    merged_list =[]
    while i < len(first_sublit) and j <len(second_sublist):
        if first_sublit[i] < second_sublist[j]:
            merged_list.append(first_sublist[i])
            # This code is not complete yet 

    
