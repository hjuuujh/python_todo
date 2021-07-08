from os import read
import views as v
import models as m
import os.path

def save_file(todos):
    save_file = open("list.dat","w")
    for index, t in enumerate(v.todos):
            save_file.write("{0},{1},{2},{3},{4}\n".format(t.id,t.title,t.contents, t.date, t.done))
    save_file.close()


def init_data_load():

    todos = []
    file_exist = os.path.isfile("list.dat")
    if(file_exist):
        read_file = open("list.dat","r")
        while(True):
            data = read_file.readline()
            if(not data):
                break

            data_list = data.split(',')
            todo = m.Todo(data_list[0],data_list[1],data_list[2],data_list[3],data_list[4])
            todos.append(todo)

            
        read_file.close()
    return todos