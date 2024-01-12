#Section 4, Assignment 4, November 8, 2023
#Extra Credit attempted for doc string, not presenting the numbers or phrase backwards
# i also googled the equation for the light year to miles because i have no clue what it was
# also went to office hours for help from Rob Lemlin, shoutout Rob Lemlin  

F_to_C = 1
C_to_F = 2
LY_to_M = 3
M_to_F = 4
QUIT = 0
choice = 99


#In our main function, this is where we'll call our menu and ask for input 
def main():
    menu()
    choice = int(input("Please select an option or type in 0 to exit the program."))
#In the menu function, this is where we'll list all of our options     
def menu():
    print("Menu | Options: ")
    print("1. Convert Fahrenheit to Celsius")
    print("2. Convert Celsius to Fahrenheit")
    print("3. Convert Light Years to Miles")
    print("4. Convert Meters to Feet")
    print("0. Quit")
    
#Define functions and make them do the operations 
def fare_to_cels(fahrenheit):
    '''
    fare_to_cels(value in farenheit):
    This function converts a value in Farenheit to Celsius and then returns it in a float value 
    Ex: 
    >>>fare_to_cels(32)
    >>>0.0
    '''
    return (fahrenheit - 32) * 5/9 

def cels_to_fare(celsius):
    '''
    cels_to_fare(value in celsius):
    This function converts a value in Celsius to Farenheit and then returns it in a float value
    Ex:
    >>>cels_to_fare(0)
    >>>32.0
    '''
    return (9/5) * celsius + 32

def light_to_mile(light):
    '''
    light_to_mile(value in lightyears):
    This function converts a value in lighteyars to miles then returns it in a float value 
    Ex:
    >>>light_to_mile(1)
    >>>5878625370000.0
    '''
    return light * 5878625370000

def met_to_ft(meter):
    '''
    met_to_ft(value in meter)
    This function converts a value in meters to feet then returns it in a float value 
    Ex:
    >>>met_to_ft(1)
    >>>3
    '''
    return meter * 3
    
  


# outcome of users choice, this will be in a while loop, and when the while condition is met the
# menu function will be called and will ask for choice and will repeat until broken
while choice != 0:
    menu()
    choice = int(input("Please select an option or type in 0 to exit the program."))

    if choice == F_to_C:
        f = float(input("Enter the tempurature in Farenheit: "))
        fare_to_cels(f)
        print(f,'degreeF is equal to', fare_to_cels(f), 'degrees Celsius' )
        

    elif choice == C_to_F:
        c = float(input("Enter the tempurature in Celsius: "))
        cels_to_fare(c)
        print(c, 'degreesC is equal to', cels_to_fare(c), 'degrees Fahrenheit')

    elif choice == LY_to_M:
        ly = float(input("Enter a distance in lightyears: "))
        light_to_mile(ly)
        print(ly, 'lightyears is equal to', light_to_mile(ly), 'in miles')

    elif choice == M_to_F: 
        m = float(input("Enter a distance in meters: "))
        met_to_ft(m)
        print(m, 'meters is equal to', met_to_ft(m), 'in feet')

    elif choice == QUIT:
        exit()
    
    else:
        print("Invalid selection. Select a option or press 0 to quit. ")
    
    
    
#We'll call the main function in the end for this to start
main() 





