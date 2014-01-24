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

def test():
    xs = [3,2,4,5,1]
    print(bubblesort(xs))

test()