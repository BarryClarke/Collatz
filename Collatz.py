#Program to prove the Collatz conjecture

n = int(input("Enter a positive integer: "))

#Keep looping until we reach 1
while n!= 1:
#Print the current value of n    
    print(n)
    #If n is even, divide by 2
    if n % 2 == 0:
        n = n//2
    #If n is odd, multiply by 3 and add 1
    else:
        n = (3*n) +1

#Finally, print the 1
print(n)
