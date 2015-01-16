
import random

def insertionSort(items):
    for i in range(1, len(items)):
        j=i
        while j >0 and items[j] > items[j-1]:
            items[j], items[j-1] = items[j-1] , items [j]
            j -=1

if __name__ == "__main__":
    items =[ random.randint (-50,100) for c in range(32)]
    print "Before" , items
    insertionSort(items)
    print "After" , items