# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 15:57:28 2021

@author: 417-02
"""


from tkinter import messagebox

import tkutils as tku
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from PIL import Image, ImageTk
import data 
import ai1
import password as ps
import level1
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

class Window2():
	def __init__(self, parent,usr_name,get_login_time,current_login_user):
		self.login_times = get_login_time
		self.usr_name = usr_name        
		self.root1 = tk.Toplevel()
        
		self.parent = parent
		self.root1.geometry("%dx%d" % (1200, 800))  # 窗体尺寸
		center_window(self.root1)                   # 将窗体移动到屏幕中央
		self.root1.title("诊断系统")                 # 窗体标题
		self.root1.iconbitmap("images\\Money.ico")  # 窗体图标
		self.root1.grab_set()
		self.body()      # 绘制窗体组件
		self.current_user_list = current_login_user
	# 绘制窗体组件
	def body(self):
		self.title(self.root1).pack(fill=tk.X)

		self.main(self.root1).pack(expand=tk.YES, fill=tk.BOTH)

		self.bottom(self.root1).pack(fill=tk.X)

	def title(self, parent):
		""" 标题栏 """

		def label(frame, text, size, bold=False):
			return tk.Label(frame, text=text, bg="black", fg="white", height=2, font=_ft(size, bold))

		frame = tk.Frame(parent, bg="black")

		label(frame, "人工智能三级诊断平台", 16, True).pack(side=tk.LEFT, padx=10)
		#label(frame, "一级诊断", 12).pack(side=tk.LEFT, padx=100)
		#label(frame, "二级诊断", 12).pack(side=tk.LEFT, padx=0)
		#label(frame, "三级诊断", 12).pack(side=tk.LEFT, padx=100)
		label(frame, "", 12).pack(side=tk.RIGHT, padx=20)
		
		label(frame, str(self.login_times),10).pack(side=tk.RIGHT, padx=5, pady=5)
		label(frame, "登陆时间:",10).pack(side=tk.RIGHT, padx=5, pady=5)
		label(frame, str(self.usr_name),10).pack(side=tk.RIGHT, padx=5, pady=5)
		label(frame, "欢迎您:", 10).pack(side=tk.RIGHT, padx=5)
		image_label(frame, "images\\user.png", 40, 40, False).pack(side=tk.RIGHT)

		return frame
	#def showlog(self):
	#	log.LoginView(self.root)
		#return frame
        
	def bottom(self, parent):
		""" 窗体最下面留空白 """

		frame = tk.Frame(parent, height=10, bg="whitesmoke")
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

	def main_top(self, parent):
		def label(frame, text, size=12):
			return tk.Label(frame, bg="white", fg="gray", text=text, font=_ft(size))

		frame = tk.Frame(parent, bg="white", height=150)

		image_label(frame, "images\\img_title.png", width=240, height=120, keep_ratio=False) \
			.pack(side=tk.LEFT, padx=10, pady=10)

		self.main_top_middle(frame).pack(side=tk.LEFT)

		label(frame, "收起^").pack(side=tk.RIGHT, padx=10)

		frame.propagate(False)
		return frame

	def main_top_middle(self, parent):
		str1 = "心律失常智能诊断模型，可以识别患者的异常心电，并根据需要，辅助医生进行初级和深度诊断。"
		str2 = "一般情况下只需要十秒钟即可完成辅助诊断。"

		def label(frame, text):
			return tk.Label(frame, bg="white", fg="gray", text=text, font=_ft(12))

		frame = tk.Frame(parent, bg="white")

		self.main_top_middle_top(frame).pack(anchor=tk.NW)

		label(frame, str1).pack(anchor=tk.W, padx=10, pady=2)
		label(frame, str2).pack(anchor=tk.W, padx=10)

		return frame

	def main_top_middle_top(self, parent):
		def label(frame, text, size=12, bold=True, fg="blue"):
			return tk.Label(frame, text=text, bg="white", fg=fg, font=_ft(size, bold))

		frame = tk.Frame(parent, bg="white")

		label(frame, "智能诊断", 20, True, "black").pack(side=tk.LEFT, padx=10)
		label(frame, "操作文档").pack(side=tk.LEFT, padx=10)
		label(frame, "教学视频").pack(side=tk.LEFT, padx=10)
		label(frame, "常见问题").pack(side=tk.LEFT, padx=10)

		return frame
	
	def data1(self):
		data.Window3(self.parent,self.current_user_list)

	def main_left(self, parent):
		def label(frame, text, size=10, bold=False, bg="white"):
			return tk.Label(frame, text=text, bg=bg, font=_ft(size, bold))

		frame = tk.Frame(parent, width=180, bg="white")
		label(frame, "诊断中心", 12, True).pack(anchor=tk.W, padx=20, pady=10)
		#label(frame, "一级诊断").pack(anchor=tk.W, padx=40, pady=5)
        
		f2 = tk.Frame(frame, bg="white")
		#v_seperator(f2, width=5, bg="blue").pack(side=tk.LEFT, fill=tk.Y)
		label(f2, "一级诊断", bg="white").pack(side=tk.LEFT, anchor=tk.W, padx=40, pady=5)
		f2.pack(fill=tk.X)
        
		f1 = tk.Frame(frame, bg="white")
		#v_seperator(f1, width=5, bg="blue").pack(side=tk.LEFT, fill=tk.Y)
		label(f1, "二级诊断", bg="white").pack(side=tk.LEFT, anchor=tk.W, padx=40, pady=5)
		f1.pack(fill=tk.X)

		label(frame, "三级诊断").pack(anchor=tk.W, padx=40, pady=5)
		#label(frame, "校验模型").pack(anchor=tk.W, padx=40, pady=5)
		#label(frame, "发布模型").pack(anchor=tk.W, padx=40, pady=5)

		h_seperator(frame, 10)

		'''
        f7 = tk.Frame(frame, bg="white")		
		label(f7, "数据中心", 12, True).pack(anchor=tk.W, padx=20, pady=10)
		#label(f7, "病人数据管理").pack(anchor=tk.W, padx=40, pady=5)
		tk.Button(f7, text="病人数据管理", command=self.data1).pack(anchor=tk.W, padx=40, pady=5)        
		#label(frame, "添加病人数据").pack(anchor=tk.W, padx=40, pady=5)
		'''
		label(frame, "数据中心", 12, True).pack(anchor=tk.W, padx=20, pady=10)
#		label(frame, "病人数据管理").pack(anchor=tk.W, padx=40, pady=5)
#		label(frame, "添加病人数据").pack(anchor=tk.W, padx=40, pady=5)
		tk.Button(frame, text="病人数据管理", command=self.data1).pack(anchor=tk.W, padx=40, pady=5)
		h_seperator(frame, 10)

		label(frame, "用户中心", 12, True).pack(anchor=tk.W, padx=20, pady=10)
#		label(frame, "病人数据管理").pack(anchor=tk.W, padx=40, pady=5)
#		label(frame, "添加病人数据").pack(anchor=tk.W, padx=40, pady=5)
		tk.Button(frame, text="修改密码", command=self.change_password_windows).pack(anchor=tk.W, padx=40, pady=5)
		frame.propagate(False)
		return frame

	def change_password_windows(self):
	    ps.change_User_password(self.current_user_list)
            
	def main_right(self, parent):
		def label(frame, text, size=10, bold=False, fg="black"):
			return tk.Label(frame, text=text, bg="white", fg=fg, font=_ft(size, bold))

		def space(n):
			s = " "
			r = ""
			for i in range(n):
				r += s
			return r
        
		def zhenduan1(index):
			dig1=level1.get_dignosisi(index)
			label1['text'] = dig1

		def zhenduan(index):
			dig1=level1.get_dignosisi(index)
			label1['text'] = dig1			
            
		frame = tk.Frame(parent, width=200, bg="white")
        
		def onResize(event):
		    """Prints the scrollbar's position on window resize."""
		    print(str(myScrollbar.get()))
		
		'''
        myFrame = frame
		mySecondaryFrame = frame
		myCanvas = tk.Canvas(myFrame)
		myScrollbar = tk.Scrollbar(myFrame, orient='vertical', command=myCanvas.yview)

		myCanvas.config(yscrollcommand=myScrollbar.set)

		#for i in range(0,100):
		 #   print(i)
		 #   button = tk.Button(mySecondaryFrame, text=i)
		 #   button.pack(fill='y',expand=True)
		 #   myCanvas.configure(scrollregion=(0, 0, 0, 400))

		myFrame.pack(fill='both',expand=True)
		myScrollbar.pack(side="right",fill='y')
		myCanvas.pack(side='right', fill='both', expand=True)

		button_window = myCanvas.create_window(0, 0, anchor='nw', window=mySecondaryFrame)

		myCanvas.bind('<Configure>', onResize)

		frame.mainloop()
        '''
		#self.scrollBar = tk.Scrollbar
		#self.scrollBar.pack(side=tk.RIGHT,fill=tk.Y)
		#111
		label(frame, "分级诊断", 12, True).pack(anchor=tk.W, padx=20, pady=5)

		h_seperator(frame)

		f1 = tk.Frame(frame, bg="white")
		label(f1, space(8) + "诊断性质:").pack(side=tk.LEFT, pady=5)
		label(f1, "识别病人异常心律").pack(side=tk.LEFT, padx=20)
		f1.pack(fill=tk.X)

		f2 = tk.Frame(frame, bg="white")
		label(f2, space(5) + "*", fg="red").pack(side=tk.LEFT, pady=5)
		label(f2, "输入病人姓名:").pack(side=tk.LEFT)
		entry=tk.Entry(f2, bg="white", font=_ft(10), width=25)
		entry.pack(side=tk.LEFT, padx=20)
		#tk.Button(f2, text="下一步", width=12, command=zhenduan).pack(side=tk.LEFT, padx=5, pady=5)
		f2.pack(fill=tk.X)

		'''
        f3 = tk.Frame(frame, bg="white")
		label(f3, space(5) + "*", fg="red").pack(side=tk.LEFT, pady=5)
		label(f3, "联系方式:").pack(side=tk.LEFT)
		tk.Entry(f3, bg="white", font=_ft(10), width=25).pack(side=tk.LEFT, padx=20)
		f3.pack(fill=tk.X)
        '''
		
		f4 = tk.Frame(frame, bg="#80c1ff")
		tk.Button(f4, text="开始一级诊断", width=12, command=lambda: zhenduan1(entry.get())).pack(side=tk.LEFT,padx=5)
		#label(f4, space(5) + "*", fg="red").pack(side=tk.LEFT, anchor=tk.N, pady=5)
		#label(f4, space(8) +"一级诊断:").pack(side=tk.LEFT, anchor=tk.N, pady=5)
		label1=tk.Label(f4, bg="white",bd=1,font=_ft(10), height=5, width=60)
		label1.pack(side=tk.LEFT, padx=20, pady=5)
		f4.pack(fill=tk.X)
        
		#lower_frame = tk.Frame(frame, bg='black')
		#lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

		#label = tk.Label(lower_frame)
		#label.place(relwidth=1, relheight=1)

		f5 = tk.Frame(frame, bg="white")
		tk.Button(f5, text="进行二级诊断", width=12, command=lambda: zhenduan1(entry.get())).pack(side=tk.LEFT, padx=5, pady=5)
		#label(f4, space(5) + "*", fg="red").pack(side=tk.LEFT, anchor=tk.N, pady=5)
		#label(f5, space(8) +"二级诊断:").pack(side=tk.LEFT, anchor=tk.N, pady=5)
		tk.Text(f5, bg="white", font=_ft(10), height=5, width=60).pack(side=tk.LEFT, padx=20, pady=5)
		f5.pack(fill=tk.X)

		f6 = tk.Frame(frame, bg="white")
		tk.Button(f6, text="进行三级诊断", width=12, command=lambda: zhenduan1(entry.get())).pack(side=tk.LEFT, padx=5, pady=5)
		#label(f4, space(5) + "*", fg="red").pack(side=tk.LEFT, anchor=tk.N, pady=5)
		#label(f6, space(8) +"三级诊断:").pack(side=tk.LEFT, anchor=tk.N, pady=5)
		tk.Text(f6, bg="white", font=_ft(10), height=5, width=60).pack(side=tk.LEFT, padx=20, pady=5)
		f6.pack(fill=tk.X)
		#tk.Button(canvas, text="基本信息", bg="cadetblue", command=self.show_single, font=ft2, height=2, fg="white", width=15)\
		#	.pack(side=tk.LEFT, expand=tk.YES, anchor=tk.CENTER, padx=5)
		#tk.Button(canvas, text="患者系统", bg="cadetblue", command=self.show_multi, font=ft2, height=2, fg="white", width=15)\
		#	.pack(side=tk.LEFT, expand=tk.YES, anchor=tk.CENTER, padx=5)
		return frame
if __name__ == "__main__":
	app = Window2()
	app.root.mainloop()    