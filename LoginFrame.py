import re
from tkinter import *
# from CoCenter import *
from tkinter import messagebox
import pyodbc
from CoCenter import CoCenter


def getVal(s):
    tmp = s.replace('(', '')
    tmp = tmp.replace(')', '')
    tmp = tmp.replace('[', '')
    tmp = tmp.replace(']', '')
    tmp = tmp.replace('\'', '')
    tmp = tmp.replace(',', '')
    tmp = tmp.replace(' ', '')
    return tmp


class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__()
        frame = Frame(master)
        frame.pack()
        self.root = master
        self.lab1 = Label(frame, text="工号:", pady=10)
        self.lab1.grid(row=0, column=0, sticky=W)
        self.ent1 = Entry(frame)
        self.ent1.grid(row=0, column=1, columnspan=2, sticky=W)
        self.lab2 = Label(frame, text="密码:", pady=10)
        self.lab2.grid(row=1, column=0, sticky=W)
        self.ent2 = Entry(frame, show="*")
        self.v = IntVar()
        self.v.set(0)
        self.ent2.grid(row=1, column=1, columnspan=2, sticky=W)
        self.radiobutton = Radiobutton(frame, text="司机", variable=self.v, value=0)
        self.radiobutton.grid(row=2, column=0, sticky=E + W)
        self.radiobutton2 = Radiobutton(frame, text="路队长", variable=self.v, value=1)
        self.radiobutton2.grid(row=2, column=1, sticky=E + W)
        self.radiobutton3 = Radiobutton(frame, text="队长", variable=self.v, value=2)
        self.radiobutton3.grid(row=2, column=2, sticky=E + W)
        self.radiobutton3 = Radiobutton(frame, text="管理员", variable=self.v, value=3)
        self.radiobutton3.grid(row=2, column=3, sticky=E + W)
        self.button = Button(frame, text="登陆", command=self.ButtonClick)
        self.button.grid(row=3, column=0, padx=10, ipadx=10, sticky=E + W)
        self.button2 = Button(frame, text="退出", command=frame.quit)
        self.button2.grid(row=3, column=2, padx=10, ipadx=10, sticky=E + W)
    
    def ButtonClick(self):
        job_number = self.ent1.get()  # 工号
        password = self.ent2.get()
        if self.v.get() == 0:
            self.login(job_number, password, '司机')
        elif self.v.get() == 1:
            self.login(job_number, password, '路队长')
        elif self.v.get() == 2:
            self.login(job_number, password, '队长')
        else:
            self.login(job_number, password, '管理员')
    
    def login(self, job_number, password, position):
        if position != '管理员':
            if not job_number:
                messagebox.showinfo('登录失败', '请输入工号！')
            elif not password:
                messagebox.showinfo('登录失败', '请输入密码！')
            else:
                cnxn_admin = pyodbc.connect('DRIVER={SQL Server};SERVER=LAPTOP-38ACSOA2;DATABASE=公交管理系统;UID=sa;PWD=')
                cursor = cnxn_admin.cursor()
                cursor.execute(
                    "SELECT 用户信息.工号,密码,职位,成员信息.姓名 FROM 用户信息,成员信息 WHERE 用户信息.工号=成员信息.工号 AND 用户信息.工号=" + job_number)
                users_info = cursor.fetchall()
                if not users_info:
                    messagebox.showinfo('登录失败', '用户名不存在！')
                elif password not in re.findall(r'\d+', users_info[0][1]):
                    messagebox.showinfo('登录失败', '密码错误！')
                elif position not in users_info[0]:
                    messagebox.showinfo('登录失败', '职位选择错误！')
                else:
                    name = users_info[0][-1]
                    cnxn = pyodbc.connect(
                        'DRIVER={SQL Server};SERVER=LAPTOP-38ACSOA2;DATABASE=公交管理系统;UID=' + name + ';PWD=' + password)
                    messagebox.showinfo('登录成功',
                                        '欢迎使用本系统！用户 ' + users_info[0][
                                            -1] + '\n' + '工号：' + job_number + '  职位：' + position)
                    # job_number: 工号  password: 密码  name: 姓名  position: 职位
                    w = CoCenter(job_number, password, name, position, cnxn_admin, cnxn)
        else:
            if job_number != 'sa':
                messagebox.showinfo('登录失败', '管理员用户名错误！')
            else:
                try:
                    cnxn_admin = pyodbc.connect(
                        'DRIVER={SQL Server};SERVER=LAPTOP-38ACSOA2;DATABASE=公交管理系统;UID=sa;PWD=')
                    cursor = cnxn_admin.cursor()
                except pyodbc.InterfaceError:
                    messagebox.showinfo('登录失败', '管理员密码错误！')
                else:
                    messagebox.showinfo('登录成功', '欢迎使用本系统！')
                    w = CoCenter(job_number, password, name='', position='admin', cnxn_admin=cnxn_admin,
                                 cnxn=cnxn_admin)
    
    def quit(self):
        messagebox.showinfo('提示', '退出系统成功！')
        self.destroy()
        frame.quit
