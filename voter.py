#

citizen = input("Enter your citizenship: ")
age = int(input("Enter your age: "))
    
    # Ask if they have a passport or ID
has_passport = input("Do you have a passport? (yes/no): ")
has_id = input("Do you have an ID? (yes/no): ")

country = ['kenyan', 'ugandan', 'tanzanian']

if (citizen
        and age > 18 
        and (has_passport == 'yes' or has_id == 'yes')):
        print("You are eligible to vote.")
else:
        print("You are not eligible to vote.")
