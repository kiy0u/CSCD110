#Assignment 6, Section 4, November 29, 2023


#create main function
def main():
    # initailize the list
    funnyList = []
    #prompt which file to open
    file = input("Which file would you like to open: ")
    
    try:
        # open the file
        fyle = open(file, 'r')
        #read lines in said file 
        funnyList = fyle.readlines()
        #take out the funny \n thingymabober
        for index in range(len(funnyList)):
            funnyList[index] = funnyList[index].rstrip()
        # CLOSE THE FILE
        fyle.close()
        # now display the list
        print(funnyList)
    except:
        print("This file cannot be found. Well I can't really find it for you.")
        

main()
        
        
    
