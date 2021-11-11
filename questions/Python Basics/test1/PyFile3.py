escape = open("HakunaMatata")
worddic = { }
for line in escape:
    print(line)
    myline = line.split()
    print(myline)

    for word in myline:
        w = worddic.get(word,0)
        print("the word %s occours in dictionary %d times" %(word, w))
        worddic[word] = w+1
        print(" read %s" %word)
        print("The word %s occours %d times in dictionary" %(word, worddic[word]))

print("\n", worddic , "\n")
search = input("Enter search string")
if search in worddic:
    print("Found word in %s %d times" %(search, worddic[search]))
else:
    print("SOrry not found")

        


