#ex.3 calculate bmi
print("welcome to the BMI Helper for Seniors!")

height = int(input("Please enter height (cm): "))
weight = int(input("Please enter weight (kg): "))
bmi = weight / (height / 100)**2

print(f"Your BMI is {bmi}")
print(f"Your BMI is {bmi: .2f}")
