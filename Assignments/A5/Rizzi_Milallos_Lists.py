#Assignment 5, Section 4, November 22, 2023 

#Make the main function 
def main(): 
    #set up the list 
    numlist = []
    #start a for loop so that it prompts 5 times for a number 
    for item in range(5):
        number = int(input("Enter a number: "))
        numlist.append(number) #this will append for every number entered
    #print the list, smallest #, largest #, sum and average 
    print(numlist)
    print(f'Min: {min(numlist)}')
    print(f'Max: {max(numlist)}')
    print(f'Sum: {sum(numlist)}')
    print(f'Average: {sum(numlist)/len(numlist)}')



#Call main function 
main()