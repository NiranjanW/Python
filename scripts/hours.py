def computepay(h,r):


    if h <=40 :
    	pay = h*r
    else :
        pay = (40* r) + (r*1.5 * ( h-40))
    return pay

try:
    hrs = raw_input("Enter Hours:")
    hours = float(hrs)
    rte = raw_input("Enter Rate:")
    rate = float(rte)
except:
    print"Error"
    quit()


p = computepay(hours,rate)
print "Pay",p