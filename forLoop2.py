# for i in range (2,10,2):
#     if i == 6:
#         break
#     print("inside for loop", i)

# print("outside for loop",i)

# for i in range (2,20,2):
#     if i == 6:
#         continue                    #number 6 will be skipped
#     print("inside for loop", i)

# print("outside for loop",i)

# for i in range (2,20,2):
#     if i == 6 or i == 10:
#         continue                    #number 6 & 10 will be skipped
#     print("inside for loop", i)

# print("outside for loop",i)

for i in range (20):
    if i == 6 or i%2 == 1:
        continue                    #number 6 & odd will be skipped
    print("inside for loop", i)

print("outside for loop",i)