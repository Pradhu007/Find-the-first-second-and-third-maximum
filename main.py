

intcountinput = int(input("Enter how many integers?"))

numlist = []
for i in range(intcountinput):
    n = int(input("Enter number"))
    numlist.append(n)


max = 0
previousmax = 0
thirdmax = 0

for i in range(len(numlist)):

    if int(numlist[i]) > max:
        thirdmax = previousmax
        previousmax = max
        

        max = numlist[i]






print("The maximum score is {}".format(max))
print("The runner up score is {}".format(previousmax))
print("The third max is {}".format(thirdmax))












