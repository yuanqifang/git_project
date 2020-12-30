# 时间: 2020/12/27 22:49
# 作者: YUAN
filename='student_txt'
def main():
    while True:
        menu()
        try:
            choice = int(input("请输入需要进行的操作(0-7):"))
            if choice in [0, 1, 2, 3, 4, 5, 6, 7]:
                if choice == 0:
                    answer = input("您确定要退出吗? Y/N:")
                    if answer == 'Y' or answer == 'y':
                        break
                    else:
                        continue
                elif choice == 1:
                    insert()
                elif choice == 2:
                    find()
                elif choice == 3:
                    delete()
                elif choice == 4:
                    update()
                elif choice == 5:
                    sort()
                elif choice == 6:
                    total()
                elif choice == 7:
                    show_student()
        except:
            print('输入无效,请重新输入')
            menu()

def menu():
    print("-------------学生管理系统--------------")
    print("--------------功能菜单----------------")
    print("1. 录入学生信息")
    print("2. 查找学生信息")
    print("3. 删除学生信息")
    print("4. 修改学生信息")
    print("5. 排序")
    print("6. 统计学生人数")
    print("7. 显示所有学生信息")
    print("0. 退出")
    print("--------------------------------------")

def insert():
    student_list = []
    while True:
        id = input('请输入学生id:')
        if not id:
            break
        name = input('请输入学生姓名:')
        if not name:
            break
        try:
            python = int(input('请输入python成绩:'))
            java = int(input('请输入Java成绩:'))
        except:
            print('输入无效,请重新输入')
            continue
        student = {'id': id, 'name': name, 'python': python, 'java': java}
        student_list.append(student)
        answer=input('是否继续添加:Y/N')
        if answer=='Y' or answer=='y':
            continue
        else:
            break
    save(student_list)
    print('学生信息录入完成')

def save(lst):
    try:
        stu_txt=open(filename,'a',encoding='utf-8')
    except:
        stu_txt=open(filename,'w',encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item)+'\n')
    stu_txt.close()

def find():
    student_find=[]
    answer=input('input id/name which do you want to find:')
    stu_list=open(filename,'r',encoding='utf-8')
    student=stu_list.readlines()
    stu_list.close()
    for item in student:
        d=dict(eval(item))
        if answer != '':
            if answer==d['id']:
                student_find.append(d)
            elif answer==d['name']:
                student_find.append(d)
    show(student_find)
    answer2 = input('find continue? Y/N')
    if answer2 == 'y' or answer2 == 'Y':
        find()
    else:
        return

def show(lst):
    if len(lst)==0:
        print('当前无数据,请插入学生信息')
        return
    format_title='{: ^6}\t{: ^12}\t{: ^8}\t{: ^10}\t{: ^6}\t'
    print(format_title.format('id','name','python','java','total'))
    format_data='{: ^6}\t{: ^12}\t{: ^8}\t{: ^10}\t{: ^6}\t'
    for item in lst:
        print(format_data.format(item.get('id'),
                                 item.get('name'),
                                 item.get('python'),
                                 item.get('java'),
                                 int(item.get('python'))+int(item.get('java'))
                                 ))

def show_student():
    show_list=[]
    student = open(filename, 'r', encoding='utf-8')
    student_txt = student.readlines()
    student.close()
    for item in student_txt:#遍历文件中的字典
        show_list.append(eval(item))
    if show_student:
        show(show_list)
    else:
        print('当前学生信息为空,请插入信息')
        menu()



def delete():
    student_list=[]
    answer=input('请输入要删除的学生id或姓名:')
    students=open(filename,'r',encoding='utf-8')
    students_list=students.readlines()
    students.close()
    for item in students_list:#遍历列表中的字符串
        d=eval(item)#将字符串转换为字典
        if answer==d['id']:#遍历字典中的id
            student_list.append(d)  #如果找到相同的id 追加到列表中
        elif answer==d['name']: #遍历字典中的name
            student_list.append(d)  #如果找到相同的name 追加到列表中
    if student_list:
        print('找到该学生的信息为:')
        show(student_list)  #调用show()函数 返回查找出来的列表
        answer2 = input('是否要将其删除? y/n')
        if answer2 == 'y' or answer2 == 'Y':
            student_new = []
            for item in students_list:  # 遍历所有学生信息的字符串
                d = eval(item)  # 将单条学生信息的字符串转换为字典
                student_tmp = []  # 定义一个空列表用于保存单条学生信息
                student_tmp.append(d)
                if student_tmp != student_list:  # 如果和查找出来的学生字典信息不相等则追加到列表中
                    student_new.append(d)  # 得到剩下的学生列表student_new
            with open(filename, 'w', encoding='utf-8') as wfile:  # 以写入模式打开源文件
                wfile.truncate()  # 清空文件
            with open(filename, 'a', encoding='utf-8') as wfile:  # 以追加方式打开文件
                for item in student_new:  # 将所有剩余的学生信息
                    wfile.write(str(item) + '\n')
            print('该学生已删除,当前学生列表为:')
            show_student()
            answer3 = input('delete continue? y/n')
            if answer3 == 'y' or answer3 == 'Y':
                delete()
            elif answer3 == 'N' or answer3 == 'n':
                menu()
            else:
                print('输入错误,返回主菜单')
                menu()
        elif answer2 == 'n' or answer2 == 'N':
            print('撤销操作')
            delete()
        else:
            print('输入错误,请重新查找')
            delete()
    else:
        print('搜索不到该学生信息,请重新输入')
        delete()

