l = ["Fairfield",
    "Fairfield East",
    "Fairfield Heights",
    "Fairfield West",
    "Fairlight",
    "Fiddletown",
    "Five Dock",
    "Flemington",
    "Forest Glen",
    "Forest Lodge",
    "Forestville",
    "Freemans Reach",
    "Frenchs Forest",
    "Freshwater"]
for i in l:
    if i[6] != 'Forest':
        print(i)

f_suburbs = dict()
f_suburbs["Fairfield"] = 18081
f_suburbs["Fairfield East"] = 5273
f_suburbs["Fairfield Heights"] = 7517
f_suburbs["Fairfield West"] = 11575
f_suburbs["Fairlight"] = 5840
f_suburbs["Fiddletown"] = 233
f_suburbs["Five Dock"] = 9356
f_suburbs["Flemington"] = None
f_suburbs["Forest Glen"] = None
f_suburbs["Forest Lodge"] = 4583
f_suburbs["Forestville"] = 8329
f_suburbs["Freemans Reach"] = 1973
f_suburbs["Frenchs Forest"] = 13473
f_suburbs["Freshwater"] = 8866

for town, population in f_suburbs.items():
    if town[:6] != 'Forest' and population is not None:
        print(f'{town}: {population}')

for i in range (1,101):
    if i % 3 == 0 and i % 5 != 0:
        print(f"{i}: Fizz")
    elif i % 5 == 0 and i % 3 != 0:
        print(f"{i}: Buzz")
    elif i % 5 == 0 and i % 3 == 0:
        print(f"{i}: FIZZ BUZZ")
    else:
        print(i)

happy = True
if happy:
    print ('I am happy') #缩进代表是if statement的一部分，反之则不是
print('This will print regardless of the value of happy')

happy = 1
if -1: #只要不是0都可以print
    print ('I am happy')

if not False:
    print('not False is True')
if not True is False:
    print('not True is False')

#else and elif(添加条件）
b = False
if b is True:
    print('b is True')
else:
    print('b is not True')

a = 0
b = True
if a != 0:
    print('a is non-zerp')
elif b is True:
    print("b is True")
elif a < 0 and b is True:
    print('a is negative and b is True')
else:
    print("None of the condition above hold")

#input
hours = input("Enter number of hours you worked this week: ")
hours = int (hours)
normal_rate = 51.45
overload_rate = 88.9
if hours > 35:
    pay = (35 * normal_rate) + (hours - 35) * overload_rate
else:
    pay = hours * normal_rate
print(f"This weekly payments is : {pay}")

#for loop
#用loop下载多只股票的价格
import yfinance
start = '2020-01-01'
end = None
tickers = ['QAN.AX', 'WES.AX']
for tic in tickers:
    df = yfinance.download(tic, start, end, ignore_tz=True)
    print(df)
    df.to_csv('qan_stk_prc.csv')

#Dictionary in loop：冒号前面是key，后面是value
d = {
    "beauty": True,
    "truth": True,
    "red wheelbarrow": 100000,
    5: "fingers"
    }
for value in d.values():
    print(value)
for key in d:
    print(key)
for i in d.items():
    print(i)
#tuple unpack
for i, j in d.items():
    print(f"{i}: {j}")

#range
for i in range(0,5):
#python只打印到4：-> 1，2，3，4
    print(i)
#设置间隔
for i in range(0,5,2):
#最后一位数表示间隔为2 -> 0,2,4
    print(i)

#Enumerations: #打印出位置信息
letters = ["a", "b", "c", "d", "e"]
for i in enumerate(letters, start = 1000):
#start=1000 means 最左位置上的items位置值为1000
    print(i)

#find the biggest number in a list
numbers = [3,9,1,5,7,2,11,0,3,12,3,15]
largest_number = None
for number in numbers:
    if largest_number is None:
        largest_number = number
    elif number > largest_number:
        largest_number = number
    print(number, largest_number)
print (f'The largest value is {largest_number}')

#while loop #一直运行
the_sum = 0
i = 1
while i<= 100:
    the_sum = the_sum + i
    i = i + 1
print(the_sum)

#Continue and break
for i in range(1,10):
    if i % 2 == 1:
        continue
    #print(i) -> #2,4,6,8; 如果continue在print后面则print->1,3,5,7,9
for even in range (0,10,2):
    print(even)
    if even > 2:
        break # 0,2,4; 4 break，跳出loop

#function
def quan_tic(): #定义一个function
    tic = "QAN.AX"
    print(tic)
    return tic #定义返回值

#function parameters
