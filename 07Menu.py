
def hello_world():
    print("")
    print("----Start of Output ---------------------------")
    print("")
    print("Hello World")
    print("")
    print("----End of Output -----------------------------")
    print("")
    print("")
    print("")
    input("Press Enter to continue")
    os.system('clear')
def goodbye_world():
    print("")
    print("----Start of Output ---------------------------")
    print("")
    print("Hello World")
    input("------> Program paused - press enter to continue")
    print("Goodbye World")
    print("")
    print("----End of Output -----------------------------")
    print("")
    print("")
    print("")
    input("Press Enter to continue")
def goodbye_person():
    print("")
    print("----Start of Output ---------------------------")
    print("")
    print("Hello")
    name = input("What is your name ? ")
    print("Goodbye", name)
    print("")
    print("----End of Output -----------------------------")
    print("")
    print("")
    print("")
    input("Press Enter to continue")
def goodbye_teacher():
    print("")
    print("----Start of Output ---------------------------")
    print("")
    name = input("Teacher's name (try Mr Horan) ")
    if name == "Mr Horan":
        print("You are lucky, he is a great teacher.")
    else:
        print(name, "is an ok teacher")
    print("")
    print("----End of Output -----------------------------")
    print("")
    print("")
    print("")
    input("Press Enter to continue")
def for_loop():
    print("")
    print("----Start of Output ---------------------------")
    print("")
    for x in range(1, 500):
        print(x) 
    print("")
    print("----End of Output -----------------------------")
    print("")
    print("")
    print("")
    input("Press Enter to continue")
import os
os.system('clear')
print(' -' + '-'*(46) + '-')
print("|                                                |")
print("|    07Menu                                      |")
print("|    Name : Aditi                                |")
print("|    Version : 01                                |")
print("|                                                |")
print(' -' + '-'*(46) + '-')
print("")
print("1. Hello world")
print("2. Goodbye world")
print("3. Goodbye person")
print("4. Good teacher")
print("5. forLoop")
print("6. whileLoop")
print("7. stringLoop")
print("8. Convert to ascii")
print("9. Encode a string")
print("x. To Exit")
number = input("Enter an option ")
if number == "1":
    hello_world()
    print(' -' + '-'*(46) + '-')
    print("")
    print("1. Hello world")
    print("2. Goodbye world")
    print("3. Goodbye person")
    print("4. Good teacher")
    print("5. forLoop")
    print("6. whileLoop")
    print("7. stringLoop")
    print("8. Convert to ascii")
    print("9. Encode a string")
    print("x. To Exit")
    number = input("Enter an option ")
if number == "2":
    goodbye_world()
    print("1. Hello world")
    print("2. Goodbye world")
    print("3. Goodbye person")
    print("4. Good teacher")
    print("5. forLoop")
    print("6. whileLoop")
    print("7. stringLoop")
    print("8. Convert to ascii")
    print("9. Encode a string")
    print("x. To Exit")
    number = input("Enter an option ")
if number == "3":
    goodbye_person()
    print("1. Hello world")
    print("2. Goodbye world")
    print("3. Goodbye person")
    print("4. Good teacher")
    print("5. forLoop")
    print("6. whileLoop")
    print("7. stringLoop")
    print("8. Convert to ascii")
    print("9. Encode a string")
    print("x. To Exit")
    number = input("Enter an option ")
if number == "4":
    goodbye_teacher()
    print("1. Hello world")
    print("2. Goodbye world")
    print("3. Goodbye person")
    print("4. Good teacher")
    print("5. forLoop")
    print("6. whileLoop")
    print("7. stringLoop")
    print("8. Convert to ascii")
    print("9. Encode a string")
    print("x. To Exit")
    number = input("Enter an option ")
if number == "5":
    for_loop()
    print("1. Hello world")
    print("2. Goodbye world")
    print("3. Goodbye person")
    print("4. Good teacher")
    print("5. forLoop")
    print("6. whileLoop")
    print("7. stringLoop")
    print("8. Convert to ascii")
    print("9. Encode a string")
    print("x. To Exit")
    number = input("Enter an option ")
