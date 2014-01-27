import random
import timeit
def bubblesort(xs):
    swapped = True
    while swapped:
        swapped = False
        # Do a single pass of the list
        for i in range(len(xs)-1):
            if xs[i] > xs[i+1]:
                #Swap xs[i] and xs[i+1]
                temp = xs[i+1]
                xs[i+1] = xs[i]
                xs[i] = temp

                swapped = True
    return xs

def mergesort(xs):
    if(len(xs) < 2):
        return xs
    
    middleindex = int(len(xs)/2)
    firsthalf = xs[0:middleindex]
    secondhalf = xs[middleindex:len(xs)]
    return merge(mergesort(firsthalf),mergesort(secondhalf))

def merge(first,second):
    merged = []
    while(len(first) > 0 and len(second) > 0):
        if(first[0] <= second[0]):
            merged.append(first.pop(0))
        else:
            merged.append(second.pop(0))
    merged.extend(first)
    merged.extend(second)
    return merged

def quicksort(xs):
    #Choose the middle element as a pivot.
    #TODO: Compare other pivot strategies (pick randomly, or first element)
    if (len(xs) < 2):
        return xs

    pivotindex = int(len(xs)/2)
    pivot = xs.pop(pivotindex)
    lowers = []
    uppers = []
    
    for x in xs:
        if (x <= pivot):
            lowers.append(x)
        else:
            uppers.append(x)

    result = []
    result.extend(quicksort(lowers))
    result.append(pivot)
    result.extend(quicksort(uppers))

    return result

def quicksortrandom(xs):
    #Choose a random element as a pivot.
    if (len(xs) < 2):
        return xs

    pivotindex = random.randrange(len(xs))
    pivot = xs.pop(pivotindex)
    lowers = []
    uppers = []
    
    for x in xs:
        if (x <= pivot):
            lowers.append(x)
        else:
            uppers.append(x)

    result = []
    result.extend(quicksort(lowers))
    result.append(pivot)
    result.extend(quicksort(uppers))

    return result


def test():
    xs = [3,2,4,5,1]
    print(bubblesort(xs))

#test()
#x1 = [random.randrange(100) for i in range(100)]
#print("Middle", timeit.timeit("sorts.quicksort(x1)", number = 10000, setup = "import sorts, random; x1 = sorts.x1"))
#print("Random", timeit.timeit("sorts.quicksortrandom(x1)", number = 10000, setup = "import sorts, random; x1 = sorts.x1"))