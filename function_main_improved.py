FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of do-to item."""
    with open(filepath ,'r') as file_local:
        todos_local = file_local.readlines()
    #f'./experiments/todos.txt'
    return todos_local


def write_todos(todos_arg,filepath=FILEPATH):
    """ Write the to-do item list un the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


#print("hello from function")
if __name__=="__main__":
    print(get_todos())