 
a=some array of integers
 
split = [a[i:i+10] for i in xrange(0, len(a), 10)] 
 
for i in split:
    j = max(i) 
    k = i.index(max(i))
    print (j,k)
