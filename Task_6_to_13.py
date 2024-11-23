#Task 6: Basic Arithmetic Calculator

a = int(input("Enter the first number : "))
b = int(input("Enter the second number: "))

addition = a+b
substraction = a-b
multiplication = a*b
division = a/b

print("\nAddition = " , addition)
print("Substraction = " , substraction)
print("Multiplication = " , multiplication)
print("Division = " , division)
print("\n------------------------------------------------------------")

#Task 7: Personal Information Script

name = input("\nEnter your name : ")
age  = int(input("Enter your age : "))
color= input("Enter your favourite colour : ")

print("\nHello " + name + ".\nYour age is : " , age , "\nYour favourite colour is : " + color)
print("\n-------------------------------------------------------------")

#Task 8: Unit Conversion Program

days = int(input("\nEnter the number of days : "))

hours = days * 24
minutes  = hours * 60
seconds  = minutes * 60

print("\nYour working hours\t: " , hours)
print("Your working minutes\t: " ,minutes)
print("Your working seconds\t: " , seconds)
print("\n---------------------------------------------------------------")


#Task 9: Simple Interest Calculator

principal = float(input("\nEnter the principal amount : "))
rate_of_interest = float(input("Enter the rate of interest (in %): "))
time = float(input("Enter the time (in years): "))

simple_interest = (principal * rate_of_interest * time) / 100

print(f"The simple interest for the entered values is: {simple_interest}")
print("\n---------------------------------------------------------------")

#Task 10: Temperature Conversion

c = float(input("Enter the temperature in Celsius :"))
f = c*(9/5) + 32
print(c," Celsiu = " ,f, " Farenheit")

F = float(input("\nEnter the temperature in Farenheit : "))
C = (F-32)*5/9
print(F, " Farenheit = ",C, " Celsius")
print("\n---------------------------------------------------------------")

#Task 11: Grocery Bill Estimator

item_1 = int(input("Enter the price of item 1 : "))
item_2 = int(input("Enter the price of item 2 : "))
item_3 = int(input("Enter the price of item 3 : "))

total  = item_1 + item_2 + item_3

print("\nTotal Cost : Rs." , total)
print("\n---------------------------------------------------------------")

#Task 12: Distance Converter

meters = int(input("Enter the distance in meters : "))
km = meters/1000
miles = meters * 0.000621371

print("\nThe distance in kilo meters : " ,km)
print("The distance in miles : " , miles)
print("\n---------------------------------------------------------------")

#Task 13: BMI Calculator

height = float(input("Enter your height in meters(M) : "))
weight = float(input("Enter your weight in kilograms(kg) : "))
bmi = weight/height**2

print("\nYour BMI value : " , bmi)
print("\n---------------------------------------------------------------")


