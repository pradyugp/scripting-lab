def atomicdictionary():
 atomicelements = {'H':'Hydrogen', 'He':'Helium', 'Au':'Gold', 'S':'Sulpher'}
 atomicelements['Li'] = 'Lithium' 

# Print the atomic elements 
 for i in atomicelements: 
  print "Key is ", i, "Value is ", atomicelements[i]


 numb = len(atomicelements) 
 print "Original Number of elements is ", numb
 print "Enter the new atomic element" 
 answer = "y" 

#Add elements into the dictionary by interacting with the user 
 while answer =="y" or answer == "Y": 
  key = raw_input("Enter the Atomic Symbol:\t")
  value = raw_input("Enter the Atom Name:\t")
  atomicelements[key] = value
  answer = raw_input("Do you want to enter elements(y/n or Y/N):\t")

 print atomicelements

 print "New Number of elements is ", len(atomicelements) 

# Search for the element that the user gives 
 search = " "
 search = raw_input("Enter the Key Symbol to search for\t")
 

 if search in atomicelements: 
  print "Yes element %s exists" %search 
  print "Its value is: %s" %atomicelements[search]
 else:
  print "Sorry! I dont have your element"

 
