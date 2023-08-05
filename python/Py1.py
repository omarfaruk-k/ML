print("Bismillah")


#############--------------------String,Range-----------------#############
s = "Machine Learning"

print(s)
print("\n")
print(s[8::])
print(s[0:6:])

print(s[::-1])  #to reversly print a string

print(f"Length of the stirng is {len(s)} \n")



###############----------------------List----------------------#################

lst=["a","aaa", 1, 30101] #py list can hold multiple data type
print(lst)

lst.append("JKi23")  ##Just insert a element at the last position of list
print(lst)

lst.pop()   ##Delete the last element of list
print(lst)


lst.pop(1)  ##remove items from given index in list
print(lst)

list2 = [5, 8, 1, 6, 2, 2, 4]
print(f"Unsorted list: {list2}")

list2.sort()

print(f"Sorted list: {list2}")

##############---------------------Dictionary----------------#################

dictionary = {'A':'Alpha','B':'Bravo', "D":'Delta', 'a':102, 'b':893, 'ListInDic':[1,3,5,7,9]}

print(dictionary) ##Printing the whole dictionary
dictionary['c']=435
print(dictionary)
print(dictionary['A'])
print(f'One element of a List inside Dictionary {dictionary["ListInDic"][1]}')

print(f'Printing only Keys of dictionary {dictionary.keys()}')
print(f'Printing only values of dictionary {dictionary.values()}')
print(f'Printing only Items of dictionary {dictionary.items()}')


###########---------------------- Set ----------------------##############

set1=set()
set1.add(120)
set1.add(670)
set1.add(120)
set1.add(120)
print(set1)

list1=[1,1,1,1,1,3,3,3,3,3,3,3,5,5,5,5,5,7,9]
set2=set(list1)   ##to find the unique elements of a list, we can put it in set as set does not hold repeted values

print(set2)



############---------------------- For --------------##############

for ltr in s:
    print(ltr)

for k,v in dictionary.items():
    print(f'value {v}')

for k,v in dictionary.items():
    print(f'Key {k}')


