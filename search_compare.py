import random
import timeit
from timeit import default_timer as timer

print("\n\tFor each of the 4 search methods:")
print("\t - generate 100 lists of 500 positive integers")
print("\t - generate 100 lists of 1,000 positive integers")
print("\t - generate 100 lists of 10,000 positive integers")
print("\t\t... and then run each search method on each set of 100 lists (3 per search method)")
print("\t\t... and figure out the average time to run each using the timeit module")
#
# Sequential Search - no sorting on the list
#
def sequential_search(a_list, item):
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos+1

    return found

# 100 lists of 500 positive integers
result500 = []

for x in range(1, 100):
    randomlist = []
    randomlist = random.sample(range(1, 501), 500)
    start = timer()
    sequential_search(randomlist, -1)
    end = timer()
    result500.append(end - start)

averagess = sum(result500) / len(result500)
print("\nSequential Search on a random list of 500 positive integers took" , "%10.7f" % (averagess) , ", on average")

# 100 lists of 1,000 positive integers
result1000 = []

for x in range(1, 100):
    randomlist = []
    randomlist = random.sample(range(1, 1001), 1000)
    start = timer()
    sequential_search(randomlist, -1)
    end = timer()
    result1000.append(end - start)

averagess = sum(result1000) / len(result1000)
print("Sequential Search on a random list of 1,000 positive integers took" , "%10.7f" % (averagess) , ", on average")

# 100 lists of 10,000 positive integers
result10000 = []

for x in range(1, 100):
    randomlist = []
    randomlist = random.sample(range(1, 10001), 10000)
    start = timer()
    sequential_search(randomlist, -1)
    end = timer()
    result10000.append(end - start)

averagess = sum(result10000) / len(result10000)
print("Sequential Search on a random list of 10,000 positive integers took" , "%10.7f" % (averagess) , ", on average")

#
# Ordered Sequential Search - list is sorted
#
def ordered_sequential_search(a_list, item):
    pos = 0
    found = False
    stop = False

    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos+1

    return found

# 100 lists of 500 positive integers
ossresult500 = []

for y in range(1, 101):
    randomlist2 = []
    randomlist2 = random.sample(range(1, 501), 500)
    randomlist2.sort()
    start2 = timer()
    ordered_sequential_search(randomlist2, -1)
    end2 = timer()
    ossresult500.append(end2 - start2)

averageoss = sum(ossresult500) / len(ossresult500)
print("\nOrdered Sequential Search of a sorted list of 500 positive integers took" , "%10.7f" % (averageoss) , ", on average")

# 100 lists of 1,000 positive integers
ossresult1000 = []

for y in range(1, 101):
    randomlist2 = []
    randomlist2 = random.sample(range(1, 1001), 1000)
    randomlist2.sort()
    start2 = timer()
    ordered_sequential_search(randomlist2, -1)
    end2 = timer()
    ossresult1000.append(end2 - start2)

averageoss = sum(ossresult1000) / len(ossresult1000)
print("Ordered Sequential Search of a sorted list of 1,000 positive integers took" , "%10.7f" % (averageoss) , ", on average")

# 100 lists of 10,000 positive integers
ossresult10000 = []

for y in range(1, 101):
    randomlist2 = []
    randomlist2 = random.sample(range(1, 10001), 10000)
    randomlist2.sort()
    start2 = timer()
    ordered_sequential_search(randomlist2, -1)
    end2 = timer()
    ossresult10000.append(end2 - start2)

averageoss = sum(ossresult10000) / len(ossresult10000)
print("Ordered Sequential Search of a sorted list of 10,000 positive integers took" , "%10.7f" % (averageoss) , ", on average")

#
# Binary Search Iterative - list is sorted
#
def binary_search_iter(a_list, item):
    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found

# 100 lists of 500 positive integers
bsiresult500 = []

for z in range(1, 101):
    randomlist3 = []
    randomlist3 = random.sample(range(1, 501), 500)
    randomlist3.sort()
    start3 = timer()
    binary_search_iter(randomlist3, -1)
    end3 = timer()
    bsiresult500.append(end3 - start3)

averagebsi = sum(bsiresult500) / len(bsiresult500)
print("\nBinary Search Iterative of a sorted list of 500 positive integers took" , "%10.7f" % (averagebsi) , ", on average")

# 100 lists of 1,000 positive integers
bsiresult1000 = []

for z in range(1, 101):
    randomlist3 = []
    randomlist3 = random.sample(range(1, 1001), 1000)
    randomlist3.sort()
    start3 = timer()
    binary_search_iter(randomlist3, -1)
    end3 = timer()
    bsiresult1000.append(end3 - start3)

averagebsi = sum(bsiresult1000) / len(bsiresult1000)
print("Binary Search Iterative of a sorted list of 1,00 positive integers took" , "%10.7f" % (averagebsi) , ", on average")

# 100 lists of 10,000 positive integers
bsiresult10000 = []

for z in range(1, 101):
    randomlist3 = []
    randomlist3 = random.sample(range(1, 10001), 10000)
    randomlist3.sort()
    start3 = timer()
    binary_search_iter(randomlist3, -1)
    end3 = timer()
    bsiresult10000.append(end3 - start3)

averagebsi = sum(bsiresult10000) / len(bsiresult10000)
print("Binary Search Iterative of a sorted list of 10,000 positive integers took" , "%10.7f" % (averagebsi) , ", on average")

#
# Binary Search Recursive - list is sorted
#
def binary_search_recur(a_list, item):
    if len(a_list) == 0:
        return False
    else:
        midpoint = len(a_list) // 2
    if a_list[midpoint] == item:
        return True
    else:
        if item < a_list[midpoint]:
            return binary_search_recur(a_list[:midpoint], item)
        else:
            return binary_search_recur(a_list[midpoint + 1:], item)

# 100 lists of 500 positive integers
bsrresult500 = []

for aa in range(1, 101):
    randomlist4 = []
    randomlist4 = random.sample(range(1, 501), 500)
    randomlist4.sort()
    start4 = timer()
    binary_search_recur(randomlist4, -1)
    end4 = timer()
    bsrresult500.append(end4 - start4)

average = sum(bsrresult500) / len(bsrresult500)
print("\nBinary Search Recursive of a sorted list of 500 positive integers took" , "%10.7f" % (average) , ", on average")

# 100 lists of 1,000 positive integers
bsrresult1000 = []

for aa in range(1, 101):
    randomlist4 = []
    randomlist4 = random.sample(range(1, 1001), 1000)
    randomlist4.sort()
    start4 = timer()
    binary_search_recur(randomlist4, -1)
    end4 = timer()
    bsrresult1000.append(end4 - start4)

average = sum(bsrresult1000) / len(bsrresult1000)
print("Binary Search Recursive of a sorted list of 1,000 positive integers took" , "%10.7f" % (average) , ", on average")

# 100 lists of 10,000 positive integers
bsrresult10000 = []

for aa in range(1, 101):
    randomlist4 = []
    randomlist4 = random.sample(range(1, 10001), 10000)
    randomlist4.sort()
    start4 = timer()
    binary_search_recur(randomlist4, -1)
    end4 = timer()
    bsrresult10000.append(end4 - start4)

average = sum(bsrresult10000) / len(bsrresult10000)
print("Binary Search Recursive of a sorted list of 10,000 positive integers took" , "%10.7f" % (average) , ", on average")