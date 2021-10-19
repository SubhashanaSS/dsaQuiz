def devideByTwo(n):
    if(n == 1):
        return 2
    else:
        return devideByTwo(n-1)/2;

n = int (input("Enter number: "))
while(n != -1):
    print(devideByTwo(n))
    n = int(input("Enter Number: "))
print("Finished")
    
