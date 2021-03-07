import random
import timeit
from timeit import default_timer as timer

print("\n\tFor each of the 3 sort methods:")
print("\t - generate 100 lists of 500 random positive integers")
print("\t - generate 100 lists of 1,000 random positive integers")
print("\t - generate 100 lists of 10,000 random positive integers")
print("\t\t... then run each sort method on each set of 100 lists (3 per sort method)")
print("\t\t... and figure out the average time to run each using the timeit module")
print("\n\tPLEASE BE PATIENT! RUNNING THE INSERTION SORT METHOD TAKES A LONG TIME!")

# INSERTION SORT - below works
def insertion_sort(a_list):
    for index in range(1,len(a_list)):
        position = a_list[index]
        j = index -1
        while j >= 0 and position < a_list[j]:
            a_list[j+1] = a_list[j]
            j -= 1
        a_list[j+1] = position

# Below from the text doesn't seem to work!
#def insertion_sort(a_list):
#   for index in range(1, len(a_list)):
#        current_value = a_list[index]
#        position = index

#        while position > 0 and a_list[position - 1] > current_value:
#            a_list[position] = a_list[position - 1]
#            position = position - 1

#        a_list[position] = current_value

# 100 lists of 500 positive integers
result500 = []

for x in range(1, 100):
    randomlist = []
    randomlist = random.sample(range(1, 501), 500)
    start = timer()
    insertion_sort(randomlist)
    end = timer()
    result500.append(end - start)

average500 = sum(result500) / len(result500)
print("\nInsertion Sort on a random list of 500 positive integers took" , "%10.7f" % (average500) , ", on average over 100 lists")

# 100 lists of 1,000 positive integers
result1000 = []

for x in range(1, 100):
    randomlist = []
    randomlist = random.sample(range(1, 1001), 1000)
    start = timer()
    insertion_sort(randomlist)
    end = timer()
    result1000.append(end - start)

average1000 = sum(result1000) / len(result1000)
print("Insertion Sort on a random list of 1,000 positive integers took" , "%10.7f" % (average1000) , ", on average over 100 lists")

# 100 lists of 10,000 positive integers
result10000 = []

#for x in range(1, 100): # Processing 100 lists of 10,000 random integers using insertion sort takes around 23 minutes!
# for x in range(1, 5): # Processing 5 lists of 10,000 takes around 70 seconds
for x in range(1, 3):
    randomlist = []
    randomlist = random.sample(range(1, 10001), 10000)
    start = timer()
    insertion_sort(randomlist)
    end = timer()
    result10000.append(end - start)

average10000 = sum(result10000) / len(result10000)
print("Insertion Sort on a random list of 10,000 positive integers took" , "%10.7f" % (average10000) , ", on average over 3 lists")
print("\t*** Processing 100 lists with 10,000 integers takes around 23 minutes! ***")

#
# SHELL SORT
#

def shell_sort(a_list):
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)

        #print("After increments of size", sublist_count, "The list is", a_list)

        sublist_count = sublist_count // 2

def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i

    while position >= gap and a_list[position - gap] > current_value:
        a_list[position] = a_list[position - gap]
        position = position - gap

        a_list[position] = current_value

# 100 lists of 500 positive integers
result500 = []

for x in range(1, 100):
    randomlist = []
    randomlist = random.sample(range(1, 501), 500)
    start = timer()
    shell_sort(randomlist)
    end = timer()
    result500.append(end - start)

average500 = sum(result500) / len(result500)
print("\nShell Sort on a random list of 500 positive integers took" , "%10.7f" % (average500) , ", on average over 100 lists")

# 100 lists of 1,000 positive integers
result1000 = []

for x in range(1, 100):
    randomlist = []
    randomlist = random.sample(range(1, 1001), 1000)
    start = timer()
    shell_sort(randomlist)
    end = timer()
    result1000.append(end - start)

average1000 = sum(result1000) / len(result1000)
print("Shell Sort on a random list of 1,000 positive integers took" , "%10.7f" % (average1000) , ", on average over 100 lists")

# 100 lists of 10,000 positive integers
result10000 = []

for x in range(1, 100):
    randomlist = []
    randomlist = random.sample(range(1, 10001), 10000)
    start = timer()
    shell_sort(randomlist)
    end = timer()
    result10000.append(end - start)

average10000 = sum(result10000) / len(result10000)
print("Shell Sort on a random list of 10,000 positive integers took" , "%10.7f" % (average1000) , ", on average over 100 lists")

#
# PYTHON SORT
#

def python_sort(a_list):
    a_list.sort()
    return a_list

# 100 lists of 500 positive integers
result500 = []

for x in range(1, 100):
    randomlist = []
    randomlist = random.sample(range(1, 501), 500)
    start = timer()
    python_sort(randomlist)
    end = timer()
    result500.append(end - start)

average500 = sum(result500) / len(result500)
print("\nPython's Sort() on a random list of 500 positive integers took" , "%10.7f" % (average500) , ", on average over 100 lists")

# 100 lists of 1,000 positive integers
result1000 = []

for x in range(1, 100):
    randomlist = []
    randomlist = random.sample(range(1, 1001), 1000)
    start = timer()
    python_sort(randomlist)
    end = timer()
    result1000.append(end - start)

average1000 = sum(result1000) / len(result1000)
print("Python's Sort() on a random list of 1,000 positive integers took" , "%10.7f" % (average1000) , ", on average over 100 lists")

# 100 lists of 10,000 positive integers
result10000 = []

for x in range(1, 100):
    randomlist = []
    randomlist = random.sample(range(1, 10001), 10000)
    start = timer()
    python_sort(randomlist)
    end = timer()
    result10000.append(end - start)

average10000 = sum(result10000) / len(result10000)
print("Python's Sort() on a random list of 10,000 positive integers took" , "%10.7f" % (average10000) , ", on average over 100 lists")