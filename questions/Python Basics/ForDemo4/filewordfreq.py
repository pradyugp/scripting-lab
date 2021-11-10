escape = open('Escape.txt')

worddic = { }
for line in escape: 
 print line 
 myline = line.split()
 print myline

 for word in myline: 
  w = worddic.get(word,0)
  print "key word %s exists in doctionary with %d value" %(word, w)  
  
  worddic[word] = w + 1
  print worddic[word] 
 
print worddic ,"\n "

search = raw_input("Enter search string: ")
if search in worddic: 
   print "Found word %s %d times" %(search, worddic[search])
else: 
   print "Sorry! Not found"


# ---- Code Modification Expected --- 
# Print number of each Characters in the file  
# Total number of words 
# Total number of characters 
