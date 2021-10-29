filename = "data.txt"
i=0
j=0
maximus=0
counter=0
with open(filename, encoding="utf8") as file:
    contents = file.readlines()
    for i in range (0,10000-1):
        
        for j in range (i+1, 10000):
            if(int(contents[i])*int(contents[j]))%34 != 0:
               counter = counter +1
               if int(contents[i])+int(contents[j])>maximus:
                   maximus = int(contents[i])+int(contents[j])
print(counter)
print(maximus)
