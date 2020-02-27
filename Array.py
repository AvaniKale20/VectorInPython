from array import *

values = array('i', [1, 2, 3, ])
print values
print
print "printing value in array one by omne"
for i in range(len(values)):
    print (values[i])

print "without using range "
for e in values:
    print (e)
