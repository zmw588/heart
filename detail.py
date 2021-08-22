# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 13:46:41 2021

@author: 417-02
"""


import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import tkutils as tku
class Detail_Windows(): # 这里要用Toplevel不能用Tk因为tkinter只支持一个主窗体存在.要想再跳出一个窗体必须选Toplevel
    def __init__(self,parent,action_flag:int,current_stu:list,all_stu_list:list):
        super().__init__()
        self.root3 = tk.Toplevel()
        self.parent = parent
        self.comp_info=1
        self.root3.title("病人信息窗体")
        self.root3.geometry("700x600+300+100")  # 通过控制图像大小可以通过+号来调整窗体出现的位置
        self.root3.resizable(0, 0)  # 固定窗体大小.不允许改动窗体大小. resizable(0,0)表示x轴为0y轴也为0
        self.root3.grab_set()
        self.flag = action_flag
        self.current_student_list = current_stu
        self.all_stu_list = all_stu_list
        self.body(self.root3,self.flag,self.current_student_list)
        #self.iconbitmap(R"C:\Users\Administrator\python_图库\china.ico")  # 加载.ico文件
        #tku.center_window(self.root)                   # 将窗体移动到屏幕中央
        #background_color="#CCFFFF"
        #self.root.configure(bg=background_color)

        #设置全局变量
          #接收构造函数中action_flag中的值.（为了判断传进来的是添加,修改还是删除等状态值）
         # 接收构造函数中current_stu传进来的值（为了接收选中行中的值）
         #接收构造函数中all_stu_list传进来的值(强调主窗体中all_list中的值最终跟我们子窗体中all_stu_list中的值相同.因为传的是地址)
    def body(self,root3,flag,current_student_list):
        
        self.Setup_UI(self.root3,self.flag)
        self.load_windows_flag(self.root3,self.flag,self.current_student_list)
    def Setup_UI(self,parent,flag):
        # 通过style设置属性
        self.Style01 = ttk.Style()
        self.Style01.configure("titel2.TLabel", font=("微软眼黑", 24, "bold"), foreground="darkred")
        self.Style01.configure("TPanedwindow", background="#9999FF")#RoyalBlue
        self.Style01.configure("TButton", font=("微软眼黑", 11), background="#9999FF", foreground="black")
        self.Style01.configure("TLabel",font=("微软眼黑", 14, "bold"), foreground="black",background="#9999FF")
        self.Style01.configure("TRadiobutton",font=("微软眼黑", 14, "bold"), foreground="black",background="#9999FF")

        #加载窗体图片
        #self.login_img = tk.PhotoImage(file = R"D:\417_students\zhangMW\cpsc2019cai\Python-master\tkinter-pack Demo\images\bg1.png")
        #self.label_img = ttk.Label(self.root3,image = self.login_img)
        #self.label_img.pack()

        #添加Titile框体
        self.var_titel = tk.StringVar()
        self.title_label = ttk.Label(self.root3,textvariable=self.var_titel,style = "titel2.TLabel")
        self.title_label.place(x = 20,y = 30)

        #添加一个Panewindows
        self.pane = ttk.PanedWindow(self.root3,width=696, height=450, style="TPanedwindow")
        self.pane.place(x=2,y=98)

        #添加学员信息属性

        self.label_number = ttk.Label(self.pane,text = "床号",style="stu_number.TLabel")
        self.var_stunumber=tk.StringVar()
        self.label_number.place(x=30, y=20)
        self.entry_number = ttk.Entry(self.pane,textvariable = self.var_stunumber,font=("微软眼黑",12, "bold"),width=8)
        self.entry_number.place(x=80, y=20)

        self.label_name = ttk.Label(self.pane,text = "姓名",style="TLabel")
        self.var_stuname = tk.StringVar()
        self.label_name.place(x=170, y=20)
        self.entry_name = ttk.Entry(self.pane,textvariable=self.var_stuname,font=("微软眼黑",12, "bold"),width=11)
        self.entry_name.place(x=220, y=20)

        self.label_age = ttk.Label(self.pane,text = "年龄",style="TLabel")
        self.var_age = tk.StringVar()
        self.label_age.place(x=323, y=20)
        self.entry_age = ttk.Entry(self.pane,textvariable=self.var_age,font=("微软眼黑",12, "bold"),width=5)
        self.entry_age.place(x=370, y=20)

        self.Label_genter = ttk.Label(self.pane, text="性别:")
        self.Label_genter.place(x=440, y=20)
        self.var_genter = tk.IntVar()
        self.radio_boy = ttk.Radiobutton(self.root3, text="男", variable=self.var_genter, value= 0)
        self.radio_boy.place(x=520, y=116)
        self.radio_gril = ttk.Radiobutton(self.root3, text="女", variable=self.var_genter, value=1)
        self.radio_gril.place(x=600, y=116)


        self.label_mobile = ttk.Label(self.pane,text = "电话",style="TLabel")
        self.var_mobile = tk.StringVar()
        self.label_mobile.place(x=30, y=120)
        self.entry_mobile = ttk.Entry(self.pane,textvariable=self.var_mobile,font=("微软眼黑",12, "bold"),width=18)
        self.entry_mobile.place(x=120, y=120)


        self.label_homeaddress = ttk.Label(self.pane,text = "家庭住址",style="TLabel")
        self.var_homeaddress = tk.StringVar()
        self.label_homeaddress.place(x=30, y=170)
        self.entry_homeaddress = ttk.Entry(self.pane,textvariable=self.var_homeaddress,font=("微软眼黑",12, "bold"),width=59)
        self.entry_homeaddress.place(x=120, y=170)

        self.label_admission_time = ttk.Label(self.pane,text = "诊断结果",style="TLabel")
        self.var_admission_time = tk.StringVar()
        self.label_admission_time.place(x=30, y=220)
        self.entry_admission_time = ttk.Entry(self.pane,textvariable=self.var_admission_time,font=("微软眼黑",12, "bold"),width=18)
        self.entry_admission_time.place(x=120, y=220)

        #添加保存,关闭按钮
        self.save_buttion = ttk.Button(self.root3, text="保存", width=10,command = self.submit(self.flag))
        self.save_buttion.place(x=480, y=560)
        self.exit_buttion = ttk.Button(self.root3, text="退出", width=10,command = self.close_windows)
        self.exit_buttion.place(x=580, y=560)

    def load_windows_flag(self,parent,flag,current_student_list):
        """
        设置加载学员信息的titel值(通过调用Setup_UI(self)中textvariable=self.var_titel变量的方式)
        :return:
        """
        print(self.flag)
        if self.flag == 1:
            self.var_titel.set("== 查看病人信息 ==")
            self.load_stu_detail(self.current_student_list)
            #控制学员信息的状态
            self.save_buttion.place_forget() # 隐藏save_buttion按键的固定写法
            #通过控制entry变量中的["state"] = Disabled来禁用对象中的entry值.从而达到只读的效果
            self.entry_number["state"] = tk.DISABLED
            self.entry_name["state"] = tk.DISABLED
            self.entry_age["state"] = tk.DISABLED
            self.radio_boy["state"] = tk.DISABLED
            self.radio_gril["state"] = tk.DISABLED
#            self.entry_brithday["state"] = DISABLED
            self.entry_homeaddress["state"] = tk.DISABLED
            self.entry_admission_time["state"] = tk.DISABLED
            
#            self.entry_mail["state"] = DISABLED
            self.entry_mobile["state"] = tk.DISABLED
#            self.entry_personid["state"] = DISABLED
#            self.entry_professional["state"] = DISABLED
#            self.entry_emergency_contact["state"] = DISABLED
#            self.entry_emergency_mobile["state"] = DISABLED
            

        elif self.flag == 2:
            self.var_titel.set("== 添加病人信息 ==")
        elif self.flag == 3:
            self.var_titel.set("== 修改病人信息 ==")
            #先填充数据
            self.load_stu_detail(self.current_student_list)
            #控制学号不允许修改
            self.entry_number["state"] = tk.DISABLED

    def load_stu_detail(self,current_student_list):
        """
        因为展示跟修改都需要调用后台数据.因此通过load_stu_detail方法进行调用
        1.判断传入进来的值是否为0，如果是说明没有数据被加载
        2.有数据的情况通过变量.set()方法来匹配每个元素对应本地数据的下标
          性别：因为性别分男女分别设定了0跟1.因此这里要判断一下。一定要跟设定男女values的值对应上设定
        :return:
        """
        if len(self.current_student_list) == 0:
            messagebox.showinfo("系统提示","没有数据需要展示！")
        else:
            self.var_stunumber.set(self.current_student_list[0])  #学号
            self.var_stuname.set(self.current_student_list[1]) #姓名
            self.var_age.set(self.current_student_list[2]) #年龄
            if "男" in self.current_student_list[3]:
                self.var_genter.set(0)
            else:
                self.var_genter.set(1)
#            self.var_brithday.set(self.current_student_list[7])
            self.var_mobile.set(self.current_student_list[4])
#            self.var_mail.set(self.current_student_list[5])
            self.var_homeaddress.set(self.current_student_list[5])
            
#            self.var_personid.set(self.current_student_list[8])
            self.var_admission_time.set(self.current_student_list[6])
#            self.var_professional.set(self.current_student_list[10])
#            self.var_emergency_contact.set(self.current_student_list[11])
#            self.var_emergency_mobile.set(self.current_student_list[12])
            

    def close_windows(self):
        """
        关闭窗口
        :return:
        """
        self.comp_info = 0
        self.root3.destroy()

    def submit(self,flag):
        if self.flag == 1:   #view data
           pass
        elif self.flag == 2: #add data
            #准备追加学生的数据
            temp_list = []
            if len(str(self.entry_number.get()).strip()) == 0:
                messagebox.showinfo("系统消息","床号不能为空！")
            else:
                temp_list.append(str(self.entry_number.get()).strip())
                temp_list.append(str(self.entry_name.get()).strip())
                temp_list.append(str(self.entry_age.get()).strip())
                if self.var_genter.get() == 0:
                    temp_list.append("男")
                else:
                    temp_list.append("女")
                temp_list.append(str(self.entry_mobile.get()).strip())
#                temp_list.append(str(self.entry_mail.get()).strip())
                temp_list.append(str(self.entry_homeaddress.get()).strip())
#                temp_list.append(str(self.entry_brithday.get()).strip())
#                temp_list.append(str(self.entry_personid.get()).strip())
                temp_list.append(str(self.entry_admission_time.get()).strip())
#                temp_list.append(str(self.entry_professional.get()).strip())
#                temp_list.append(str(self.entry_emergency_contact.get()).strip())
#                temp_list.append(str(self.entry_emergency_mobile.get()).strip())

                #追加数据
                self.all_stu_list.append(temp_list)

                #提醒
                messagebox.showinfo("系统信息","病人信息添加成功！")

                #反馈信号给主窗体
                self.comp_info = 1
                self.root3.destroy()
        elif self.flag == 3: #update data
            temp_list = []
            if len(str(self.entry_number.get()).strip()) == 0:
                messagebox.showinfo("系统消息", "病人不能为空！")
                return
            else:
                temp_list.append(str(self.entry_number.get()).strip())
                temp_list.append(str(self.entry_name.get()).strip())
                temp_list.append(str(self.entry_age.get()).strip())
                if self.var_genter.get() == 0:
                    temp_list.append("男")
                else:
                    temp_list.append("女")
                temp_list.append(str(self.entry_mobile.get()).strip())
#                temp_list.append(str(self.entry_mail.get()).strip())
                temp_list.append(str(self.entry_homeaddress.get()).strip())
#                temp_list.append(str(self.entry_brithday.get()).strip())
#                temp_list.append(str(self.entry_personid.get()).strip())
                temp_list.append(str(self.entry_admission_time.get()).strip())
#                temp_list.append(str(self.entry_professional.get()).strip())
#                temp_list.append(str(self.entry_emergency_contact.get()).strip())
#                temp_list.append(str(self.entry_emergency_mobile.get()).strip())

            #遍历集合
            for index in range(len(self.all_stu_list)):
                if self.all_stu_list[index][0] == self.current_student_list[0]:
                    self.all_stu_list[index] = temp_list
            # 提醒
            messagebox.showinfo("系统信息", "病人信息修改成功！")

            # 反馈信号给主窗体
            self.comp_info = 1

            # 关闭窗口
            self.root3.destroy()
            return self.all_stu_list



#if __name__ == "__main__":
#    this_windows = Detail_Windows(int,list,list)
#    this_windows.mainloop()