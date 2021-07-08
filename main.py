import models as m
import views as v
from exception import DuplicateError, NotFoundError
from templates import *


v.load_list()

while (True):
    menu_display()
    menu = menu_select()

    if(menu == "1"):
        todo_list = v.get_all_todos()
        list_display(todo_list)

    elif(menu == "2"):
        while(True):
            todo = input_display()
            try:
                v.register(todo)
                message_display(todo.id+" 등록 성공")
            except DuplicateError as e:
                message_display(e)
            break

    elif(menu == "3"):
        id = id_input_display("수정")

        try: 
            person = v.get_todo(id)
            new_todo = update_input_display(id)
            v.update(new_todo)
            message_display(id+" 수정성공")
        except NotFoundError as e:
            message_display(e) 

    elif(menu == "4"):
        id = id_input_display("삭제")
        try: 
           v.remove(id)
           message_display(id+" 삭제성공")
        except NotFoundError as e:
            message_display(e) 

    elif(menu == "5"):
        id = id_input_display("검색")
        try:
            todo = v.get_todo(id)
            todo_display(todo)
        except NotFoundError as e:
            message_display(e)
        
    elif(menu == "0"):
        message_display("시스템을 종료합니다.")
        v.save_list()
        break

    else:
        print("잘못된 입력")