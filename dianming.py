students = {}
f= open('C:/Users/user/Desktop/students.csv','r')
lines=f.readlines()
for line in lines:
    tmp1=line.split(',')
    xuehao = tmp1[0]
    xingming = tmp1[1]
    students[xuehao] = xingming
f.close()
import random
num = eval(input(''))
results=random.sample(students.keys(),num)
for xuehao in results:
    print(students[xuehao])
