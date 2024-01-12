#Assignment 3, Section 3, October 29, 2023
# no extra credit attempted :(
# setting the variables to their assigned number that correspond with choices 
count5 = 1
count7 = 2
addtoadd = 3
printer = 4
between515 = 5
QUIT = 0
choice = 99 

#make the menu
while choice != QUIT:
    print("MENU | Options:")
    print("1. Count from 200 to 75 by 5s")
    print("2. Count from 3 to 129 by 7s")
    print("3. Add the numbers from 210 to 325")
    print("4. Print the phrase 'Don't be evil' one letter per line")
    print("5. Print the numbers between 5 and 15")
    print("0. Quit")
    choice = int(input("Enter your option, or enter 0 to exit."))

#outcomes of said choices

    if choice == count5:
        x = 205
        while x >= 80:
            x-=5
            print(x)

    elif choice == count7:
        x = -4
        while x <= 122:
            x+=7
            print(x)

    elif choice == addtoadd:
        x = 209
        while x <= 234:
            x+=1
            print(x)

    elif choice == printer:
        for a in ("Don't be evil"):
            print(a)  

    elif choice == between515:
        for x in range(5,16):
            print(x)

    elif choice == QUIT:
        print("Thank you! Have a good day!")
        break

    else:
        print("INVALID OPTION. Please enter your option or enter 0 to quit.")

    

    
    
    