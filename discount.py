#Discount program
salary = float(input("Enter your salary: "))
years_of_service = int(input("Enter your year of service: "))

if years_of_service > 10:
    bonous_percentage = 0.12

elif years_of_service >= 6 and years_of_service <= 10:
     bonous_percentage = 10

else:
    bonous_percentage = 0.08

bonous_amount = salary * bonous_percentage
print("your bonous percentage is:", bonous_amount)
