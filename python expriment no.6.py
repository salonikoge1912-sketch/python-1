#question no. 1
# creat a list
number=[10,20,30,40,50]

# check membership
print(20 in number)
print(60 in number)
print(30 not in number)
print(70 not in number)

#question no. 2
# given list
fruit=["apple","banana","mango","cherry","grapes"]

#inclued
print(fruit[0])
print(fruit[2])

# negative indexing
print(fruit[-1])
print(fruit[-3])

#slicing
print(fruit[1:4])
print(fruit[:3])
print(fruit[2:])

#question no. 3
#create list
number=[1,2,3,4]

#update
number[1]=20
print (number)
       
#append
number.append(5)
print(number)

#insert
number.inserrt(2,99)
print(number)

#delete
number.remove(3)
print(number)
number.pop()
print(number)
del number[1]
print(number)

#question no. 4
#create list
list1=[1,2,3]
list2=[4,5,6]

#concatenation
print(list1 + list2)

#repetition
print(list*2)

#length
print(len(list1))

#maximum
print(max(list2))

#minimum
print(min(list2))
