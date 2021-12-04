import tkinter as tk
import Sql
from MyDialog import MyDialog
from AdDialog import AdDialog
from tkinter import messagebox


class CoCenter(tk.Toplevel):
    def __init__(self, job_number, password, name, position, cnxn_admin, cnxn):
        super().__init__()
        self.job_number = job_number
        self.position = position
        self.name = name
        self.password = password
        self.cnxn_admin = cnxn_admin
        self.cnxn = cnxn
        
        frame = tk.Frame(self)
        frame.pack()
        self.title("用户 " + self.name + " 欢迎您！")
        if position == '司机':
            self.button = tk.Button(frame,
                                    text="更改登陆密码", pady=10, command=self.UpdatePassword)
            self.button.grid(row=0, column=0, padx=10)
            self.button1 = tk.Button(frame,
                                     text="查看个人信息", pady=10, command=self.CheckInfo)
            self.button1.grid(row=0, column=1, padx=10)
            self.exit = tk.Button(frame, text="退出登录", command=self.cancel)
            self.exit.grid(row=1, column=1)
            self.geometry('300x80')
        elif position == '路队长':
            self.button = tk.Button(frame,
                                    text="更改登陆密码", pady=10, command=self.UpdatePassword)
            self.button.grid(row=0, column=0, padx=10)
            self.button1 = tk.Button(frame,
                                     text="查看路线成员信息", pady=10, command=self.CheckInfo)
            self.button1.grid(row=0, column=1, padx=10)
            self.exit = tk.Button(frame, text="退出登录", command=self.cancel)
            self.exit.grid(row=1, column=1)
            self.geometry('300x80')
        else:
            self.button = tk.Button(frame,
                                    text="更改登陆密码", pady=10, command=self.UpdatePassword)
            self.button.grid(row=0, column=0, padx=10)
            self.button1 = tk.Button(frame,
                                     text="查看车队成员信息", pady=10, command=self.CheckInfo)
            self.button1.grid(row=0, column=1, padx=10)
            self.exit = tk.Button(frame, text="退出登录", command=self.cancel)
            self.exit.grid(row=1, column=1)
            self.geometry('300x80')
    
    def cancel(self):
        messagebox.showinfo('提示', '退出登录！')
        self.destroy()
    
    def UpdatePassword(self):
        w1 = MyDialog(self.job_number, self.password, self.name, self.position, function=1, cnxn_admin=self.cnxn_admin,
                      cnxn=self.cnxn)
    
    def CheckInfo(self):
        w1 = MyDialog(self.job_number, self.password, self.name, self.position, function=2, cnxn_admin=self.cnxn_admin,
                      cnxn=self.cnxn)
