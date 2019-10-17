#Taking input as an integer
num = int(input("Please input a number:\t"))

#checking if the number is greater than 1
if num > 1: 
    #checking for factors
    for i in range (2,num):
        if(num % i) == 0:
            print(num,"is not a prime number")
            print(i,"times",num//i,"is",num)
            break
    else:
       print(num,"is a prime number")
       
# if input number is less than or equal to 1, it is not prime
else:
   print(num,"is not a prime number")
