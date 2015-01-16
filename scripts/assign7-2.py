import re
fname = raw_input("Enter file name: ")
fh = open(fname)
count=0
sum = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    print line
    list = line.split(':')
    count  +=1
    x=line.find( ':')


    #tok = tok.strip()
    b = line[x+1:]
    b = float(b)
    sum  = sum + b

    re.sub("\n", "", file-contents-here)
    clean = ''.join(l[:-1] for l in open('thefile.txt'))

print "Done"
print count
print b
print sum
