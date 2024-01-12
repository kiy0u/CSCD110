#Section 3, October 12, 2023, Assignment 2 

#Assign the user response to a variable 

day = int(input("Enter a number from 1 through 7 for the day of the week:"))

#Then, according to the response, it will print to the following:

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print ("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
    print("Happy weekend!")
elif day == 7:
    print("Sunday")
    print("Happy weekend!")
else:
    print("Error: I asked for a number from 1 to 7. Please enter a number between 1 to 7.")

    
