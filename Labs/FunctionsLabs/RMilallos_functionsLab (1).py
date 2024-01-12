# ----------------------------- Change code -------------------------
# The kinetic_energy function receives 
# a value for mass and velocity and returns the 
# kinetic energy 
def kinetic_energy(mass, velocity):
    KE = 0.0
    total = mass * velocity**2 / 2
    return(total)
    # TO DO 
    # calculate the kinetic energy given mass and velocity
    # return the calculated value 
    return(total)

# The feet_to_inches function receives 
# a measurement in feet and returns the 
# measurement in inches  
def feet_to_inches(feet):
    inches = 0
    inches = feet * 12
    return(inches)

    # TO Do
    # convert feet to inches
    # return the converted value

# The format email function receives
# a first and last name and then
# returns a formatted ewu email
# Example: John Smith -> JSmith@ewu.edu 
def format_email(first_name, last_name):
    email = first_name[0] + last_name + "@ewu.edu"
    return(email)
    
    # TO DO
    # format the email
    # return the email  
# ----------------------------------------------------------------


# ----------------------------- Do not change ----------------------------
print("Start Checking")
result = kinetic_energy(50,200)
expected = 1000000.00
print(f"kinetic_energy(50,200) prduced {result} expected 100000.00")
if(expected == result):
    print("Correct Result")
else: 
    print("Incorrect Result")
print()

result = feet_to_inches(12)
expected = 144
print("feet_to_inches(12) produces", result, "expected", expected)
if(expected == result):
    print("Correct Result")
else: 
    print("Incorrect Result")
print()

result = feet_to_inches(10)
expected = 120
print("feet_to_inches(10)produces", result, "expected", expected)
if(expected == result):
    print("Correct Result")
else: 
    print("Incorrect Result")
print()

result = format_email("John", "Smith")
expected = "JSmith@ewu.edu"
print(f"format_email(\"John\", \"Smith\") produces {result} expected {expected}")
if(expected == result):
    print("Correct Result")
else: 
    print("Incorrect Result")
print()
# ------------------------------------------------------------------------
