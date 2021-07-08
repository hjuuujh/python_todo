from exception import *
from file_register import *


todos = []

def register(todo):
    global todos

    index = is_exist(todo.id)
    if(index > -1):
        raise DuplicateError(todo.id)
    todos.append(todo)


def update(todo):
    index = is_exist(todo.id)
    if (index == -1):
        raise NotFoundError(todo.id)
    todos[index] = todo
   


def remove(id):
    index = is_exist(id)
    if (index == -1):
        raise NotFoundError(id)
    todos.pop(index)


def get_todo(id):
    index = is_exist(id)
    if (index == -1):
        raise NotFoundError(id)
    return todos[index]


def get_all_todos():
    return todos


def is_exist(id):
    for index, todo in enumerate(todos):
        if todo.id == id :
            return index
    return -1


def save_list():
    save_file(todos)

def load_list():
    global todos
    todos = init_data_load()
