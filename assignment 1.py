input1 = int(input("enter integer a > 0")) #input minimum 
input2 = int(input("enter integer b > 0")) #input maximum
input3 = int(input("enter integer c >= 0")) #input maxpower 

for i in range(input1, input2+1): #loop through numbers in range from input1 to input2
    sumpowers = 0 #store the sum of powers
    for j in range(input3 + 1): #loop though values from 0 to input3
        i_power = i ** j #calculate power 
        print(i_power, end=" ") #print the power value with a space
        sumpowers += i_power #Add the power value to the sum 

    print(f"sum {sumpowers}") #print the totalsum of powers 