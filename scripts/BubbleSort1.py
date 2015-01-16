
def bubbleSort(items):
    for i in range(len(items)):
        for j in range(len(items) -1 -i):
            if items[j] > items[j+1]:
                items[j] , items[j+1] = items[j+1] , items[j]



if __name__ == "__main__":
    args =[1,6,2,5,8]
    bubbleSort(args)
    for x in args:
        print x