FILEPATH="todo.txt"
def get_todos(filepath=FILEPATH):
    """"
    read text file and return a list of todo items
    """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(todos_arg,filepath=FILEPATH):
    """
    write todo items in text file
    :param todos_arg:
    :param filepath:
    :return:
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)