
text = "X-DSPAM-Confidence:    0.8475";

x = text.split(':')
#print x
v = filter(lambda n: n.isdigit(),x)
print  x[1]
#print x[0]
#print text.slice(18:30)

# def filterbyvalue(seq, value):
#    for el in seq:
#        if el.attribute==value: yield el
#
# [i for i in list if i.attribute == value]
#
# import re
# re.sub(r'\D', '', '+123-456-7890')