'''
    for i, item in enumerate(students_txt):
        if
        print(i)
        student_list.append(eval(item))
    for item in student_list:
        pass
'''

def update():
    answer=input('which student do you want to modify? id/name:')
    students=open(filename,'r',encoding='utf-8')
    students_list=students.readlines()
    students.close()
    student_list=[]
    for item in students_list:#遍历列表中的字符串
        d=eval(item)#将字符串转换为字典
        if answer==d['id']:#遍历字典中的id
            student_list.append(d)  #如果找到相同的id 追加到列表中
        elif answer==d['name']: #遍历字典中的name
            student_list.append(d)  #如果找到相同的name 追加到列表中
    if student_list:
        print('找到该学生的信息为:')
        show(student_list)  #调用show()函数 返回查找出来的列表
        answer2 = input('确定要修改该学生信息吗? y/n')
        if answer2 == 'y' or answer2 == 'Y':
            student_new = []
            for item in students_list:  # 遍历所有学生信息的字符串
                d = eval(item)  # 将单条学生信息的字符串转换为字典
                student_tmp = []  # 定义一个空列表用于保存单条学生信息
                student_tmp.append(d)
                if student_tmp != student_list:  # 如果和查找出来的学生字典信息不相等则追加到列表中
                    student_new.append(d)  # 得到剩下的学生列表student_new
            with open(filename, 'w', encoding='utf-8') as wfile:  # 以写入模式打开源文件
                wfile.truncate()  # 清空文件
            with open(filename, 'a', encoding='utf-8') as wfile:  # 以追加方式打开文件
                for item in student_new:  # 将所有剩余的学生信息
                    wfile.write(str(item) + '\n')
            print('请重新输入该学生信息:')
            student_list = []
            while True:
                id = input('请输入学生id:')
                if not id:
                    break
                name = input('请输入学生姓名:')
                if not name:
                    break
                try:
                    python = int(input('请输入python成绩:'))
                    java = int(input('请输入Java成绩:'))
                except:
                    print('输入无效,请重新输入')
                    continue
                student = {'id': id, 'name': name, 'python': python, 'java': java}
                student_list.append(student)
                save(student_list)
                print('学生信息修改完成')
                answer3 = input('update continue? y/n')
                if answer3 == 'y' or answer3 == 'Y':
                    update()
                elif answer3 == 'N' or answer3 == 'n':
                    break
                else:
                    print('输入错误,返回主菜单')
                    menu()
        elif answer2 == 'n' or answer2 == 'N':
            print('撤销操作')
            update()
        else:
            print('输入错误,请重新查找')
            update()
    else:
        print('搜索不到该学生信息,请重新输入')
        update()

def sort():
    with open(filename,'r',encoding='utf-8') as rfile:
        student_list=rfile.readlines()
    student_new=[]
    for item in student_list:
        d=eval(item)
        student_new.append(d)
    asc_or_desc=input('你希望按升序还是降序排列:1.升序 2.降序 ')
    if asc_or_desc=='1':
        asc_or_desc=False
    elif asc_or_desc=='2':
        asc_or_desc = True
    else:
        print('输入有误,请重新输入')
        sort()
    answer=input('请输入排序依据 1.python成绩 2.java成绩 3.总成绩:')
    if answer=='1':
        student_new.sort(key=lambda x:int(x['python']),reverse=asc_or_desc)
    if answer == '2':
        student_new.sort(key=lambda x:int(x['java']),reverse=asc_or_desc)
    if answer == '3':
        student_new.sort(key=lambda x:int(x['python'])+int(x['java']),reverse=asc_or_desc)
    show(student_new)

def total():
    with open(filename,'r',encoding='utf-8') as rfile:
        student_txt=rfile.readlines()
    print(f'当前系统中共有{len(student_txt)}名学生')


if __name__ == '__main__':
    main()
