import pdb


def bubbleSort(low, high):
    args =[1,6,2,5,8]
    i = low
    j= high
    #j= len(args) -1
    pivot = args[low+ (high -low)/2]

    while  (i <=j):
        #pdb.set_trace()
        while ( args[i] < pivot):
            i += 1

        while (args[j] > pivot):
            j -= 1

        if (i <= j):
            swap(i,j)
            i +=1
            j -=1

    #recursion
    if (low < j):
        bubbleSort(low,j)
    if( i<high):
        bubbleSort(i,high)


    return args


def swap( x ,y):
    temp = args[x]
    args[x] = args[y]
    args[y] = temp

if __name__ == "__main__":
    args =[1,6,2,5,8]
    x = bubbleSort(0, len(args)-1)
    print(x)

   # for i in x:
   #     print(i)

