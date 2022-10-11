
num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))

num3 = []

#Used to count the number of times the while loop runs so the proper index of the lists can be appended
j = 0

#This first loop appends num3 with the values of num1, then num2 until it reaches the end of one of the two lists

while True:
    try:
        num3.append(num1[j]) 
    except IndexError:
        break
    try:
        num3.append(num2[j])
    except IndexError:
        break
    #because while loops do not count their number of loops by default, I created the variable j
    #This value increases with each loop
    j += 1

#After one of the lists has reached its end, the program determines which of the two lists still has values to add
#It then adds this list's values to the end of num3
if len(num1) > len(num2):
    for i in range(j+1, len(num1)):
        num3.append(num1[i])
elif len(num1) < len(num2):
    for i in range(j+1, len(num2)):
        num3.append(num2[i])

print(num3)


