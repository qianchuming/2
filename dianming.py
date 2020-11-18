students = {}
f= open('C:/Users/user/Desktop/students.csv','r')
lines=f.readlines()
#print(lines)
for line in lines:
    tmp1=line.split(',')
    #print(tmp1)
    xuehao = tmp1[0]
    xingming = tmp1[1]
    students[xuehao] = xingming
    #students[line.split(',')[0]] = line.split(',')[1]
#print(students)
f.close()
import random
num = eval(input(''))
#print(students.keys())
#for key in students.keys():
#    print(key)
results=random.sample(students.keys(),num)
for xuehao in results:
    print(students[xuehao])