from tkinter import *
root = Tk()
root.title('约瑟夫小游戏') 
def move(players,step):
    num = step - 1
    while num > 0:
        tmp = players.pop(0)
        players.append(tmp)
        num = num - 1
    return players
def play(players,step,alive):
    list1 = [i for i in range(1,players+1)]
    while len(list1)>alive: 
        list1 = move(list1,step)
        list1.pop(0) 
    return list1

Label(root, text='请输入参加游戏的人数:').grid(row=0, sticky=W)
players_num =Entry(root).grid(row=0, column=1, sticky=E)
 
Label(root, text=' 请输入淘汰的数字：').grid(row=1, sticky=W)
step_num =Entry(root).grid(row=1, column=1, sticky=E)

Label(root, text=' 请输入幸存人数：').grid(row=2, sticky=W)
alive_num =Entry(root).grid(row=2, column=1, sticky=E)

Button(root, text='结果').grid(row=3, column=1, sticky=E)

alive_list = play(players_num,step_num,alive_num)
print(alive_list)

root.mainloop()
