#check if the conditions is true or not 

age = int(input("What is your age :"))

if age > 18 :
    print("You are eligible for voting.")

elif age <= 0:
    print("You havent born yet")

else:
    print("You are not eligible for the voting.")
