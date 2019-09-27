
from collections import Counter 
data_set =open("/home/cs2016a202/rashid/sample.txt","r")  
data=data_set.read()  
split_it = data.split() 
Counter = Counter(split_it) 
most_occur = Counter.most_common(11)   
print(most_occur)