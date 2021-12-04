import xlwt
import pyodbc
import tkinter as tk
from Sql import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from prettytable import PrettyTable


class MyDialog(tk.Toplevel):
    def __init__(self,
                 job_number: str,
                 password: str,
                 name: str,
                 position: str,
                 function: int,
                 cnxn_admin,
                 cnxn
                 ):
        """
        :param job_number: 工号
        :param password:密码
        :param name:姓名
        :param position: 职位
        :param function: 功能
        """
        super().__init__()
        self.job_number = job_number
        self.position = position
        self.function = function
        self.name = name
        self.password = password
        
        self.cnxn_admin = cnxn_admin
        self.cnxn = cnxn
        
        self.frame = tk.Frame(self)
        self.frame.pack()
        if function == 1:  # 修改密码
            self.title("修改密码")
            self.newp = tk.StringVar()
            self.lab1 = tk.Label(self.frame, text="请输入新密码:", pady=10)
            self.lab1.grid(row=0, column=0)
            self.ent1 = tk.Entry(self.frame, textvariable=self.newp)
            self.ent1.grid(row=0, column=1)
            self.bo1 = tk.Button(self.frame, text="确认", command=self.confirm)
            self.bo1.grid(row=1, column=0)
            self.exit = tk.Button(self.frame, text="取消", command=self.cancel)
            self.exit.grid(row=1, column=1)
            self.geometry('300x80')
        if function == 2:  # 查看个人信息
            if self.position == '队长':  # 队长可以查看自己车队所有成员的个人信息
                self.title("查询车队成员信息")
                sql = "SELECT * FROM 成员信息 WHERE 车队号 = (SELECT 车队号 FROM 成员信息 WHERE 姓名='" + self.name + "');"
                data = Sql(self.cnxn, sql, isSelect=True)
                self.table = PrettyTable(["工号", "姓名", "性别", "年龄",
                                          "入职时间", "车队号", "线路号", "职位"])
                self.table.add_rows(data)
                self.lab1 = tk.Label(self.frame, text=self.table, pady=10)
                self.lab1.grid(row=0, column=0)
                self.bo1 = tk.Button(self.frame, text="修改信息", command=self.UpdateInfo)
                self.bo1.grid(row=1, column=0)
                self.exit = tk.Button(self.frame, text="确认", command=self.cancel2)
                self.exit.grid(row=1, column=2)
                self.bo2 = tk.Button(self.frame, text="刷新", command=self.refresh)
                self.bo2.grid(row=1, column=1)
                self.geometry('500x300')
            elif self.position == '路队长':  # 路队长可以看到同一条线路的人员信息
                self.title("查询路线成员信息")
                sql = "SELECT 信息2.* FROM 成员信息 信息1,成员信息 信息2 WHERE 信息1.工号=" + self.job_number + " AND 信息1.车队号=信息2.车队号 AND 信息1.线路号=信息2.线路号;"
                data = Sql(self.cnxn, sql, isSelect=True)
                self.table = PrettyTable(["工号", "姓名", "性别", "年龄",
                                          "入职时间", "车队号", "线路号", "职位"])
                self.table.add_rows(data)
                self.lab1 = tk.Label(self.frame, text=self.table, pady=10)
                self.lab1.grid(row=0, column=0)
                self.bo1 = tk.Button(self.frame, text="修改信息", command=self.UpdateInfo)
                self.bo1.grid(row=1, column=0)
                self.exit = tk.Button(self.frame, text="确认", command=self.cancel2)
                self.exit.grid(row=1, column=2)
                self.bo2 = tk.Button(self.frame, text="刷新", command=self.refresh)
                self.bo2.grid(row=1, column=1)
                self.geometry('500x300')
            else:  # 司机只能查看自己的信息
                self.title("查询个人信息")
                sql = "SELECT * FROM 成员信息 WHERE 工号=" + self.job_number + ";"
                data = Sql(self.cnxn, sql, isSelect=True)
                self.table = PrettyTable(["工号", "姓名", "性别", "年龄",
                                          "入职时间", "车队号", "线路号", "职位"])
                self.table.add_rows(data)
                self.lab1 = tk.Label(self.frame, text=self.table, pady=10)
                self.lab1.grid(row=0, column=0)
                self.bo1 = tk.Button(self.frame, text="修改信息", command=self.UpdateInfo)
                self.bo1.grid(row=1, column=0)
                self.exit = tk.Button(self.frame, text="确认", command=self.cancel2)
                self.exit.grid(row=1, column=2)
                self.bo2 = tk.Button(self.frame, text="刷新", command=self.refresh)
                self.bo2.grid(row=1, column=1)
                self.geometry('500x300')
    
    def confirm(self):
        new_password = str(self.newp.get())
        sql = 'ALTER LOGIN ' + self.name + ' WITH PASSWORD=' + "'" + new_password + "'" + ';'
        Sql(self.cnxn_admin, sql, isSelect=False)
        sql = "UPDATE 用户信息 SET 密码='" + new_password + "' WHERE 用户名 IN (SELECT 工号 FROM 成员信息 WHERE 姓名='" + self.name + "');"
        Sql(self.cnxn, sql, isSelect=False)
        messagebox.showinfo('提示', '修改成功！\n 新密码为：' + new_password)
        self.destroy()
    
    def UpdateInfo(self):
        w1 = UpdateInfo(self.cnxn, self.job_number, self.position)
    
    def refresh(self):
        sql = "SELECT 职位 FROM 成员信息 WHERE 工号=" + self.job_number + ";"
        self.position = Sql(self.cnxn, sql, isSelect=True)[0][0]
        if self.position == '队长':  # 仍为队长
            self.title("查询车队成员信息")
            sql = "SELECT * FROM 成员信息 WHERE 车队号 = (SELECT 车队号 FROM 成员信息 WHERE 姓名='" + self.name + "');"
            data = Sql(self.cnxn, sql, isSelect=True)
            self.table = PrettyTable(["工号", "姓名", "性别", "年龄",
                                      "入职时间", "车队号", "线路号", "职位"])
            self.table.add_rows(data)
            self.lab1 = tk.Label(self.frame, text=self.table, pady=10)
            self.lab1.grid(row=0, column=0)
        if self.position == '路队长':
            self.title("查询路线成员信息")
            sql = "SELECT 信息2.* FROM 成员信息 信息1,成员信息 信息2 WHERE 信息1.工号=" + self.job_number + " AND 信息1.车队号=信息2.车队号 AND 信息1.线路号=信息2.线路号;"
            data = Sql(self.cnxn, sql, isSelect=True)
            self.table = PrettyTable(["工号", "姓名", "性别", "年龄",
                                      "入职时间", "车队号", "线路号", "职位"])
            self.table.add_rows(data)
            self.lab1 = tk.Label(self.frame, text=self.table, pady=10)
            self.lab1.grid(row=0, column=0)
        else:
            self.title("查询个人信息")
            sql = "SELECT * FROM 成员信息 WHERE 工号=" + self.job_number + ";"
            data = Sql(self.cnxn, sql, isSelect=True)
            self.table = PrettyTable(["工号", "姓名", "性别", "年龄",
                                      "入职时间", "车队号", "线路号", "职位"])
            self.table.add_rows(data)
            self.lab1 = tk.Label(self.frame, text=self.table, pady=10)
            self.lab1.grid(row=0, column=0)
    
    def cancel(self):
        messagebox.showinfo('提示', '操作取消！')
        self.destroy()
    
    def cancel2(self):
        self.destroy()


