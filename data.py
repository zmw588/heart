# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 11:30:14 2021

@author: 417-02
"""


# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 13:44:10 2021

@author: 417-02
"""

import os
import detail2 as dt
import password as ps

from tkinter import messagebox
import pickle
import tkutils as tku
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from PIL import Image, ImageTk

import tkinter.font as tkFont
import data 
import ai1
def center_window(win, width=None, height=None):
	""" 将窗口屏幕居中 """
	screenwidth = win.winfo_screenwidth()
	screenheight = win.winfo_screenheight()
	if width is None:
		width, height = get_window_size(win)[:2]
	size = '%dx%d+%d+%d' % (width, height, (screenwidth - width)/2, (screenheight - height)/3)
	win.geometry(size)


def get_window_size(win, update=True):
	""" 获得窗体的尺寸 """
	if update:
		win.update()
	return win.winfo_width(), win.winfo_height(), win.winfo_x(), win.winfo_y()


def tkimg_resized(img, w_box, h_box, keep_ratio=True):
	"""对图片进行按比例缩放处理"""
	w, h = img.size

	if keep_ratio:
		if w > h:
			width = w_box
			height = int(h_box * (1.0 * h / w))

		if h >= w:
			height = h_box
			width = int(w_box * (1.0 * w / h))
	else:
		width = w_box
		height = h_box

	img1 = img.resize((width, height), Image.ANTIALIAS)
	tkimg = ImageTk.PhotoImage(img1)
	return tkimg


def image_label(frame, img, width, height, keep_ratio=True):
	"""输入图片信息，及尺寸，返回界面组件"""
	if isinstance(img, str):
		_img = Image.open(img)
	else:
		_img = img
	lbl_image = tk.Label(frame, width=width, height=height)

	tk_img = tkimg_resized(_img, width, height, keep_ratio)
	lbl_image.image = tk_img
	lbl_image.config(image=tk_img)
	return lbl_image


def _font(fname="微软雅黑", size=12, bold=tkFont.NORMAL):
	"""设置字体"""
	ft = tkFont.Font(family=fname, size=size, weight=bold)
	return ft


def _ft(size=12, bold=False):
	"""极简字体设置函数"""
	if bold:
		return _font(size=size, bold=tkFont.BOLD)
	else:
		return _font(size=size, bold=tkFont.NORMAL)


def h_seperator(parent, height=2):  # height 单位为像素值
	"""水平分割线, 水平填充 """
	tk.Frame(parent, height=height, bg="whitesmoke").pack(fill=tk.X)


def v_seperator(parent, width, bg="whitesmoke"):  # width 单位为像素值
	"""垂直分割线 , fill=tk.Y, 但如何定位不确定，直接返回对象，由容器决定 """
	frame = tk.Frame(parent, width=width, bg=bg)
	return frame

