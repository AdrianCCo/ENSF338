import sys

sys.setrecursionlimit(20000)

test = [8, 42, 25, 3, 3, 2, 27, 3]

new_arr = [0] * len(test)
counter = 0

def merge_sort(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)
        merge(arr, low, mid, high)



def merge(arr, left_start, mid, top_boundary):

    right_start = mid + 1
    left_index = left_start
    right_index = right_start
    general_index = left_start

    #Check if general index is greater than the highest possible sub-array index
    while(general_index <= top_boundary):

        #Check if value in the left index of arr is greating right_index of arr
        #If so then place the value of the left index in into the general index
        if (arr[left_index] <= arr[right_index]):
            new_arr[general_index] = arr[left_index]
            left_index += 1 

        #If the right index of arr is greater than the left index, then the value
        #placed in the new_arr will be the right index in the new_arr in the general index
        else:
            new_arr[general_index] = arr[right_index]
            right_index += 1 

        general_index += 1  

        #If the left sub array has reached the start of the right sub array
        #then start filling the rest of new_arr indexes with the right_sub array values
        #starting from the right_index of the given array
        if(left_index >= right_start): 
            while(right_index <= top_boundary):
                new_arr[general_index] = arr[right_index]
                general_index += 1
                right_index += 1   

        #If the right sub array has surpassed the highest possible sub array index
        #then start filling the new array with the left sub array values starting from
        #the left index of the given array
        if(right_index > top_boundary):  
            while(left_index < right_start):
                new_arr[general_index] = arr[left_index]
                general_index += 1
                left_index += 1

    #Insert the new changes into the original array
    while(left_start <= top_boundary):
         arr[left_start] = new_arr[left_start]
         left_start += 1


merge_sort(test, 0, len(test) - 1)
print(test)




    
    