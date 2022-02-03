
def divide_and_conquer(array, beginning, end, iteration_number):
    if end - beginning > 0:
        iteration_number[0] +=1
        pivot = array[end][2]
        small_index = beginning
        for numbers in range(beginning, end):
            if array[numbers][2] <= pivot:
                # switching elements
                temp = array[numbers]
                array[numbers] = array[small_index]
                array[small_index] = temp
                small_index = small_index + 1

        #switching  the pivot with the first element bigger than it
        temp = array[small_index]
        array[small_index] = array[end]
        array[end] = temp

        #now the left and right side of the pivot
        divide_and_conquer(array, beginning, small_index-1,iteration_number)
        divide_and_conquer(array, small_index+1, end,iteration_number)

# A quick implementation of quick sort
def sort_quick(array, iteration_number):
    last_index = len(array) -1
    divide_and_conquer(array, 0, last_index, iteration_number)

#Gives the value to weight ratio of every item
def give_value(array, iteration_number):
    new_array = []
    len_a = len(array) 
    for value in range(0,len_a):
        iteration_number[0] += 1
        new_array.append([array[value][0], array[value][1],array[value][0]/array[value][1]])
    return new_array

#Sums up all the items value
def sum(array):
    total = 0
    for item in range (0,len(array)):
        total += array[item][0]
    return total

# An implementation of the greedy algorithm
def greedy(max_weight, array):
    # iteration_count counts all the iterations that happened in the algorithm
    iteration_count = [0]
    with_value = give_value(array,iteration_count)
    sort_quick(with_value, iteration_count)
    last_element = len(with_value) 
    current_weight = 0
    backpack = []
    # Using a sorted list , take the most worth items untill the backpack is full
    for item in range(last_element-1, -1, -1):
        iteration_count[0] += 1
        if with_value[item][1] + current_weight <= max_weight:
            backpack.append(with_value[item])
            current_weight += with_value[item][1]
    return [iteration_count, sum(backpack),backpack]
