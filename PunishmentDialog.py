import pyodbc
import tkinter as tk
import pandas as pd
from Sql import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from prettytable import PrettyTable

PUNISHMENT_TYPE = ['违反交通信号灯规则', '未礼让行人', '超速', '实线变道']


class PunishMentCenter(tk.Toplevel):
    def __init__(self,
                 job_number: str,
                 name: str,
                 position: str,
                 cnxn
                 ):
        """
        查看某名司机违章信息
        :param job_number: 工号
        :param name:姓名
        :param position: 职位
        """
        super().__init__()
        self.job_number = job_number
        self.position = position
        self.name = name
        
        self.cnxn = cnxn
        
        self.frame = tk.Frame(self)
        self.frame.pack()
        self.title("违章信息")
        self.bo1 = tk.Button(self.frame, text="查询违章信息", command=self.CheckPunishMentInfo)
        self.bo1.grid(row=1, column=0)
        self.bo1 = tk.Button(self.frame, text="录入违章信息", command=self.InsertPunishMentInfo)
        self.bo1.grid(row=1, column=1)
        self.bo1 = tk.Button(self.frame, text="删除违章信息", command=self.DeletePunishMentInfo)
        self.bo1.grid(row=2, column=0)
        self.exit = tk.Button(self.frame, text="返回", command=self.cancel)
        self.exit.grid(row=2, column=1)
        self.geometry('200x150')
    
    def cancel(self):
        self.destroy()
    
    def CheckPunishMentInfo(self):
        w1 = CheckPunishMentInfo(self.job_number, self.name, self.position, self.cnxn)
    
    def InsertPunishMentInfo(self):
        w1 = InsertPunishMentInfo(self.job_number, self.name, self.position, self.cnxn)
    
    def DeletePunishMentInfo(self):
        w1 = DeletePunishMentInfo(self.job_number, self.name, self.position, self.cnxn)


