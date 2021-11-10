celestial = [
        ['sun', 'sirius', 'vega'], 
        ['Haileys', 'Encke', 'Lexell', 'West'], 
        ['Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus'], 
        ['Milkyway', 'Whirlpool', 'Black Eye', 'Starbust']
] 
print("\nCelestial Objects are ", celestial)
print("Stars are ", celestial[0])
print("Comets are ", celestial[1])
print("Planets are ", celestial[2])
print("Galaxies are ", celestial[3])

# a) Add the Galaxy name 'Andromeda' as the second element in the Galaxy list.Replace the existing element 
galaxytemp = celestial[3]
galaxytemp[1] = 'Andromeda' 
celestial[3] = galaxytemp 
print("\nModified Galaxies are ", celestial[3])

# b) Find the number of planets in your list 
print("\nNumber of planets are ", len(celestial[2]))

# c) What is the name of the last comet in your list? 
cometemp = celestial[1]
print("\nLast comet is ", cometemp[-1])

# d) Intialize the list of planets so that every element reads as 'Earth'  
planetemp = celestial[2] 
i = 0
while i < len(planetemp): 
 planetemp[i] = 'Earth' 
 i = i+1

celestial[2] = planetemp
print("\nReplaced Planets are ", celestial[2])

# e) How many lists that you created in the Celestial list contains the same number of elements? --- TRICKY 

print("\nCelestial Objects are ", celestial) 
print("Stars are ", celestial[0])
print("Comets are ", celestial[1])
print("Planets are ", celestial[2])
print("Galaxies are ", celestial[3])

numberlist = [0,0,0,0]

j=0

while j < len(celestial):
 numberlist[j] = len(celestial[j])
 j = j+1
print(numberlist)


s=0
for j in numberlist:
 
 if numberlist.count(j) > 1: 
    s = s+1

print(s , "\nLists exists that have same number of elements______________________________________", numberlist)

 
 

# f) Create a list that contains the number of satellites for each of the planets in your list 

satellites = [1, 2, 69,62,27]

# g) How many satellites are there in total? 
sattot = 0
for i in satellites:
 sattot = sattot + i

print("\nTotal number of satellites is ", sattot) 

# h) Add star 'Dhruva' to the end of the star list. Print the postion of 'Dhruva' 
startemp = celestial[0]
startemp.append('Dhruva')

celestial[0] = startemp 

print("\nModified Celestial Star List is ", celestial[0])

# i) Remove the second element 'Earth' from the planet list. Replace it with 'Pandroa'. Print the position of 'Pandora'

planetemp = celestial[2] 
planetemp[1]='Pandora'
celestial[2] = planetemp
print("\nModified Celestial Planet list is ", celestial[2])
print("Position of Pandora in Celestial Planet List is ", celestial[2].index('Pandora')+1)

# j) How many 'Earth' elements exist in the planets list? 

print("\nEarth occurs ", celestial[2].count('Earth'), " times")

# k) Create a range list having the exact number of elements as the total number of satellites 

print("\nTotal number of satelites calculated in #g above is ", sattot)
print("Range list is ", range(0,sattot))
 
# l) Create another list 3 stars 

startemp = ['Polaris', 'Canopus', 'Altaire'] 

# m) Combine the two star lists to create a list called 'mystars'
mystars = startemp + celestial[0]
print("\nCombined star list is", mystars) 

#n) Do the following "slicing" 

   #(i) print the 3rd, 4th and 5th element
print("\nPrinting 3rd, 4th hand 5th element:", mystars[2:5])

   #(ii) print all elements starting from the 3rd element 
print("\nprint all elements starting from the 3rd element : ", mystars[2:] )
   #(iii) print from beginning until the 4th element 
print("\nprint from beginning until the 4th element: ", mystars[:4] )

   #(iv) print all 
print("\nprint all: ", mystars[:]) 

# o) Create a new Galaxy list containing all elements of your galaxy list except 'Andromeda' 

newgalaxy = []
for i in celestial[3]:
 if i != 'Andromeda': 
  newgalaxy.append(i)

print(newgalaxy)



