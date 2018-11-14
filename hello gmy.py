
# b=100<101
# print(b)
# i=1
# while i < 5:
#     print(i)
#     i=i+1
#     print(i)
# print(3//2）
# import  random
# f = random.uniform(10,20)
# print(f)
# import  random
# f = random.randint(10,20)
# print(f)
# b = 25<30<66>20
# print(b)
# l=[1.2,'huyu','guomengyao']
# print(l)
# print(l[2])
# print(l[:3])
# k = (1,2,5,6,7,)
# print(k)
# print(7%5)
# l=[1,2,3,4,5,6,]
# d=[7,8,9,]
# print(l+d)
#
# t = (1,2,3,4,)
# t[1]=6
# print(t[1])

# a=(0,1,2,9)
# k=(5,7)
# k=a+k
# print(k)

# x =  int(input('please enter into score：'))
# if(x>90):
#     print('excellent')
# elif(x>80):
#     print('very good')
# elif(x>70):
#     print('good')
# else:
#     print('come on')
# print('end')

# list=[]
# i = 0
# while i<6:
#     x=input()
#     list.append(x)
#     i=i+1
# print(list)

# list=[]    建立一个空列表
# i = 0
# s = 0
# n = int(input())   n为输入的一个整数
# while i<n:         while循环当i<n
#     x=input()       输入x
#     if(int(x)%2==1):    如果x对2取余，余数为1
#     # list.append(int(x))    将这些x放入空列表list中
#       s = s+int(x)      s为这些x的和
#     i=i+1
# print(s)



# import random
# a = random.randint(1,2)
# if(a==1):
#     a="左"
# else:
#     a="右"
# b = random.randint(1,9)
# c = random.randint(1,6)
# print("请%s侧%s排%s列的同学回答老师问题!" % (a,b,c))
#
# a = input()
# b =a[::-1]
# if a == b :
#     print("是回文字符串")
# else:
#     print("不是回文字符串")
#
#
# a=input("输入月/日:")
# a=a . split("/")
# b=[31,28,31,30,31,30,31,31,30,31,30]
# m=a[0]
# n=a[1]
# if m=="1":
#     print("这是2018年的第%s天"%n)
# else:
#     i=0
#     q=0
#     while  i<int(m)-1:
#         q=q+b[i]
#         i=i+1
# print("这是2018年的第%s天" % (int(n) + int(q)))



# def f(π,r):
#     s = π*r*r
#     return(s)
# print(f(3.14,5))


# def f(len):
#     i=1
#     while i<=len:
#          print(i,end=" ")
#          i=i+1
#     print(" ")
# def g(len):
#     i = 0
#     while i<len:
#         f(i+1)
#         i=i+1
# a = int(input("input:"))
# g(a)

# for i in range (1,100000000):
#     if i%1==0 and i%2==1 and i%3==0 and i%4==1 and i%5==4 and i%6==3 and i%7==0 and i%8==1 and i%9==0:
#         print(i)
#         break
#     else:
#         pass

# l=[]
# b=666
# a=int(input())
# while b>=1:
#     s=b%a
#     b=b//a
#     l.append(s)
# l.reverse()
# list=map(str,l)
# print(''.join(list))


# i=0
# while i%1!=0 or i%2!=1 or i%3!=0 or i%4!=1 or i%5!=4 or i%6!=3 or i%7!=0 or i%8!=1 or i%9!=0:
#     i+=1
# print(i)


# a=int(input())
# b=int(input())
# c=int(input())
# d=int(input())
# e=int(input())
# f=int(input())
# g=int(input())
# h=int(input())
# i=int(input())
# j=int(input())
# l=[a,b,c,d,e,f,g,h,i,j]
# l.sort()
# print(l[-2])


# def f(len):
#     i=1
#     while i<=len:
#          print(i,end=" ")
#          i=i+1
#     print(" ")
# def g(len):
#     i = 0
#     while i<len:
#         f(i+1)
#         i=i+1
# a = int(input("input:"))
# g(a)

# a=int(input())
# i = 1
# while i <= a:
#     j = 1
#     while j <= i:
#         print("%d*%d"%(i,j),end = ' ')
#         j += 1
#     print()
#     i += 1

# a=int(input())
# def f(x):
#     n=1
#     while n<=a:
#         m=1
#         while m<=n:
#             print(("%sx%s=%s"%(n,m,n*m)),end=' ')
#             m=m+1
#         print()
#         n=n+1
# f(a)



# 1.实现sum。
# 2.实现list中的元素的修改
# 3.用函数实现12
# 4.输入1 1 2 3 5 8 13 21 34
# 5.用函数实现4
# 作业1.reverse   2.用递归函数实现4

# lis = [2,6,15,36,27,66]
# def reverse_g(lis):
#     a=[]
#     a=[lis[-1],lis[-2],lis[-3],lis[-4],lis[-5],lis[-6]]
#     return(a)
# print(reverse_g(lis))


n=int(input('n:'))
def x(n):
    a=1
    b=1
    i=1
    if n==0:
        return False
    elif n==1:
        return 1
    elif n==2:
        return 1
    elif n>2:
        a=a+b
        i=i+1
        b=a+b
        if i==n:
            return a

print(x(n))










