def atomicdictionary():
    atomicelements = {'H':'Hydrogen', 'He':'Helium', 'C':'Carbon'}
    atomicelements['Li'] = 'Lithium'

    for i in atomicelements:
        print("Key is ", i, "Value is ", atomicelements[i])
        

    num = len(atomicelements)
    print("Original no of elements is ", num)
    print("Enter the new atomic element")
    answer = "y"

    while answer == "y" or answer == "Y":
        key = input("Enter the atomic symbol: \t")
        value = input("Enter the atom name: \t")
        atomicelements[key] = value
        answer = input("Do you want to enter more elements? yY or nN:\t")
        
    print(atomicelements)
    print("New Number of elements is ", len(atomicelements))

    search = input("Enter the key symbol to search for \t")
    if search in atomicelements:
        print("Yes element %s exists" %search)
        print("Its value is %s" %atomicelements[search])
    else:
        print("I dont have your element")


atomicdictionary()
