#Logical operators and or not  in python

temp = int(input("What is the temperature is outside:? "))

if not(temp >= 0 and temp <= 30):
    print("The temperature is good today.")
    print("Go outside ")
elif not (temp <= 0 or temp >=30):
    print("The temperature is bad today ")
    print("Stay inside.!")

#     #not operator
# if not (temp >= 0 and temp <= 30):
#      print("The temperature is good today.")
#      print("Go outside ")