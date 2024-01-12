# Section 3, October 12, 2023, Assignment 2

#Let's go golfing! - DJ Khaled 2023

#Assign the variables to integer inputs

hole = int(input("Enter the number of hole played:"))
par_val = int(input("Enter the par value for the hole:"))
num_stroke = int(input("Enter the number of strokes it took to complete the hole:"))

#The value of the slangs will be found when we subtract the number of strokes and the par value 

slang_val = num_stroke - par_val

#Then according to the difference, the following will be displayed: 

if slang_val == 0:
    uhh = "a par"
elif slang_val == 1:
    uhh = "a bogey"
elif slang_val == 2:
    uhh = "a double bogey"
elif slang_val == 3:
    uhh = "a triple bogey"
elif slang_val == 4:
    uhh = "a 4 over par"
elif slang_val == 5:
    uhh = "a 5 over par"
elif slang_val == -1:
    uhh = "a birdie"
elif slang_val == -2:
    uhh = "an Eagle"
elif slang_val == -3:
    uhh = "a Double Eagle"
elif slang_val == -4:
    uhh = "a Condor"
elif slang_val == -5:
    uhh = "an Ostritch"
else:
    uhh = "BAD SCORE"

print("On hole number", hole, ", which is a par", par_val, ", you got", uhh)
