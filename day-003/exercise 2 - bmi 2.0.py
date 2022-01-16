# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = weight / (height ** 2)

if bmi < 18.5:
	print(f"Your BMI is {int(round(bmi, 0))}, you are underweight.")
elif 18.5 <= bmi and bmi < 25: 
	print(f"Your BMI is {int(round(bmi, 0))}, you have a normal weight.")
elif 25 <= bmi and bmi < 30:
	print(f"Your BMI is {int(round(bmi, 0))}, you are slightly overweight.")
elif 30 <= bmi and bmi < 35:
	print(f"Your BMI is {int(round(bmi, 0))}, you are obese.")
else:
	print(f"Your BMI is {int(round(bmi, 0))}, you are clinically obese.")