class InsertPunishMentInfo(tk.Toplevel):
    def __init__(self,
                 job_number: str,
                 name: str,
                 position: str,
                 cnxn
                 ):
        """
        录入某名司机违章信息
        :param job_number: 工号
        :param name:姓名
        :param position: 职位
        """
        super().__init__()
        self.job_number = job_number
        self.position = position
        self.name = name
        
        self.cnxn = cnxn
        
        self.frame = tk.Frame(self)
        self.frame.pack()
        self.title("录入违章信息")
        self.lab1 = tk.Label(self.frame, text="请输入违章人员的工号:", pady=10)
        self.lab1.pack(side=TOP, padx=5)
        self.ent1 = tk.Entry(self.frame)
        self.ent1.pack(side=TOP, padx=5)
        self.lab2 = tk.Label(self.frame, text="请选择违章类型:", pady=10)
        self.lab2.pack(side=TOP, padx=5)
        self.value = StringVar()
        values = PUNISHMENT_TYPE
        self.value.set('违反交通信号灯规则')
        self.combobox = ttk.Combobox(
            master=self.frame,  # 父容器
            height=10,  # 高度,下拉显示的条目数量
            width=5,  # 宽度
            state='normal',  # 设置状态 normal(可选可输入)、readonly(只可选)、 disabled
            cursor='arrow',  # 鼠标移动时样式 arrow, circle, cross, plus...
            # font=('', 20),  # 字体
            textvariable=self.value,  # 通过StringVar设置可改变的值
            values=values,  # 设置下拉框的选项
        )
        self.combobox.pack(side=TOP, padx=5)
        
        self.lab3 = tk.Label(self.frame, text="违章所在线路:", pady=10)
        self.lab3.pack(side=TOP, padx=5)
        self.ent3 = tk.Entry(self.frame)
        self.ent3.pack(side=TOP, padx=5)
        
        self.lab6 = tk.Label(self.frame, text="违章车牌号:", pady=10)
        self.lab6.pack(side=TOP, padx=5)
        self.ent6 = tk.Entry(self.frame)
        self.ent6.pack(side=TOP, padx=5)
        
        self.lab4 = tk.Label(self.frame, text="违章时间:", pady=10)
        self.lab4.pack(side=TOP, padx=5)
        self.ent4 = tk.Entry(self.frame)
        self.ent4.pack(side=TOP, padx=5)
        self.lab5 = tk.Label(self.frame, text="违章时间请用 - 号分隔。正确输入示例：2021-12-20", pady=10)
        self.lab5.pack(side=TOP, padx=5)
        
        self.bo1 = tk.Button(self.frame, text="确认", command=self.confirm)
        self.bo1.pack(padx=5)
        self.exit = tk.Button(self.frame, text="取消", command=self.cancel)
        self.exit.pack(padx=5)
        
        self.geometry('500x450')
    
    def cancel(self):
        messagebox.showinfo('提示', '操作取消！')
        self.destroy()
    
    def confirm(self):
        punishment_job_number = self.ent1.get()
        punishment_type = self.value.get()
        xianlu = self.ent3.get()
        shijian = self.ent4.get()
        chepai = self.ent6.get()
        # 获得有权限添加违章信息的工号集合
        if self.position == '司机':
            messagebox.showinfo('提示', '司机无录入信息权限！')
            self.destroy()
            return
        elif self.position == '路队长':
            sql = "SELECT 信息1.工号 FROM 成员信息 信息1,成员信息 信息2 WHERE 信息1.工号=" + self.job_number + " AND 信息1.车队号=信息2.车队号 AND 信息1.线路号=信息2.线路号;"
            data = [item[0] for item in Sql(self.cnxn, sql, isSelect=True)]
        else:
            sql = "SELECT 工号 FROM 成员信息 WHERE 车队号 = (SELECT 车队号 FROM 成员信息 WHERE 工号=" + self.job_number + ");"
            data = [item[0] for item in Sql(self.cnxn, sql, isSelect=True)]
        
        if not punishment_job_number:
            messagebox.showinfo('提示', '违章人员工号不能为空！')
            self.destroy()
            return
        else:
            if punishment_job_number not in data:
                messagebox.showinfo('提示', '违章人员工号不存在或超出权限！')
                self.destroy()
                return
            elif punishment_job_number == self.job_number and self.position == '队长':
                messagebox.showinfo('提示', '队长无违章记录！')
                self.destroy()
                return
        
        if not punishment_type:
            messagebox.showinfo('提示', '请选择或输入违章类型！')
            self.destroy()
            return
        elif punishment_type not in PUNISHMENT_TYPE:
            PUNISHMENT_TYPE.append(punishment_type)
        
        if not chepai:
            messagebox.showinfo('提示', '车牌号不能为空！')
            self.destroy()
            return
        
        if not xianlu:
            messagebox.showinfo('提示', '违章所在线路不能为空！')
            self.destroy()
            return
        else:
            if self.position == '路队长':
                sql = "SELECT 线路号 FROM 成员信息 WHERE 工号={0};".format(self.job_number)
            else:
                sql = "SELECT DISTINCT 线路号 FROM 线路成员信息 WHERE 车队号 = (SELECT 车队号 FROM 成员信息 WHERE 工号={0});".format(
                    self.job_number)
            all_xianlu = [item[0] for item in Sql(self.cnxn, sql, isSelect=True)]
            if xianlu not in all_xianlu:
                messagebox.showinfo('提示', '操作失败！\n线路号不存在或超出权限！')
                self.destroy()
                return
        
        if not shijian:
            messagebox.showinfo('提示', '违章日期不能为空！')
            self.destroy()
            return
        else:
            shijian_split = shijian.split('-')
            if len(shijian_split) != 3 or not (1 <= int(shijian_split[1]) <= 12) or not (
                    1 < int(shijian_split[2]) <= 31):
                messagebox.showinfo('提示', '操作失败\n请检查违章日期是否输入正确！')
                self.destroy()
                return
        
        # 获得新违章编号
        sql = "SELECT 违章编号 FROM 违章记录表;"
        data = [item[0] for item in Sql(self.cnxn, sql, isSelect=True)]
        data = sorted(data, key=lambda x: int(x))
        if data == []:
            new_punishment_id = 1
        else:
            new_punishment_id = int(data[-1]) + 1
        
        sql = "INSERT INTO 违章记录表 VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}');".format(new_punishment_id,
                                                                                                   punishment_job_number,
                                                                                                   punishment_type,
                                                                                                   xianlu,
                                                                                                   shijian,
                                                                                                   self.job_number,
                                                                                                   chepai)
        Sql(self.cnxn, sql, isSelect=False)
        messagebox.showinfo('提示', '操作成功\n成功录入工号为{}的人员违章信息！'.format(punishment_job_number))
        self.destroy()
        return


