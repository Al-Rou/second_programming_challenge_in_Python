#Prompt the user for entries
enteredNumbers = input("Enter your numbers: ")
a = ""
#Defining the array and filling it out with all numbers
arrayDef = []
for i in range (len(enteredNumbers)):
    if((enteredNumbers[i] != ';') and (enteredNumbers[i] != ',')):
        a += enteredNumbers[i]
    else:
        arrayDef.append(int(a))
        a = ""
arrayDef.append(int(a))
#Deleting the first entered number, as it is the length of array, not an entry
arrayDef.pop(0)
#Sorting the array
for i in range (len(arrayDef)-1):
    for j in range(i+1, len(arrayDef)):
        if(arrayDef[i] > arrayDef[j]):
            temp = arrayDef[i]
            arrayDef[i] = arrayDef[j]
            arrayDef[j] = temp
#Finding two neighbors which are the same
for i in range (len(arrayDef)-1):
    if (arrayDef[i] == arrayDef[i+1]):
        print(arrayDef[i])
        break

