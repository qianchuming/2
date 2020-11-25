def move(play_list, num):
    while num > 0:
        play_list.append(play_list.pop(0))
        num=num-1
    return play_list

def play(players, step, stop):
    play_list = [i for i in range(1,players+1)]
    num=step-1
    while len(play_list) > stop:
        play_list=move(play_list, num)
        play_list.pop(0)
    retuern play_list