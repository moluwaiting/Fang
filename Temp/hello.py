# Python learning  Ctrl+caps执行文件
import sys
from random import randint
# import tensorflow as tf

class day1:             #2019.07.17
    def fun1():
        msgs =(1,2,3,4,5,6)
        print(ord("a")) #获得某个字符的二进制码
        print(msgs)
    def fun2():
        face = randint(1,6)#生成随机数
        if face == 1:
            print("1")
        elif face ==2:
            print("2")
        else:
            print("wrong!")
    def fun3():
        sum = 0
        for x in range(0,3,1):#范围为１－２，不指定０的话就从１开始,步长为１
            sum+=x
        print(sum)
    def fun4():
        x = int(input('x = '))
        y = int(input('y = '))
        if x > y:
            x, y = y, x
        for factor in range(x, 0, -1):
            if x % factor == 0 and y % factor == 0:
                print('%d和%d的最大公约数是%d' % (x, y, factor))
                print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
                break
    def fun5():
        
        row = int(input('请输入行数: '))

        for i in range(row):
            for _ in range(row-i):#下划线为临时变量
                print('*', end='')
            print()

    def Narcissistic_number():#寻找水仙花数一个3位数，它的每个位上的数字的3次幂之和等于它本身：例如：1^3 + 5^3+ 3^3 = 153
        result = []
        for i in range(99,1000):#遍历所有的三位数
            a = i//100 #python整除
            #百位数  
            b = (i-100*a)//(10)
            #十位数
            c = i-100*a-b*10  
            #个位数
            if a**3+b**3+c**3 == i :
                result.append(i)#存到一个列表里
        print(result)
    
    def Perfect_number():       #除了自身以外的所有公约数的和等于自身
        Perfect = []
        for i in range(1,1001):
            yushu = []
            for j in range(2,i):#从1开始，一直到i-1
                if (i%j)  == 0: #整除运算,取余数
                    yushu.append(j)
            sum = 0
            for k in range(len(yushu)):
                sum = sum + yushu[k]
            if sum+1 == i:
                Perfect.append(i)
        print(Perfect)

class day2():           #2019.07.18


    
    def baijibaiqian():
        #公鸡５块钱一只，母鸡三块钱一只，鸡仔1/3快钱一只，１００快钱买１００只鸡，多少种可能
        for i in range(0,101):
            for j in range(0,101-i):
                if 5*i+3*j+(1/3)*(100-i-j) == 100 :
                    print(i,j,100-i-j)
    
    def factorial(num):
        sum = 1
        while(num!=0):
            sum = num*sum
            num-=1
        return sum
    
    def roll_dice(n=1):#默认值设置为1,可以自己指定
        sum = 0
        for _ in range(n):
            sum += randint(1,6)
        return sum
    
    def palindrome_number(num=123321):        #回文数,正反一样
        # 尝试将数字颠倒过来
        num1 = str(num) #字符型
        num2 = []       #列表
        j = len(num1) #数的总个数
        for i in range(len(num1)):
            num2.append(num1[int(len(num1)-i-1)])
        num3 = "".join(num2)                   #列表转字符串，中间无间隔
        if int(num3) == num:
            print(str(num)+str("　是一个回文数!"))
        else:
            print(str(num)+str("　不是一个回文数!"))
    
    def prime_num(num=7):#素数
        for i in range(2,num):
            if (num%i) == 0 :
                print("False")
                num = 0
                break
        if num != 0:
            print("True")
                
                
    def test():
        yushu = 10%5
        # yushu = list(yushu)
        print(yushu)
        # str1 = "".join(yushu)
        # print(str1)


if __name__ == "__main__":
    day2.prime_num(9)
    # day2.test()
    # pass