class CheckPunishMentInfo(tk.Toplevel):
    def __init__(self,
                 job_number: str,
                 name: str,
                 position: str,
                 cnxn
                 ):
        """
        查看违章信息
        :param job_number: 工号
        :param name:姓名
        :param position: 职位
        """
        super().__init__()
        self.job_number = job_number
        self.position = position
        self.name = name
        
        self.cnxn = cnxn
        
        self.frame = tk.Frame(self)
        self.frame.pack()
        self.title("查询违章信息")
        
        # 司机只能查看个人的违章信息，路队长可以查看线路上成员的违章信息，队长可以查看车队成员违章信息
        if self.position == '司机':
            self.lab1 = tk.Label(self.frame, text="用户 {0} 的违章信息如下".format(self.name), pady=10)
            self.lab1.grid(row=0, column=0)
            sql = "SELECT * FROM 违章记录表 WHERE 违章者工号={};".format(self.job_number)
            data = Sql(self.cnxn, sql, isSelect=True)
            self.table = PrettyTable(["违章编号", "违章者工号", "违章内容", "所在线路", "违章时间", "车牌号", "记录人工号"])
            self.table.add_rows(data)
            self.lab1 = tk.Label(self.frame, text=self.table, pady=10)
            self.lab1.grid(row=1, column=0)
            self.exit = tk.Button(self.frame, text="确认", command=self.cancel)
            self.exit.grid(row=3, column=0)
            self.bo = tk.Button(self.frame, text="刷新", command=self.refresh)
            self.bo.grid(row=2, column=0)
            self.geometry('450x250')
        elif self.position == '路队长':
            sql = "SELECT 线路号 FROM 成员信息 WHERE 工号={}".format(self.job_number)
            xianlu = Sql(self.cnxn, sql, isSelect=True)[0][0]
            self.lab1 = tk.Label(self.frame, text="线路 {0} 的所有违章信息如下".format(xianlu), pady=10)
            self.lab1.grid(row=0, column=0)
            
            sql = "SELECT * FROM 违章记录表 WHERE 违章者工号 IN (SELECT 工号 FROM 线路成员信息 WHERE 线路号='{0}');".format(xianlu)
            data = Sql(self.cnxn, sql, isSelect=True)
            self.table = PrettyTable(["违章编号", "违章者工号", "违章内容", "所在线路", "违章时间", "车牌号", "记录人工号"])
            self.table.add_rows(data)
            self.lab1 = tk.Label(self.frame, text=self.table, pady=10)
            self.lab1.grid(row=1, column=0)
            self.bo = tk.Button(self.frame, text="查询线路成员违章信息", command=self.CheckUserPunishMentInfo)
            self.bo.grid(row=2, column=0)
            self.bo = tk.Button(self.frame, text="刷新", command=self.refresh)
            self.bo.grid(row=3, column=0)
            self.exit = tk.Button(self.frame, text="确认", command=self.cancel)
            self.exit.grid(row=4, column=0)
            self.geometry('450x400')
        else:
            # 显示车队下所有违章信息
            sql = "SELECT 车队号 FROM 成员信息 WHERE 工号={}".format(self.job_number)
            self.chedui = Sql(self.cnxn, sql, isSelect=True)[0][0]
            self.lab1 = tk.Label(self.frame, text="车队 {0} 的所有违章信息如下".format(self.chedui), pady=10)
            self.lab1.grid(row=0, column=0)
            
            sql = "SELECT * FROM 违章记录表 WHERE 违章者工号 IN (SELECT 工号 FROM 线路成员信息 WHERE 车队号='{0}');".format(self.chedui)
            data = Sql(self.cnxn, sql, isSelect=True)
            self.table = PrettyTable(["违章编号", "违章者工号", "违章内容", "所在线路", "违章时间", "记录人工号", "车牌号", ])
            self.table.add_rows(data)
            self.lab1 = tk.Label(self.frame, text=self.table, pady=10)
            self.lab1.grid(row=1, column=0)
            self.bo = tk.Button(self.frame, text="查询车队成员违章信息", command=self.CheckUserPunishMentInfo)
            self.bo.grid(row=2, column=0)
            self.bo = tk.Button(self.frame, text="刷新", command=self.refresh)
            self.bo.grid(row=3, column=0)
            self.exit = tk.Button(self.frame, text="确认", command=self.cancel)
            self.exit.grid(row=4, column=0)
            self.geometry('500x400')
    
    def cancel(self):
        self.destroy()
    
    def CheckUserPunishMentInfo(self):
        w1 = CheckUserPunishMentInfo(self.job_number, self.name, self.position, self.cnxn)
    
    def refresh(self):
        if self.position == '司机':
            self.lab1 = tk.Label(self.frame, text="用户 {0} 的违章信息如下".format(self.name), pady=10)
            self.lab1.grid(row=0, column=0)
            sql = "SELECT * FROM 违章记录表 WHERE 违章者工号={};".format(self.job_number)
            data = Sql(self.cnxn, sql, isSelect=True)
            self.table = PrettyTable(["违章编号", "违章者工号", "违章内容", "所在线路", "违章时间", "车牌号", "记录人工号"])
            self.table.add_rows(data)
            self.lab1 = tk.Label(self.frame, text=self.table, pady=10)
            self.lab1.grid(row=1, column=0)
            self.exit = tk.Button(self.frame, text="确认", command=self.cancel)
            self.exit.grid(row=3, column=0)
            self.bo = tk.Button(self.frame, text="刷新", command=self.refresh)
            self.bo.grid(row=2, column=0)
            self.geometry('450x250')
        elif self.position == '路队长':
            sql = "SELECT 线路号 FROM 成员信息 WHERE 工号={}".format(self.job_number)
            xianlu = Sql(self.cnxn, sql, isSelect=True)[0][0]
            self.lab1 = tk.Label(self.frame, text="线路 {0} 的所有违章信息如下".format(xianlu), pady=10)
            self.lab1.grid(row=0, column=0)
        
            sql = "SELECT * FROM 违章记录表 WHERE 违章者工号 IN (SELECT 工号 FROM 线路成员信息 WHERE 线路号='{0}');".format(xianlu)
            data = Sql(self.cnxn, sql, isSelect=True)
            self.table = PrettyTable(["违章编号", "违章者工号", "违章内容", "所在线路", "违章时间", "记录人工号"])
            self.table.add_rows(data)
            self.lab1 = tk.Label(self.frame, text=self.table, pady=10)
            self.lab1.grid(row=1, column=0)
            self.bo = tk.Button(self.frame, text="查询线路成员违章信息", command=self.CheckUserPunishMentInfo)
            self.bo.grid(row=2, column=0)
            self.bo = tk.Button(self.frame, text="刷新", command=self.CheckUserPunishMentInfo)
            self.bo.grid(row=3, column=0)
            self.exit = tk.Button(self.frame, text="确认", command=self.cancel)
            self.exit.grid(row=4, column=0)
            self.geometry('450x400')
        else:
            # 显示车队下所有违章信息
            sql = "SELECT * FROM 违章记录表 WHERE 违章者工号 IN (SELECT 工号 FROM 线路成员信息 WHERE 车队号='{0}');".format(self.chedui)
            data = Sql(self.cnxn, sql, isSelect=True)
            self.table = PrettyTable(["违章编号", "违章者工号", "违章内容", "所在线路", "违章时间", "记录人工号", "车牌号", ])
            self.table.add_rows(data)
            self.lab1 = tk.Label(self.frame, text=self.table, pady=10)
            self.lab1.grid(row=1, column=0)



