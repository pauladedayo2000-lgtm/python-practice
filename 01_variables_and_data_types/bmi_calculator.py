"""Calculate BMI from user input and show the basic data types."""

name = input("Enter your name: ")                    # str
age = int(input("Enter your age: "))                 # int
weight_kg = float(input("Enter your weight in kg: "))   # float
height_m = float(input("Enter your height in metres: "))  # float

bmi = weight_kg / (height_m ** 2)
in_healthy_range = 18.5 <= bmi < 25                  # bool

print(f"{name}, age {age}, your BMI is {bmi:.1f}")
print("In healthy range:", in_healthy_range)
print("Types used:", type(name).__name__, type(age).__name__,
      type(bmi).__name__, type(in_healthy_range).__name__)
