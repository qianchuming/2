from tkinter import *

root = Tk()

Label(root, text='请输入参加游戏的人数:').grid(row=0, sticky=W)
Entry(root).grid(row=0, column=1, sticky=E)
 
Label(root, text=' 请输入淘汰的数字：').grid(row=1, sticky=W)
Entry(root).grid(row=1, column=1, sticky=E)

Label(root, text=' 请输入幸存人数：').grid(row=2, sticky=W)
Entry(root).grid(row=2, column=1, sticky=E)

Button(root, text='结果').grid(row=3, column=1, sticky=E)

root.mainloop()