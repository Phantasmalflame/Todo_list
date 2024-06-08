
current_list = [] # used to keep track of list that will  written on text file
pogo = [] # used to transfer list file onto current list


todo_list = open("list_file", "r")
new_list = todo_list.readlines()
for l in new_list:
    as_list = l.split(',')
    pogo.append(as_list[0].replace("\n", ""))
current_list = pogo

def todo():
    global current_list  # Allows current list to be used everywhere

    while True:
        response = int(input("what would you like to do? 0. show current list"
                             "1. Add to list 2. Remove 3. show current text file"
                             " list 4. add to text "
                             "file"))
        if response == 0:
            print(current_list)
            continue
        if response == 1: # function to add onto the file
            add_list = input("what would you like to add?")
            current_list.append(add_list)
            continue
        elif response == 2: # deletes items from current list
            remove_list = int(input('''what would you like to remove'''))
            current_list.pop(remove_list)
            continue
        elif response == 3:
            todo_list = open("list_file", "r")
            print(todo_list.read())
            continue
        elif response == 4: #
            todo_list = open("list_file", "w") # opens the file to overwrite with current_list
            todo_list.write("\n".join(current_list))
            todo_list.close()
            print("added to text file")
            g = True
            if g == True:
                pogo = []
                todo_list = open("list_file", "r") # makes the current_list function match the text file
                new_list = todo_list.readlines()
                for l in new_list: # loop for reading text file
                    as_list = l.split(',')
                    pogo.append(as_list[0].replace("\n",""))
                current_list = pogo
            continue
        else:
            quit()


todo()
