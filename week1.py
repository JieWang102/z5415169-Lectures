# Downloads Qantas share price beginning 1 January 2020
import yfinance
tic = "QAN.AX"
start = '2020-01-01'                                      # (3)
end = None                                                # (4)
df = yfinance.download(tic, start, end, ignore_tz=True)   # (5)
print(df)                                                 # (6)
df.to_csv('qan_stk_prc.csv')                              # (7)

#assigning variables
a=1
b=2
print(a)
print(type(a))

#parallel assignment
a,b=1,2
a,b=b,a #a,b=2,1

c=(2+8)/2**3
print(c)
#10/8=1.25

#字符串
c="hello world!"
print(c)
print(type(c))

a=None
print(a)
print(type(a))

#boolean
a=True
print(a)
print(type(a))

a = False
print(a)
print(type(a))

# 转换类型
a = 1
print(a)
print(type(a))
a = str(a)
print(a)
print(type(a))

a = 1.0
print(a)
a = int(a) #更新
print(a)

a = float(a)
print(a)

a = 1.6
a = int(a)
print(a) #a = 1 不是四舍五入

a="1"
print(int(a))
print(float(a))
print(type(a))
#只是打印a变成int和float后的样子，并没有更改类型

msg="I like number"
num=1
print(msg, str(num))
print(msg+" "+str(num))
print(msg, num) #, 不同类型不受影响

#input
#当程序运行到input的时候，就会要求用户输入信息且此信息是string

a=input("Give me a number:")
print(a)
print(type(a))

name=input("what is your name?")
print(name)
print(type(name))

num=input("My favourite number is 1, what is yours?")
result=(1+int(num))
print("The sum of our number is", result)

#两函数相加
def function(a,b):
    value=a+b
    return value
#intentation - 4 spaces
example=function(10,20)
print(example)
