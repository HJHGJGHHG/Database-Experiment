import tkinter as tk
from MyDialog import MyDialog, CheckLineInfo, CheckBusInfo
from AdminDialog import AdminUpdatePassword, AdminCheckUserInfo
from tkinter import messagebox
from PunishmentDialog import PunishMentCenter


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
        if position == '司机':
            self.title("用户 " + self.name + " 欢迎您！")
            self.button = tk.Button(frame,
                                    text="更改登陆密码", pady=10, command=self.UpdatePassword)
            self.button.grid(row=0, column=0, padx=10)
            self.button1 = tk.Button(frame,
                                     text="查看个人信息", pady=10, command=self.CheckInfo)
            self.button1.grid(row=0, column=1, padx=10)
            self.button1 = tk.Button(frame,
                                     text="查看所属线路下公交信息", pady=10, command=self.CheckBusInfo)
            self.button1.grid(row=1, column=0, padx=10)
            self.button1 = tk.Button(frame,
                                     text="查看违章信息", pady=10, command=self.CheckPunishMentInfo)
            self.button1.grid(row=1, column=1, padx=10)
            self.exit = tk.Button(frame, text="退出登录", command=self.cancel)
            self.exit.grid(row=2, column=0)
            self.geometry('300x150')
        elif position == '路队长':
            self.title("用户 " + self.name + " 欢迎您！")
            self.button = tk.Button(frame,
                                    text="更改登陆密码", pady=10, command=self.UpdatePassword)
            self.button.grid(row=0, column=0, padx=10)
            self.button1 = tk.Button(frame,
                                     text="查看线路成员信息", pady=10, command=self.CheckInfo)
            self.button1.grid(row=0, column=1, padx=10)
            self.button1 = tk.Button(frame,
                                     text="录入线路成员信息", pady=10, command=self.InsertInfo)
            self.button1.grid(row=1, column=0, padx=10)
            self.button1 = tk.Button(frame,
                                     text="查看线路下公交信息", pady=10, command=self.CheckBusInfo)
            self.button1.grid(row=1, column=1, padx=10)
            self.button1 = tk.Button(frame,
                                     text="查看违章信息", pady=10, command=self.CheckPunishMentInfo)
            self.button1.grid(row=2, column=0, padx=10)
            self.exit = tk.Button(frame, text="退出登录", command=self.cancel)
            self.exit.grid(row=2, column=1)
            self.geometry('500x200')
        elif position == '队长':
            self.title("用户 " + self.name + " 欢迎您！")
            self.button = tk.Button(frame,
                                    text="更改登陆密码", pady=10, command=self.UpdatePassword)
            self.button.grid(row=0, column=0, padx=10)
            self.button1 = tk.Button(frame,
                                     text="查看车队成员信息", pady=10, command=self.CheckInfo)
            self.button1.grid(row=0, column=1, padx=10)
            self.button1 = tk.Button(frame,
                                     text="录入车队成员信息", pady=10, command=self.InsertInfo)
            self.button1.grid(row=1, column=0, padx=10)
            self.button1 = tk.Button(frame,
                                     text="查看车队辖下线路信息", pady=10, command=self.CheckLineInfo)
            self.button1.grid(row=1, column=1, padx=10)
            self.button1 = tk.Button(frame,
                                     text="查看车队下公交信息", pady=10, command=self.CheckBusInfo)
            self.button1.grid(row=2, column=0, padx=10)
            self.button1 = tk.Button(frame,
                                     text="查看违章信息", pady=10, command=self.CheckPunishMentInfo)
            self.button1.grid(row=2, column=1, padx=10)
            self.exit = tk.Button(frame, text="退出登录", command=self.cancel)
            self.exit.grid(row=3, column=1)
            self.geometry('500x200')
        else:
            self.title("欢迎您管理员！")
            self.button = tk.Button(frame,
                                    text="更改登陆密码", pady=10, command=self.AdminUpdatePassword)
            self.button.grid(row=0, column=0, padx=10)
            self.button1 = tk.Button(frame,
                                     text="查看成员信息", pady=10, command=self.AdminCheckInfo)
            self.button1.grid(row=0, column=1, padx=10)
            self.exit = tk.Button(frame, text="退出登录", command=self.cancel)
            self.exit.grid(row=1, column=1)
            self.geometry('300x120')
    
    def cancel(self):
        messagebox.showinfo('提示', '退出登录！')
        self.destroy()
    
    def UpdatePassword(self):
        w1 = MyDialog(self.job_number, self.password, self.name, self.position, function=1, cnxn_admin=self.cnxn_admin,
                      cnxn=self.cnxn)
    
    def CheckInfo(self):
        w1 = MyDialog(self.job_number, self.password, self.name, self.position, function=2, cnxn_admin=self.cnxn_admin,
                      cnxn=self.cnxn)
    
    def InsertInfo(self):
        w1 = MyDialog(self.job_number, self.password, self.name, self.position, function=3, cnxn_admin=self.cnxn_admin,
                      cnxn=self.cnxn)
    
    def CheckLineInfo(self):
        w1 = CheckLineInfo(self.job_number, self.name, self.position, cnxn=self.cnxn)
    
    def CheckBusInfo(self):
        w1 = CheckBusInfo(self.job_number, self.name, self.position, cnxn=self.cnxn)
    
    def CheckPunishMentInfo(self):
        w1 = PunishMentCenter(self.job_number, self.name, self.position, cnxn=self.cnxn)
    
    def AdminUpdatePassword(self):
        w1 = AdminUpdatePassword(self.job_number, self.password, cnxn_admin=self.cnxn_admin)
    
    def AdminCheckInfo(self):
        w1 = AdminCheckUserInfo(cnxn_admin=self.cnxn_admin)
