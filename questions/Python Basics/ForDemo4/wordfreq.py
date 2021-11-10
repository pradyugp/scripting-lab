atomicelements = ['Oxygen', 'Hydrogen', 'Sulpher', 'Hydrogen', 'Oxygen', 'Hydrogen', 'Helium', 'Hydrogen', 'Helium', 'Carbon', 'Sulpher', 'Gold', 'Silver', 'Silver', 'Silver', 'Silver', 'Gold', 'Gold', 'Hydrogen' ]

print "Number of atomicelements ", len(atomicelements)
print atomicelements 


#for i in atomicelements: 
# print atomicelements.count(i)


# ----- OUTPUT -----
#Number of atomicelements  5
#['Oxygen', 'Hydrogen', 'Sulpher', 'Oxygen', 'Hydrogen']
#2
#2
#1
#2
#2
# ---- PROBLEM -----
#Though answer is correct, it does not make sense!!

# --- SOLUTION -- Use Dictionaries 

mydictionary = {}

for i in atomicelements: 
 mydictionary[i] = atomicelements.count(i)

print mydictionary

# ---- OUTPUT ----
#{'Sulpher': 1, 'Hydrogen': 2, 'Oxygen': 2}

# Sort the elements based on the number of times it occurs in the file 


