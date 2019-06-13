#creating a list
lst = [2, 5, 3, 5, 6, 5, 8, 5, 9, 5]
print("Initial List:\n",lst)

#removing all the same elements using loop
for x in lst:
    lst.remove(5)

#final elements
print("Final List:\n",lst)
