
# myList = [1,5,8,200,4,"test"]   #list is array in c

# print(myList[3])

# myList[4] = 900

# print(myList)

# myList[0] = myList[2]
# print("new list:",myList)

# print("length of myList:", len(myList))

# aString = "heidir"
# print(len(aString))
# print(aString[3])

# print("slice aString [1:3 -->]", aString[1:3])

# print("slice aString [ :5 -->]", aString[ :5])

# print("slice aString [ 2: -->]", aString[ 2:])

# print("slice aString [ :  -->]", aString[ : ])

myList = []

for i in range(5):
    myList.append(i)

print("myList append",myList)

myList1 = []

for i in range(5):
    myList1.insert(i,i+5)

print("myList1 insert",myList1)