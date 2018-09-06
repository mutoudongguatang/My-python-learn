#!/usr/bin/python
# -*- coding: UTF-8 -*-



# name = ' Lily '
# message = '"Hello eric,would you like to learn some python today?"'
# print(name + message)
# print(name.title()+message.title())   #首字母大写
# print(name.upper()+message.upper())   #每个字母都大写
# print(name.lower()+message.lower())   #全部小写
# print(name.rstrip()+message)   #将末尾空格剔除
# print(name.lstrip()+message)    #将开头空格剔除
# print(name.strip()+message)     #头尾空格剔除


# bicycles = ['trke','cannondale','redline','specialized']
# print(bicycles)
# print(bicycles[0])  #读取列表中的第一个元素
# print(bicycles[0].title())  #读取列表中的第一个元素并且元素的第一个字母大写
# print(bicycles[-1])     #读取列表中的倒数第一个元素
# message = 'My first bicycle was a '+bicycles[0].title()+'.'
# print(message)


# name = ['Lily','Zhao','Qian','Sun','Li','Zhou']
# message = 'Hello '
# print(message+name[0])
# print(message+name[1])
# print(message+name[2])
# print(message+name[3])
# print(message+name[4])
# print(message+name[5])




# motor = ['honda','yamha','suzuki']
# motor.insert(0,'ducati')    #往列表第一位置添加新的元素，其余元素后移
# print(motor)
# del motor[0]    #删除列表中的第一个元素
# del motor[1]    #删除列表中的第二个元素
# motor.remove('honda')   #指定删除列表中的元素
# print(motor)
# popped_moro = motor.pop()     #删除列表中的元素，并打印删除的元素;如果pop没有值默认从后往前删除元素
# print(motor)
# print(popped_moro)
# motor[0] = 'ducati'   #替换列表中的第一个元素
# print(motor)
# motor.append('ducati')  #在列表的最后添加新的元素
# print(motor)




#往空列表中添加元素
# motor = []
# motor.append('honda')
# motor.append('yamha')
# motor.append('suzuki')
# print(motor)




# list_name = ['zhao','qian','sun']
# print(list_name)
# print('zhao xian sheng bu neng lai')
# del list_name[0]
# list_name.insert(0,'li')
# print(list_name)




cars = ['bus','toyota','bmw','audi','subaru']
# cars.sort()     #使用sort函数对列表的元素进行字母顺序排序,永久性排序
# print(sorted(cars))     #使用sorted对列表进行临时排序
# cars.reverse()  #从后往前打印列表,并且列表里元素的位置永久性改变
# print(cars)
# cars.reverse()
# print(len(cars))    #使用函数len获悉列表的长度



# word = ['japan','maldives','austria','finland','germany','usa','new zealand']
# print(sorted(word))
# print(word)
# print(word[-2])
# for word in word:
#     print(word.title()+', that was a great trick!')
#     print("I can't wait to see your next trick, " + word.title() + ".\n")
# print("Thank you")




# pizza = ['canada','mexico','aruba','brasil','chile']
# for pizza in pizza:
#     print(pizza.title() + ', I like pepperoni pizza!')
# print('I really love pizza')




# for num in range(1,8):  #使用range函数打印1~8之间不包含8的序列数字
#     print(num)



# num = list(range(1,8))  #使用list函数将range函数的数字直接转换为列表
# print(num)


# num = list(range(1,11,2))   #使用range函数打印10以内的奇数
# print(num)




# squares = []
# for value in range(1,9):
#     squares.append(value**2)    #1~9之间数字平方
#     print(squares)



# digits = [1,2,3,4,5,6,7,8,9,10]
# print(min(digits))  #使用min函数读取列表中的最小元素
# print(max(digits))  #使用max函数读取列表中的最大元素
# print(sum(digits))  #使用sum函数求列表中所有元素之和



# squares = [value **2 for value in range(1,11)]
# print(squares)



# for num in range(1,21):
#     print(num)


# num = [value for value in range(1,1000001)]
# list_num = num
# print(min(list_num))  #列表元素中最小的元素
# print(max(list_num))  #列表元素中最大的元素
# print(sum(list_num))  #列表元素之和



# num = [value for value in range(1,20,2)]   #列出20以内的奇数
# print(num)



# num = [value for value in range(3,30,3)]  #列出30以内能被3整除的元素
# print(num)



# num = [value**3 for value in range(1,11)] #1~10所有元素的立方
# print(num)



# players = [value for value in range(1,20)]  #1~20之间的列表
# print(players)
# num = players[0:10] #从players列表切片，范围第一位元素到第十位元素
# print(num)
# tie = num   #把num列表赋值给tie
# cube = [value**3 for value in tie]  #给tie列表所有元素值立方
# print(cube)



# players = ['a','b','c','d','e','f']
# for player in players[:4]:  #遍历切片展示列表前4位元素
#     print(player.title())



# my_foods = ['pizza','falafel','carrot cake']
# friend_foods = my_foods[:]  #把my_foods列表中的所有元素复制给friend_foods列表
# my_foods.append('cannoli')
# print(my_foods)
# friend_foods.append('ice cream')
# print(friend_foods)



# foods = ('shrimp','beef','lamb','beer','noodles')
# foods = ('shrimp','beef','lamb','beer','ball')
# for food in foods:    #使用for循环遍历
#     print(food.title())



# cars = ['audi','bum','subaru','toyota']
# for car in cars:
#     if car == 'audi':       #使用if判断读取列表中的元素是否等于赋值
#         print(car.upper())
#     else:
#         print(car.title())



user_name = ['zhao','qian','sun','li','zhou','wu']
new_name = raw_input("请输入姓名:")
print(new_name)
if new_name in user_name:
    print("请重新输入")
else:
    print("可以注册")
































