class DeletePunishMentInfo(tk.Toplevel):
    def __init__(self,
                 job_number: str,
                 name: str,
                 position: str,
                 cnxn
                 ):
        """
        删除某条违章信息
        :param job_number: 工号
        :param name:姓名
        :param position: 职位
        """
        super().__init__()
        self.job_number = job_number
        self.position = position
        self.name = name
        
        self.cnxn = cnxn
        
        self.frame = tk.Frame(self)
        self.frame.pack()
        self.title("删除违章信息")
        
        self.lab1 = Label(self.frame, text="违章编号:", pady=10)
        self.lab1.grid(row=0, column=0, sticky=W)
        self.ent1 = Entry(self.frame)
        self.ent1.grid(row=0, column=1, columnspan=2, sticky=W)
        
        self.bo1 = tk.Button(self.frame, text="确认", command=self.confirm)
        self.bo1.grid(row=11, column=0)
        self.exit = tk.Button(self.frame, text="取消", command=self.cancel)
        self.exit.grid(row=11, column=1)
        
        self.geometry('200x100')
    
    def confirm(self):
        punishment_id = self.ent1.get()
        if not punishment_id:
            messagebox.showinfo('提示', '操作失败\n违章编号不能为空！')
            self.destroy()
            return
        else:
            # 判断违章编号是否存在
            sql = "SELECT 违章编号 FROM 违章记录表"
            all_punishment_id = [item[0] for item in Sql(self.cnxn, sql, isSelect=True)]
            print(all_punishment_id)
            if punishment_id not in all_punishment_id:
                messagebox.showinfo('提示', '操作失败\n违章编号不存在！')
                self.destroy()
                return
            else:
                # 判断记录人是否有权限修改
                # 记录人有权限修改的工号集合
                if self.position == '司机':
                    messagebox.showinfo('提示', '司机无删除信息权限！')
                    self.destroy()
                    return
                elif self.position == '路队长':
                    sql = "SELECT 信息1.工号 FROM 成员信息 信息1,成员信息 信息2 WHERE 信息1.工号=" + self.job_number + " AND 信息1.车队号=信息2.车队号 AND 信息1.线路号=信息2.线路号;"
                    data = [item[0] for item in Sql(self.cnxn, sql, isSelect=True)]
                else:
                    sql = "SELECT 工号 FROM 成员信息 WHERE 车队号 = (SELECT 车队号 FROM 成员信息 WHERE 工号=" + self.job_number + ");"
                    data = [item[0] for item in Sql(self.cnxn, sql, isSelect=True)]
                
                sql = "SELECT 违章者工号 FROM 违章记录表 WHERE 违章编号={}".format(punishment_id)
                delete_job_number = Sql(self.cnxn, sql, isSelect=True)[0][0]
                if delete_job_number not in data:
                    messagebox.showinfo('提示', '超出权限！')
                    self.destroy()
                    return
                else:
                    sql = "DELETE FROM 违章记录表 WHERE 违章编号={}".format(punishment_id)
                    Sql(self.cnxn, sql, isSelect=False)
                    messagebox.showinfo('提示', '操作成功\n成功删除工号为{0}编号为{1}的违章信息！'.format(delete_job_number, punishment_id))
                    self.destroy()
    
    def cancel(self):
        messagebox.showinfo('提示', '操作取消！')
        self.destroy()


