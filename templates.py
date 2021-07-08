import models as m

def menu_display():
    print("==== 메뉴 선택 ====")
    print("1. 일정 확인")
    print("2. 일정 입력")
    print("3. 일정 수정")
    print("4. 일정 삭제")
    print("5. 상세 정보")
    print("0. 종료")


def menu_select():
    menu = input("메뉴 선택 : ")
    return menu


def input_display():
    id = input("아이디 : ")
    title = input("제목 : ")
    contents = input("내용 : ")
    date = input_date()
    return m.Todo(id, title, contents, date, False)


def list_display(todos):
    print("===== 전체 일정 =====")
    print("아이디 \t제목\t내용\t날짜\t수행여부")
    
    for todo in todos:
        print(todo.info())


def id_input_display(command):
    id = input("id " + command + " : ")
    return id



def todo_display(todo):
    print("==== 상세 정보 ===")
    print("아이디 \t제목\t내용\t날짜\t수행여부")
    print(todo.info())


def message_display(message):
    print(message)


def update_input_display(id):
    title = input("제목 : ")
    contents =  input("내용 : ")
    date = input_date()
    done = input("수행 여부(y/n) : ")
    while(True):
        if(done == "y"):
            done = True
            break
        elif(done == "n"):
            done = False
            break
        else:
            print("잘못된 입력")
            done = input("수행 여부(y/n) : ")

    return m.Todo(id, title, contents, date, done)


def input_date():

    while(True):
        try:
            year = int(input("연 : "))
            break
        except ValueError as e:
            print("숫자 입력")

    while(True):
        try:
            month = int(input("월 : "))
            if(month<1 or month>12):
              print("잘못된 입력")
            else:
                break
        except ValueError as e:
            print("숫자 입력")
            
    while(True):
        try:
            day = int(input("일 : "))
            if(day<0):
                print("잘못된 입력")
            elif(month==2):
                if(day>28):
                    print("잘못된 입력")
                else:
                    break
            elif(month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
                if(day>31):
                    day = int(input("일 : "))
                else:
                    break
            elif(month==4 or month==6 or month==9 or month==11):
                if(day>30):
                    print("잘못된 입력")
                else:
                    break
            else:
                break
        except ValueError as e:
            print("숫자 입력")
    return str(year) + "/" + str(month) + "/" + str(day) 