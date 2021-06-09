enteredNumbers = input("Enter your numbers: ")
a = ""
arrayDef = []
for i in range (len(enteredNumbers)):
    if((enteredNumbers[i] != ';') and (enteredNumbers[i] != ',')):
        a += enteredNumbers[i]
    else:
        arrayDef.append(int(a))
        a = ""
arrayDef.append(int(a))
arrayDef.pop(0)
for i in range (len(arrayDef)-1):
    for j in range(i+1, len(arrayDef)):
        if(arrayDef[i] > arrayDef[j]):
            temp = arrayDef[i]
            arrayDef[i] = arrayDef[j]
            arrayDef[j] = temp

for i in range (len(arrayDef)-1):
    if (arrayDef[i] == arrayDef[i+1]):
        print(arrayDef[i])
        break