class CheckUserPunishMentInfo(tk.Toplevel):
    def __init__(self,
                 job_number: str,
                 name: str,
                 position: str,
                 cnxn
                 ):
        """
        查询成员违章信息信息
        :param job_number: 工号
        :param name:姓名
        :param position: 职位
        """
        super().__init__()
        self.job_number = job_number
        self.position = position
        self.name = name
        
        self.cnxn = cnxn
        
        self.frame = tk.Frame(self)
        self.frame.pack()
        
        if self.position == '路队长':
            self.title("查询线路成员违章信息")
        else:
            self.title("查询车队成员违章信息")
        self.lab1 = Label(self.frame, text="违章人员工号:", pady=10)
        self.lab1.grid(row=0, column=0, sticky=W)
        self.ent1 = Entry(self.frame)
        self.ent1.grid(row=0, column=1, columnspan=2, sticky=W)
        self.lab2 = Label(self.frame, text="时间段起始时刻:", pady=10)
        self.lab2.grid(row=1, column=0, sticky=W)
        self.ent2 = Entry(self.frame)
        self.ent2.grid(row=1, column=1, columnspan=2, sticky=W)
        self.lab3 = Label(self.frame, text="时间段终止时刻:", pady=10)
        self.lab3.grid(row=2, column=0, sticky=W)
        self.ent3 = Entry(self.frame)
        self.ent3.grid(row=2, column=1, columnspan=2, sticky=W)
        
        self.bo1 = tk.Button(self.frame, text="确认", command=self.confirm)
        self.bo1.grid(row=3, column=0)
        self.exit = tk.Button(self.frame, text="取消", command=self.cancel)
        self.exit.grid(row=3, column=1)
        
        self.geometry('250x200')
    
    def cancel(self):
        messagebox.showinfo('提示', '操作取消！')
        self.destroy()
    
    def confirm(self):
        if self.position == '路队长':
            sql = "SELECT 工号 FROM 线路成员信息 WHERE 线路号 IN (SELECT 线路号 FROM 成员信息 WHERE  工号={0});".format(self.job_number)
            data = [item[0] for item in Sql(self.cnxn, sql, isSelect=True)]
        else:
            sql = "SELECT 工号 FROM 成员信息 WHERE 车队号 = (SELECT 车队号 FROM 成员信息 WHERE 工号=" + self.job_number + ");"
            data = [item[0] for item in Sql(self.cnxn, sql, isSelect=True)]
        print(data)
        start = self.ent2.get()
        end = self.ent3.get()
        if not start or not end:
            messagebox.showinfo('提示', '操作失败\n时间段不能为空！')
            self.destroy()
            return
        
        punishment_job_number = self.ent1.get()
        if not punishment_job_number:
            messagebox.showinfo('提示', '操作失败\n违章人员工号不能为空！')
            self.destroy()
            return
        elif punishment_job_number not in data:
            messagebox.showinfo('提示', '操作失败\n工号不存在或超出权限！')
            self.destroy()
            return
        else:
            sql = "SELECT * FROM 违章记录表 WHERE 违章者工号={} AND 违章时间 BETWEEN '{}' AND '{}';".format(
                punishment_job_number,
                start,
                end
            )
            all_punishment = Sql(self.cnxn, sql, isSelect=True)
            column = ["违章编号", "违章者工号", "违章内容", "所在线路", "违章时间", "记录人工号", "车牌号"]
            data = {}
            for i in range(len(column)):
                tmp = [item[i] for item in all_punishment]
                data[column[i]] = tmp
            df = pd.DataFrame(data)
            punidshment_types = {}
            for punidshment_type, item in df['违章内容'].value_counts().items():
                punidshment_types[punidshment_type] = item
            
            sql = "SELECT 姓名 FROM 成员信息 WHERE 工号={};".format(punishment_job_number)
            name = Sql(self.cnxn, sql, isSelect=True)[0][0]
            ShowUserPunishMent(start, end, name, punidshment_types)
            self.destroy()


class ShowUserPunishMent(tk.Toplevel):
    def __init__(self, start, end, name, punidshment_types):
        super(ShowUserPunishMent, self).__init__()
        self.frame = tk.Frame(self)
        self.frame.pack()
        
        self.lab1 = tk.Label(self.frame, text="成员 {0} 的所有违章信息如下".format(name), pady=10)
        self.lab1.grid(row=0, column=0)
        self.lab1 = tk.Label(self.frame, text="在{0}到{1}的时间段内，有：".format(start, end), pady=10)
        self.lab1.grid(row=1, column=0)
        
        keys = list(punidshment_types.keys())
        values = []
        values.append(tuple([str(item) for item in list(punidshment_types.values())]))
        self.table = PrettyTable(keys)
        self.table.add_rows(values)
        self.lab1 = tk.Label(self.frame, text=self.table, pady=10)
        self.lab1.grid(row=2, column=0)
        
        self.bo1 = tk.Button(self.frame, text="确认", command=self.confirm)
        self.bo1.grid(row=3, column=0)
        self.geometry('350x300')
    
    def confirm(self):
        self.destroy()
