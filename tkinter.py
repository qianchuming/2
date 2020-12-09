#导入模块
import tkinter
import tkinter.ttk
import tkinter.messagebox
import tkinter.simpledialog

def button1Click():
    tkinter.messagebox.showinfo(title="Hi",message=xuehao.get())

root = tkinter.Tk() #创建应用程序的主窗口

button1 = tkinter.Button(root,text='导入学生信息',command=button1Click)

button1.place(x=20,y=20,height=30,width=100)

xuehao = tkinter.StringVar(root)
entryXuehao = tkinter.Entry(root, width=150, textvariable=xuehao)
entryXuehao.place(x=100,y=5,height=20)

#msgbox = tkinter.messagebox.showinfo(title='Hi',message=xuehao)

root.mainloop()#启动消息主循环，启动应用程序
