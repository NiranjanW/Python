fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line.rstrip()
    words = line.split()
    for word in words :
        if word in lst : continue
        lst.append(word)

    #lst =line.split()
lst.sort()
print lst