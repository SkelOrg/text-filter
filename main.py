import json

file = open("filteredwords.json","r") # gets and reads the JSON file
blacklistedwords = json.load(file) # gets the text from JSON file and stores into array
file.close()
userinput = input()
splitinput = userinput.split()

# Code from 'https://stackoverflow.com/questions/51743776/trying-to-filter-input/51744045' by 'smagnan'
for p in blacklistedwords:
    if p in userinput:
        userinput = userinput.replace(p, '#' * len(p))
print(userinput)
