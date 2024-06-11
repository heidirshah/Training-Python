print("This is a BMI calculator")
height = float(input("Enter your height in meter:"))   #by default, input() reads string values, therfore casting needs to be used for integer
weight = float(input("Enter your weight in kg:"))

bmi = weight/height

print("Your BMI:",bmi)