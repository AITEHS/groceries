import pickle



def WriteProgress(filepath, progress):
    with open(filepath, 'wb') as f:
        pickle.dump(progress, f)

def open_data(filepath):
    return open(filepath, 'rb')

def GetProgress(filepath):
    with open_data(filepath) as f:
        try:
            grocery_list.append(pickle.load(f))

            
        except EOFError:
            return None
        
      
grocery_list = []

GetProgress("data/save.pickle")
grocery_list = grocery_list[0]


print(grocery_list)


while True:
    default_text = "1 - view list;\n2 - edit list;\n3 - save & exit; "
    print(default_text)
    choice = int(input("Select option:"))

    if choice == 1:
        print(grocery_list)

    elif choice == 2:
        product = input("What product should be added to the list? ")
        grocery_list.append(product)

    elif choice ==3:
       
        break
WriteProgress('data/save.pickle', grocery_list)
print(grocery_list)
