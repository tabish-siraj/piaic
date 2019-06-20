#creating a list and printing
lst = [2, 5, 3, 5, 6, 5, 8, 5, 9, 5]
print("Initial List:\n",lst)

#Taking number which is to remove from the list
num = int(input("Input the number you want to remove:\t"))
#removing all the same elements using loop
for x in lst:
    if x == num:
        lst.remove(num)

#final elements
print("Final List:\n",lst)
