print("Demonstration of Tuple :")

#Ordered and Hetrogeneous
Tuple1 = (10,"Hello",3.14,False)
print(Tuple1)

#Indexed
print(Tuple1[1])

#Duplicate Allowed
Tuple2 = (11,21,11,31,41,21)
print(Tuple2)

#Data is Immutable
#Tuple2[0] = 12
#print(Tuple2)

#Tuple is Immutable
#Tuple2.append(51)
#print(Tuple2)

#Tuple1.remove(False)
#print(Tuple1)

for value in Tuple2:
    print(value)

print("-----------------------------------")
for i in range(len(Tuple2)):
    print(Tuple2[i])    
