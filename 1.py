# Task 1
######### 

print("Hello World!")

# Task 2
######### 

print("Hello World! \nHello World \nHello World") #For printing multiple sentences in new line
print("Hello" + "Alana") #Output - HelloAlana
print("Hello" + " " + "Alana") #Different ways to make space between words
print("Hello " + "Alana")
print("Hello" + " Alana")

# Task 3
######### 

print("Hello" + " " + input("What is your name?") + "!") #Multiple functions inside a function

# Task 4
######### 

name = input("What is your name?") #Name value is preserved for future use
print(name)
print("Hello" + " " + name)

name = "Jack"
print(name)

username = input("What is your name?")
length = len(username) #len() function to determine the number of characters in a string
print(length)

# Task 5
######### 

print("Welcome to the Band Name Generator.")
city = input("What's the name of the city you grew up in? \n") #\n used for making the cursor in the new line for the input

pet_name = input("What's your pet's name? \n")

print("Your band name could be " + city + " " + pet_name)