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

def test():
    xs = [3,2,4,5,1]
    print(bubblesort(xs))

#test()
x1 = [1,3,4]
x2 = [2,5]
print(merge(x1,x2))