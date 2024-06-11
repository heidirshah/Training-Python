# while <comparison>:
#     instruction1
#     instruction2
#     instruction3

x = int(input("Enter a number:\n\n"))

oddNumber = 0
evenNumber = 0

while x != 0:
    #print("I'm stuck inside while loop")
    if x%2 == 0:
        evenNumber += 1
    else:
        oddNumber += 1

    x = int(input("enter 0 to quit while loop:\n\n"))

print("evenNumber count =",evenNumber,sep=" ")
print("oddNumber count =", oddNumber,sep=" ")