my_name = input("what is your name")
my_age = input("how old are you")

print("My name is" + my_name + "and i am" + my_age + "years old")

first_number = input("enter random number")
secound_number = input("enter another number")
operation = input("enter the operation")

if operation == "+":
   print(first_number + secound_number)

elif operation == "*":
   print("first_number secound_number")
elif operation == "-":
   print(first_number - secound_number)
elif operation == "/":
   print(first_number / secound_number)
else :
   print("the operation is not avalid")


bus_capacity = (20)
people_inbus = input("the people in the bus")
people_outbus = input("the people want to enter the bus")

empty_seats = bus_capacity - people_inbus 

if empty_seats > people_outbus:
   print("the empty seats is " + empty_seats)
elif empty_seats <= people_outbus:
   print("there is no empty seats")











































