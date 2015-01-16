from math import log

txt= list()


with open('file.txt' , 'r') as fr , open ('file2.txt', 'w+')  as fw :
    for line in fr:
        items = line.split()
        txt.append("{0}\t{1}".format(items[0], log(float(items[1]))))
    fw.write("\n".join(txt))

#read large file
def readInChunks(fileObj, chunkSize=2048):
    """
    Lazy function to read a file piece by piece.
    Default chunk size: 2kB.
    """
    while True:
        data = fileObj.read(chunkSize)
        if not data:
            break
        yield data

f = open('bigFile')
for chuck in readInChunks(f):
    do_something(chunk)