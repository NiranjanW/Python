name = raw_input('Enter number');
handle = open(name,'r');
text = handle.read()
words = text.split
counts =dict()

for word in words:
	counts[word]=counts.get(words,0) +1

bigcount=0
bigword=0

for word,count in counts.items():
	if bigcount is None or count  > bigcount:
		bigword=word
		bigcount= count

print bigword, bigcount


