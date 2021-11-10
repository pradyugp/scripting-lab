#Write a Python Program which will
#a) Read the contents of a file line by line
#b) Counts the frequency of words occuring in each line

escape = open('HakunaMatata')

worddic = { }
for line in escape:
    print (line)
    myline = line.split()

    print (myline)

    for word in myline:
        w = worddic.get(word,0) #0 is put into the dictionary to determine from where to count from
        #Try this: w = worddic.get(word,100)
        print ("The word %s occurs in dictionary %d times" %(word, w))

        worddic[word] = w + 1
        print("After adding the new word read %s" %word)
        print ("The Word %s occurs %d times in dictionary " %(word, worddic[word]))

print ("\n", worddic ,"\n ")
