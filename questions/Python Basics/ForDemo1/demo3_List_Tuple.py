# LISTS: All the items belonging to a list can be of different data type. Items are enclosed within [ ]
# List elements and size can be changed,
print("\n *****Demo : List Manipulations")
list1 = [ 'Tintin', 22 , 5.42, 'Belgium', 'Boy Detective' ]
list2 = [45, 'Haddock']

print(list1)          # Prints complete list
print(list1[0])       # Prints first element of the list
print(list1[1:3])     # Prints elements starting from 2nd till 3rd
print(list1[2:])      # Prints elements starting from 3rd element
print(list2 * 2)  # Prints list two times
print(list1 + list2) # Prints concatenated lists

# TUPLES: All the items belonging to a tuple can also be of different data type. Items are enclosed within ( )
# Tuples are "read-only" lists. They are "Immutable". Once created their elements and size cannot be changed,

print("\n *****Demo : Tuple Manipulations")
mytuple = ('Tintin', 22 , 5.42, 'Belgium', 'Boy Detective' )
yourtuple = (45, 'Haddock')

print(mytuple)          # Prints complete tuple
print(mytuple[0])       # Prints first element of the tuple
print(mytuple[1:3])     # Prints elements starting from 2nd till 3rd
print(mytuple[2:])      # Prints elements starting from 3rd element

print("\n Demo: Difference between List and Tuple")
#mytuple[1] = 18 #Invalid - Tuple Elements cannoot be changed
#mytuple[5] = 'Snowy' #Invalid - You cannot add items from a tuple once created 
print("The only way to change the tuple is to replace it completely")
mytuple = ('Archie', 17 , 5.42, 'Riverdale', 'Teenage Student' )
yourtuple = (17, 'Veronica')
mytuple = mytuple + yourtuple
print(mytuple)

yourtuple = yourtuple * 2
print(yourtuple)      # Prints tuple two times
