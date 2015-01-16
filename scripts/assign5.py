

largest = None
smallest = None
count =0
while True:
    inp = raw_input("Enter a number: ")
    try:

    	num = int(inp)
        if   num == "done" : break
        if len(inp) < 1 : break

    	if largest is None or largest < num:
    	    largest = num

        if smallest is None or num < smallest:
    	    smallest = num

    	print num


    except:
        print "Invalid input"
        break


print "Maximum", largest
print "Mimimum", smallest