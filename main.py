from Greedy import greedy
from Brute import brute

import matplotlib.pyplot as plt
import timeit
import numpy as  np

#creates one single array of elements from which later smaller parts are used in the test
def get_numbers(amount= 100,low= 1 , high= 100):
    array = []
    for i in range(amount):
        array.append([np.random.randint(low , high),np.random.randint(low , high)])
    return array

# tests both algorithms fo the same items
def show_outcomes(max_size, arrays):
    print("===============================")
    print("Greedy")
    print(greedy(max_size, arrays))
    print("Brute")
    print(brute(max_size, arrays))
    print("===============================")

#used for taking a smaller array of the big array for the tests
def get_sub_array(amount, array=[]):
    sub_array = []
    for i in array:
        sub_array.append(i)
        amount = amount -1
        if amount == 0:
            return sub_array


#function for drawing a graph
def draw_graph(times, amount, title, color = "blue"):
    y = times
    x = amount
    plt.plot(x, y, color)
    plt.ylabel("Time[s]")
    plt.xlabel("Amount of words")
    plt.title(title)
    plt.show
    plt.savefig(title + ".png")
    plt.close()

#function for creating a .txt file with the measurments
def create_file(times, amounts,sort_type, file_name = "results"):
    full_name = file_name + ".txt"
    indexes = len(times)
    with open(full_name, 'a+') as file:
        file.write(sort_type + '\n')
        for  index in range(0,indexes):
            current_amount = amounts[index] 
            current_time  = times[index]
            line = "Numbers given:" + str(current_amount) + '\t' + "Time:" + str(current_time) + '\n'
            file.write(line)

#Shows the time results of both algorithms, draws graphs and saves the reults in a .txt file
def create_results(algorithm, name_of_algorithm = ' ',words_bank = [], max = 400, increment = 20 ):
    amount= 0
    times =[]
    words = []
    print(name_of_algorithm)
    while amount < max:
        amount = amount + increment
        collection = get_sub_array(amount, words_bank)
        time = (timeit.timeit(lambda:algorithm(20, collection ), number = 20)/20) #average executing time of adding new elements
        rounded = round(time, 4)
        times.append(rounded)
        words.append(amount)
        print('Amount of numbers:',amount, ' Rounded_time(s):', rounded)
    print("\n ------------- \n")
    #These functions are used for creating the graph and adding the data to the .txt file
    #draw_graph(times, words, name_of_algorithm)
    #create_file(times, words, name_of_algorithm)
    return words, times , algorithm


# A set of tests with various  items possibilities and maximal weights

# Checks and shows the outcomes of both algorithms to comparison. ( [iteration number], biggest sum,[items held in the backpack]).
items_1 = [[16,8], [8,3], [9,5],[6,2]]
items_2 = [[25,8], [1,1], [100,10], [6,2], [1,3], [13,5], [8,6], [9,15], [6,12], [1,11]]

show_outcomes(5,items_1)
show_outcomes(10,items_1)
show_outcomes(20,items_1)
show_outcomes(5,items_2)
show_outcomes(10,items_2)
show_outcomes(20,items_2)


# Make a pregenerated array of items with values and weights.
collection = get_numbers(1000)
#Create a bank of numbers and taking every time bigger amounts from it note the times.

create_results(greedy,'GREEDY',collection)
create_results(brute,'BRUTE', collection)