class UpdateInfo(tk.Toplevel):
    def __init__(self, cnxn, job_number, position):
        super().__init__()
        self.cnxn = cnxn
        self.job_number = job_number
        self.position = position
        
        self.frame = tk.Frame(self)
        self.frame.pack()
        
        self.title("修改信息")
        self.lab1 = tk.Label(self.frame, text="请输入需要修改信息人员的工号:", pady=10)
        self.lab1.pack(side=TOP, padx=5)
        self.ent1 = tk.Entry(self.frame)
        self.ent1.pack(side=TOP, padx=5)
        self.lab2 = tk.Label(self.frame, text="请选择要修改的列:", pady=10)
        self.lab2.pack(side=TOP, padx=5)
        self.value = StringVar()
        values = ['年龄', '车队号', '线路号', '职位']
        self.value.set('年龄')
        self.combobox = ttk.Combobox(
            master=self.frame,  # 父容器
            height=10,  # 高度,下拉显示的条目数量
            width=5,  # 宽度
            state='readonly',  # 设置状态 normal(可选可输入)、readonly(只可选)、 disabled
            cursor='arrow',  # 鼠标移动时样式 arrow, circle, cross, plus...
            # font=('', 20),  # 字体
            textvariable=self.value,  # 通过StringVar设置可改变的值
            values=values,  # 设置下拉框的选项
        )
        
        self.combobox.pack(side=TOP, padx=5)
        self.lab2 = tk.Label(self.frame, text="请输入修改后的新值:", pady=10)
        self.lab2.pack(side=TOP, padx=5)
        self.ent2 = tk.Entry(self.frame)
        self.ent2.pack(side=TOP, padx=5)
        self.lab2 = tk.Label(self.frame, text="请注意！不要输入引号！正确输入示例：L01", pady=10)
        self.lab2.pack(side=TOP, padx=5)
        self.bo1 = tk.Button(self.frame, text="确认", command=self.confirm)
        self.bo1.pack(padx=5)
        self.exit = tk.Button(self.frame, text="取消", command=self.cancel)
        self.exit.pack(padx=5)
        
        self.geometry('500x400')
    
    def confirm(self):
        # 使用var.get()来获得目前选项内容
        self.col = self.value.get()  # 需要修改那一列
        self.update_job_number = self.ent1.get()  # 需要修改信息的人员工号
        self.update_value = self.ent2.get()  # 新值
        if self.update_job_number == '' or self.update_value == '':
            messagebox.showinfo('提示', '操作失败！\n请检查是否填写了所有项并选择了更改列！')
            self.destroy()
        
        # data: 有权限修改的工号集合
        if self.position == '队长':
            sql = "SELECT 工号 FROM 成员信息 WHERE 车队号 = (SELECT 车队号 FROM 成员信息 WHERE 工号=" + self.job_number + ");"
            data = [item[0] for item in Sql(self.cnxn, sql, isSelect=True)]
        elif self.position == '路队长':
            sql = "SELECT 信息1.工号 FROM 成员信息 信息1,成员信息 信息2 WHERE 信息1.工号=" + self.job_number + " AND 信息1.车队号=信息2.车队号 AND 信息1.线路号=信息2.线路号;"
            data = [item[0] for item in Sql(self.cnxn, sql, isSelect=True)]
        else:
            data = [self.job_number]
        flag = False
        for item in data:
            if self.update_job_number in item:
                flag = True
                break
        if not flag:
            messagebox.showinfo('提示', '操作失败！\n工号不存在或者超出权限！')
            self.destroy()
        elif self.col == '年龄':
            sql = "UPDATE 成员信息 SET 年龄=" + self.update_value + " WHERE 工号=" + self.update_job_number + ";"
            try:
                Sql(self.cnxn, sql, isSelect=False)
                messagebox.showinfo('提示', '操作成功！')
            except pyodbc.IntegrityError:
                messagebox.showinfo('提示', '操作失败！\n年龄需在18至50之间！')
        elif self.col == '线路号':
            sql = "SELECT 线路号 FROM 线路表 WHERE 车队号 IN (SELECT 车队号 FROM 成员信息 WHERE 工号=" + self.update_job_number + ");"
            inLine = False
            for line in Sql(self.cnxn, sql, isSelect=True):
                if self.update_value in line[0]:
                    inLine = True
                    break
            if not inLine:
                messagebox.showinfo('提示', '操作失败！\n线路号修改只能在同一车队下完成！\n跨车队线路号修改请先修改车队号。')
            else:
                sql = "SELECT 职位 FROM 成员信息 WHERE 工号=" + self.update_job_number + ";"
                position = Sql(self.cnxn, sql, isSelect=True)[0][0]
                if position == '队长':
                    messagebox.showinfo('提示', '操作失败！队长不属于任何一条线路！')
                elif position == '司机':
                    sql = "UPDATE 成员信息 SET 线路号='" + self.update_value + "' WHERE 工号=" + self.update_job_number + ";"
                    Sql(self.cnxn, sql, isSelect=False)
                    messagebox.showinfo('提示', '操作成功！')
                else:
                    # 更改的人员职位为路队长，则变更到新的线路后职位将变为司机，同时提示原线路缺少路队长。
                    sql = "UPDATE 成员信息 SET 线路号='" + self.update_value + "',职位=N'司机' WHERE 工号=" + self.update_job_number + ";"
                    Sql(self.cnxn, sql, isSelect=False)
                    
                    messagebox.showinfo('提示', '操作成功！\n请注意，变更后职位为司机且原线路缺少一名路队长！')
        elif self.col == '职位':
            # 司机改为路队长、队长：需先判断是否存在路队长或司机
            # 路队长改为司机：可以
            # 队长改为司机：可以，改为路队长须先判断有无路队长
            pass
        else:
            pass
        # ['年龄', '车队号', '线路号', '职位']
        
        self.destroy()
    
    def cancel(self):
        messagebox.showinfo('提示', '操作取消！')
        self.destroy()
