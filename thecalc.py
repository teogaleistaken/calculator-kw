numbers = []
operations = []

mathematical = str(input("enter your math:\n"))
mathematical += " "

placeholder = ""

for i in range(0, len(mathematical)):
    if mathematical[i] == "+":
        operations.append(1)
    elif mathematical[i] == "-":
        operations.append(2)
    elif mathematical[i] == "*":
        operations.append(3)
    elif mathematical[i] == "/":
        operations.append(4)
    else:
        if mathematical[i] >= "0" and mathematical[i] <= "9":
            placeholder += mathematical[i]
            if mathematical[i + 1] < "0" or mathematical[i + 1] > "9":
                numbers.append(int(placeholder))
                placeholder = ""

result = []
notfirstinline = False
subresult = 0

for i in range(0, len(operations) + 1):
    if len(operations) == i:
        if notfirstinline == False:
            result.append(numbers[i])
            break
        result.append(subresult)
        break

    if notfirstinline == False:
        subresult = numbers[i]

    if operations[i] > 2:
        if operations[i] == 3:
            subresult *= numbers[i + 1]
        else:
            subresult /= numbers[i + 1]
        notfirstinline = True
    else:
        notfirstinline = False
        result.append(subresult)
        subresult = 0

subresult = result
result = 0
idx = 0
notfirstinline = False

for i in range(0, len(operations)):
    if notfirstinline == False:
        result = subresult[idx]
        
    if operations[i] < 3:
        idx += 1
        if operations[i] == 1:
            result += subresult[idx]
        else:
            result -= subresult[idx]

        notfirstinline = True

print(result)