class Window3():
	def __init__(self, parent,current_login_user):
		super().__init__()     
		self.root2 = tk.Toplevel()
		self.parent = parent
		self.root2.geometry("%dx%d" % (1200, 800))  # 窗体尺寸
		center_window(self.root2)                   # 将窗体移动到屏幕中央
		self.root2.title("数据系统")                 # 窗体标题
		self.root2.iconbitmap("images\\Money.ico")
		self.all_list = [] # 读取student_info.txt中所有的元素并存入all_list中
		self.current_stu_list = [] #存储双击行匹配到的最终数据
		self.get_number_result = [] #用户存储获取到的所有学员信息
		self.file_path = R"E:\cpsc2019cai\example\infor.txt"
		self.action_flag = 0  #设置查看/修改/添加学生信息的title值,默认为0# 窗体图标
		self.root2.grab_set()
		self.body()      # 绘制窗体组件
		self.Load_local_Data()   # 自动加载数据（加载的是all_list中已经读取到的所有数据）
		self.load_TreeView(self.all_list)   #自动将all_list中每一行的数据加载到TreeView中展示
		self.current_user_list = current_login_user
        #将窗体的行为转化为方法
		self.root2.protocol("WM_DELETE_WINDOW",self.close_windows)    #"WM_DELETE_WINDOW"为固定写法


	def body(self):
		self.title(self.root2).pack(fill=tk.X)

		self.main(self.root2).pack(expand=tk.YES, fill=tk.BOTH)

		self.bottom(self.root2).pack(fill=tk.X)

	def title(self, parent):
		""" 标题栏 """

		def label(frame, text, size, bold=False):
			return tk.Label(frame, text=text, bg="black", fg="white", height=2, font=_ft(size, bold))

		frame = tk.Frame(parent, bg="black")

		label(frame, "病人数据管理平台", 16, True).pack(side=tk.LEFT, padx=10)
		#label(frame, "一级诊断", 12).pack(side=tk.LEFT, padx=100)
		#label(frame, "二级诊断", 12).pack(side=tk.LEFT, padx=0)
		#label(frame, "三级诊断", 12).pack(side=tk.LEFT, padx=100)
		label(frame, "", 12).pack(side=tk.RIGHT, padx=20)
		image_label(frame, "images\\user.png", 40, 40, False).pack(side=tk.RIGHT)

		return frame
	#def showlog(self):
	#	log.LoginView(self.root)
		#return frame
        
	def bottom(self, parent):
		""" 窗体最下面留空白 """

		frame = tk.Frame(parent, height=5, bg="whitesmoke")
		frame.propagate(True)
		return frame

	def main(self, parent):
		""" 窗体主体 """

		frame = tk.Frame(parent, bg="whitesmoke")
		
		self.main_top(frame).pack(fill=tk.X, padx=30, pady=15)
		self.main_left(frame).pack(side=tk.LEFT, fill=tk.Y, padx=30)
		v_seperator(frame, 30).pack(side=tk.RIGHT, fill=tk.Y)
		self.main_right(frame).pack(side=tk.RIGHT, expand=tk.YES, fill=tk.BOTH)

		return frame

	def Load_local_Data(self):

	    if not os.path.exists(self.file_path):
	        messagebox.showinfo("系统提示","文件不存在.请确认后重新加载!!")
	    else:
	        try:
	            with open(self.file_path,'r',encoding='gb18030') as fd:
	                current_list = fd.readline() #一次读一行
	                while current_list:#表示直到current_list中所有元素被读完，循环结束
	                    temp_list = current_list.split(",") #按照逗号把每个list中的元素分割出来
	                    self.all_list.append(temp_list) #把分割后的每个元素重新添加到all_list列表中
	                    current_list = fd.readline() #因为我们一次只读一行。读完后如果不加这一句那么循环会一直只读第一行。

	        except:
	            messagebox.showinfo("系统信息","文件读取出现异常.请联系管理员！！")


	def load_TreeView(self,student_list:list):

        #加载数据后清空TreeView
	    for i in self.treeView.get_children(): #固定用法
	        self.treeView.delete(i)

    #加载数据
	    if len(student_list) == 0:  #这里的student_list是个参数变量传什么数据就是什么。这里最终传的事all_list中的数据在load_TreeView(self.all_list)中展示
	        messagebox.showinfo("系统消息","没有数据被加载！")
	    else:
	        for index in range(len(student_list)):
	            self.treeView.insert("",index,values = student_list[index])

	def get_student_result(self):

    #清空get_number_result中的数据(因为每次查询一个stu_number就显示一条.如果不清空就会每次查询的结果都会被显示)
	    self.get_number_result.clear()

    #获取输入的值
	    get_input = []
	    get_input.append(self.label_stu_no.get().strip())
	    get_input.append(self.get_stu_name.get().strip())
	    get_input.append(self.get_stu_age.get().strip())
	    
	    get_input.append(self.get_stu_address.get().strip())
	    get_input.append(self.get_stu_zhenduan.get().strip())

    #print(get_input)

    #匹配学号把结果存入到get_number_result中(第一个元素学号必须填写)
	    for item in self.all_list:
	        if get_input[0] in item[0] and get_input[1] in item[1] and get_input[2] in item[2] \
	                and get_input[3] in item[5] and get_input[4] in item[6]:
	            self.get_number_result.append(item)
    #print(self.get_number_result)


    #把数据加载到TreeView中
	    self.load_TreeView(self.get_number_result)

	def load_all_data(self):

    #清空所有填写的内容文本框
	    self.label_stu_no.set("")
	    self.get_stu_name.set("")
	    self.get_stu_age.set("")
	    
	    self.get_stu_address.set("")
	    self.get_stu_zhenduan.set("")

    #把all_list中的数据加载到TreeView
	    self.load_TreeView(self.all_list)

	def load_detail_windows(self):

	    detail_window = dt.Detail_Windows(self.action_flag,self.current_stu_list,self.all_list)#detailgui中传了几个参数就要load的几个参数
	    #self.wait_window(detail_window) #通过self.wait_window()方法接收detail_window的值
	    self.all_list=detail_window.all_stu_list
	    return detail_window.comp_info

	def add_student(self):
	    self.action_flag = 2  #如果action_flag值等于2则title值为添加学生信息
	    if self.load_detail_windows() == 1:
	        self.load_all_data()
	    else:
	        pass

	def update_student(self):
	    self.action_flag = 3 #如果action_flag值等于3则title值为修改学生信息
    #获取双击行的数据
	    item = self.treeView.selection()[0]
	    temp_stu_list = self.treeView.item(item, "values")

    # 因为双击行中的数据并不是我们想要的所有数据，因此我们还要遍历all_list中的元素。通过双击行获取的学号跟all_list中的学号做对比
    # 如果两个学号相等那么把all_list中对等的那一行的所有item存入到预备号的current_stu_list中
	    for item in self.all_list:
	        if item[0] == temp_stu_list[0]:
	            self.current_stu_list = item

    #加载数据
	    if self.load_detail_windows() == 1:
	        self.load_all_data()
	    else:
	        return

	def view_student(self,event):

	    self.action_flag = 1 #如果action_flag值等于1则title值为查看学生信息
    # 固定方法获取双击行的数据
	    item = self.treeView.selection()[0]
	    temp_stu_list = self.treeView.item(item, "values")

    # 因为双击行中的数据并不是我们想要的所有数据，因此我们还要遍历all_list中的元素。通过双击行获取的学号跟all_list中的学号做对比
    # 如果两个学号相等那么把all_list中对等的那一行的所有item存入到预备号的current_stu_list中
	    for item in self.all_list:
	        if item[0] == temp_stu_list[0]:
	            self.current_stu_list = item
	    self.load_detail_windows()

	def delete_student(self):
    #获取选中行的数据
	    item = self.treeView.selection()[0]
	    temp_stu_list = self.treeView.item(item, "values")

    #提醒是否删除数据

	    choose = messagebox.askyesno("删除确认","确定要删除病人信息【床号:" + temp_stu_list[0] + "  姓名:" + temp_stu_list[1] + " ] 信息吗？")

	    if choose:
	        #如果是执行下面代码
	        for index in range(len(self.all_list)):
	            if self.all_list[index][0] == temp_stu_list[0]:
	                self.all_list.pop(index)
	                break
        #更新表格
	        self.load_all_data()
	        messagebox.showinfo("系统消息","数据删除成功！")

	    else:
	        return

	def close_windows(self):

	    choose = messagebox.askyesno("系统关闭提醒","是否将修改的数据保存到文件？")
	    if choose:
	        try:
	            with open(self.file_path,mode="w") as fd:
	                fd.write("")
	            with open(self.file_path,mode="a") as fd:
	                for item in self.all_list:
	                    temp = ",".join(item)
	                    temp = temp.replace("\n","") + "\n"  #为了让光标换行
	                    fd.write(temp)
	        except:
	            showinfo("系统消息","写入文件出错！")

        #提醒
	        messagebox.showinfo("系统消息","文件写入成功！")

        #关闭窗体
	        self.root2.destroy()
	    else:
	        self.root2.destroy()

	def change_password_windows(self):
	    this_password_windows = ps.change_User_password(self.current_user_list)
    #把list绑定到change_password_windows中
	def main_top(self, parent):
		def label(frame, text, size=12):
			return tk.Label(frame, bg="white", fg="gray", text=text, font=_ft(size))

		frame = tk.Frame(parent, bg="white", height=150)

		image_label(frame, "images\\img_title.png", width=200, height=120, keep_ratio=False) \
			.pack(side=tk.LEFT, padx=5, pady=10)

		self.main_top_middle(frame).pack(side=tk.LEFT)

		#label(frame, "收起^").pack(side=tk.RIGHT, padx=10)

		frame.propagate(False)
		return frame

	def main_top_middle(self, parent):
		str1 = "心律失常病人数据管理系统，可进行对病人信息的增加、删除、更改。"
		#str2 = "可进行对病人信息的增加、删除、更改。"

		def label(frame, text):
			return tk.Label(frame, bg="white", fg="gray", text=text, font=_ft(12))

		frame = tk.Frame(parent, bg="white")

		self.main_top_middle_top(frame).pack(anchor=tk.NW)

		label(frame, str1).pack(anchor=tk.W, padx=10, pady=2)
		#label(frame, str2).pack(anchor=tk.W, padx=10)

		return frame    

	def main_top_middle_top(self, parent):
		def label(frame, text, size=12, bold=True, fg="blue"):
			return tk.Label(frame, text=text, bg="white", fg=fg, font=_ft(size, bold))

		frame = tk.Frame(parent, bg="white")
		label(frame, "病人信息", 15, True, "black").pack(side=tk.LEFT, padx=6)
        
		label(frame, "床号:").pack(side=tk.LEFT, padx=6)
		self.label_stu_no = tk.StringVar()
		tk.Entry(frame,textvariable = self.label_stu_no,font = ("微软雅黑",10,"bold"),width=6).pack(side=tk.LEFT, padx=6)

		label(frame,text = "姓名:").pack(side=tk.LEFT, padx=6)
		self.get_stu_name = tk.StringVar()
		self.label_stu_name = tk.StringVar()

		tk.Entry(frame,textvariable = self.get_stu_name,font = ("微软雅黑",10,"bold"),width=6).pack(side=tk.LEFT, padx=6)
		label(frame,text = "年龄:").pack(side=tk.LEFT, padx=6)
		self.get_stu_age = tk.StringVar()
		tk.Entry(frame,textvariable=self.get_stu_age,font = ("微软雅黑",10,"bold"),width=4).pack(side=tk.LEFT, padx=6)
		
		label(frame,text = "地址:").pack(side=tk.LEFT, padx=6)
		self.get_stu_address = tk.StringVar()
		tk.Entry(frame,textvariable=self.get_stu_address,font = ("微软雅黑",10,"bold"),width=14).pack(side=tk.LEFT, padx=6)
        
		label(frame,text = "诊断结果:").pack(side=tk.LEFT, padx=6)
		self.get_stu_zhenduan = tk.StringVar()
		tk.Entry(frame,textvariable=self.get_stu_zhenduan,font = ("微软雅黑",10,"bold"),width=12).pack(side=tk.LEFT, padx=6)

		tk.Button(frame,text = "查询",width=6,command = self.get_student_result).pack(side=tk.LEFT, padx=6)
		tk.Button(frame,text = "返回",width=6
                                          ,command = self.load_all_data).pack(side=tk.LEFT, padx=6)
		return frame
    


	def main_left(self, parent):
		def label(frame, text, size=10, bold=False, bg="white"):
			return tk.Label(frame, text=text, bg=bg, font=_ft(size, bold))

		frame = tk.Frame(parent, width=180, bg="white")
		label(frame, "操作中心", 12, True).pack(anchor=tk.W, padx=20, pady=10)
		#f1 = tk.Frame(frame, bg="whitesmoke")        
		ttk.Button(frame,text = "添加病人信息",width =12,command = self.add_student).place(x = 20,y = 40)
		#ttk.Button(frame, text="开始一级诊断", width=12, command=self.zhenduan).place(x = 20,y = 70)
		ttk.Button(frame,text="修改病人信息",width =12,command = self.update_student).place(x = 20,y = 70)
		ttk.Button(frame,text = "删除病人信息",width =12,command = self.delete_student).place(x = 20,y = 100)
		#ttk.Button(frame,text = "更改密码",width =12,command = self.change_password_windows).place(x = 20,y = 130)
		frame.propagate(False)
		return frame
        
	def zhenduan(self):
			ai1.Window1(self.root2)
            
	def main_right(self, parent):
		def label(frame, text, size=50, bold=False, fg="black"):
			return tk.Label(frame, text=text, bg="white", fg=fg, font=_ft(size, bold))

		def space(n):
			s = " "
			r = ""
			for i in range(n):
				r += s
			return r
        
		def zhenduan(self):
			ai1.Window1(self.root2)
            
		frame = tk.Frame(parent, width=200, bg="white")
        
		def onResize(event):
		    """Prints the scrollbar's position on window resize."""
		    print(str(myScrollbar.get()))
		

		self.treeView = ttk.Treeview(frame,columns = ("床号","姓名","年龄","性别","电话","家庭住址","诊断结果"),
                                     show = "headings")
        # 设置每一列的宽度和对齐方式
		self.treeView.column("床号", width=80, anchor="center")
		self.treeView.column("姓名", width=60, anchor="w")  #w代表西面也就是左边对齐的意思
		self.treeView.column("年龄", width=60, anchor="center")
		self.treeView.column("性别", width=60, anchor="center")
		self.treeView.column("电话", width=180, anchor="center")
		self.treeView.column("家庭住址", width=250, anchor="center")
		self.treeView.column("诊断结果", width=298, anchor="w")

        # 设置表头的标题文本
		self.treeView.heading("床号", text="床号")
		self.treeView.heading("姓名", text="姓名")
		self.treeView.heading("年龄", text="年龄")
		self.treeView.heading("性别", text="性别")
		self.treeView.heading("电话", text="电话")
		self.treeView.heading("家庭住址", text="家庭住址")
		self.treeView.heading("诊断结果", text="诊断结果")
		self.treeView.place(x=1,y=60,height =450)

        # 双击TreeView中某一行触发PopUp窗体
		self.treeView.bind("<Double-1>",self.view_student)  #<Double>是必须的Double以后的可以任意但是不能跟命令行重名
		return frame



