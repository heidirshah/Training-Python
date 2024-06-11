print("This is a BMI calculator")
height = float(input("Enter your height in meter:"))   #by default, input() reads string values, therfore casting needs to be used for integer
weight = float(input("Enter your weight in kg:"))

bmi = weight/height**2

underWeight = 18.4
normal = 24.9
overWeight = 39.9

print("Your BMI:",round (bmi,2))    #round is used to round up to specific number of integer

if bmi <= underWeight:
    print("You are under-weight")
elif bmi <= normal:
    print("you have normal weight")
elif bmi <= overWeight:
    print("You are over-weight")
else:
    print("You are obese")