# Use the dictionary f_suburbs as given as your starting point.
# This dictionary contains Sydney suburb/population pairs,
# with the mapping going from suburb keys to population values.

# Do the following steps:
# 1. Remove all suburbs that don't start with a F
# 2. Ensure that your dictionary contains:


# The None values indicate the Wikipedia did not have population data.
# These should be INCLUDED in your dictionary.

f_suburbs = {"Randwick": 29986, "Kensington": 15004, "Frenchs Forest": 13473, "Flemington": None}

nf_suburbs = []

for key in f_suburbs:
    if key[0] != 'F':
        nf_suburbs.append(key)

for suburbs in nf_suburbs:
    f_suburbs.pop(suburbs)

f_suburbs.update({
    'Fairfield': 18081,
    'Fairfield East': 5273,
    'Fairfield Heights': 7517,
    'Fairfield West': 11575,
    'Fairlight': 5840,
    'Fiddletown': 233,
    'Five Dock': 9356,
    'Flemington': None,
    'Forest Glen': None,
    'Forest Lodge': 4583,
    'Forestville': 8329,
    'Freemans Reach': 1973,
    'Frenchs Forest': 13473,
    'Freshwater': 8866
})

print(f_suburbs)

#命名空间namespace：如何用name找到object

#Method
x = 'My fUnNy tYpEcAsE sTrInG'
x = x.upper().lower()
print(x)
x_fn = x.lower
print(x_fn())

#把变量值带入string中
a = True
b = 5
print(f'The value of a is {a} and the value of b is {b}') #f-string
print('The value of a is {} and the value of b is {}'.format(a , b))

#list 有序，可更改，有index
lst_a= [1, 'string', True, None] #创建list, list中可以有数字字符串boolean空值
lst_b= ['a', lst_a] #list中可以含有另一个list

lst = [1, 'string', True, None] #index从0开始，list当中第一个值的位置是0
print(f'The item at index 0 is {lst[0]}')
print(f'The item at index 1 is {lst[1]}')
print(f'The item at index 2 is {lst[2]}')
print(f'The item at index 3 is {lst[3]}')


lst = [1, 'string', True, None] #list支持反向index，最右位置值是-1，由右向左递减
print(f'The item at index -4 is {lst[-4]}')
print(f'The item at index -3 is {lst[-3]}')
print(f'The item at index -2 is {lst[-2]}')
print(f'The item at index -1 is {lst[-1]}')

#切片
lst = ['a', 'b', 'c', 'd', 'e', 'f']
print(f'The slice from index 1 through 4 is {lst[1:4]}') #第四位数字不被包括在内，只切到第三位，index从0开始，i.e.: b, c, d
lst = ['a', 'b', 'c', 'd', 'e', 'f']
print(f'The slice from index -5 through -2 is {lst[-5:-2]}') #第-2位数字不包括在内，只切到第-3位
print(f'lst[:3] gives {lst[:3]}')
print(f'lst[:100] gives {lst[:100]}')

#append: 在list最后一位加入一个element
lst_a = [1]
list.append(lst_a, 2) #OR
lst_a = [1]
lst_a.append(2)
print(lst_a)

#extend: 合并两个list
lst_a=[1]
lst_b=[2,3]
lst_a.extend(lst_b)
print(lst_a)

#insert: 在list中一个具体位置插入item
lst = [1, True, None]
lst.insert(1, 'string')
print(f"After insertion, lst is now {lst}")

#remove or pop删除list中的item
lst = [1, 'string', True, None, True]
lst.remove(True) #OR lst.pop(2)
print(f"lst after removing the first True is {lst}")
lst = [1, 'string', True, None, True]
lst.pop()
print(f"lst after removing the CURRENT last element {lst}")
#remove list中多个elements
lst = [1, 'string', True, None, True]
elements_to_remove = [1, 'string']
for elements in elements_to_remove:
    lst.remove(elements)
print(lst)


#len: 计算list的长度（也就是list中item的数量）
lst = [1, 'string', True, None, True]
no_of_item = len(lst)
print(f"lst has {no_of_item} items")

#Tuples 固定长度不可更改顺序,有序, index和切片与list相同，lst是方括号，tuples是圆括号
#Tuples可以pack和unpack: 将element分给不同的variables
tup = (1, 2) #tuples括号可省略
(a, b) = tup
print(f"'a' is {a} and 'b' is {b}")
#赋值数量必须一致

#sets（集合）：无序不重复
s = {1, 2, 3, 3, 3, 3}
print(s) #i.e.: {1,2,3}

#add和remove修改set中的内容
s = set()
s.add('QAN.AX')
s.add('WES.AX')
print(f"After adding objects, s is {s}")

#用in和not in判断某个个体是否存在于set中
s = {1, 2, 3}
1 in s
print()
4 in s
print()

#len: 计算set中个体数量

#Dictionary：储存key和value（element的两个组成部分）的对应关系
prc_dic = {
    'Fairfield': 18081,
    'Fairfield East': 5273,
    'Fairfield Heights': 7517,
    'Fairfield West': 11575,
    'Fairlight': 5840,
    'Fiddletown': 233,
    'Five Dock': 9356,
    'Flemington': None,
    'Forest Glen': None,
    'Forest Lodge': 4583,
    'Forestville': 8329,
    'Freemans Reach': 1973,
    'Frenchs Forest': 13473,
    'Freshwater': 8866
}
#读取某key对应的value，允许创建空白的dictionary: d = {}
print(prc_dic['Freshwater'])
#用len计算dic中key的数量，但由于value可以重复因此无法计算数量

#修改key对应的value, 如果key不存在则会直接新建
prc_dic = {
    'Fairfield': 18081,
    'Fairfield East': 5273,
    'Fairfield Heights': 7517,
    'Fairfield West': 11575,
    'Fairlight': 5840,
    'Fiddletown': 233,
    'Five Dock': 9356,
    'Flemington': None,
    'Forest Glen': None,
    'Forest Lodge': 4583,
    'Forestville': 8329,
    'Freemans Reach': 1973,
    'Frenchs Forest': 13473,
    'Freshwater': 8866
}
prc_dic['Freshwater'] = 8868
print(prc_dic['Freshwater'])

#同时修改多个key-value组
prc_dic.update ({'Freshwater':2, 'Fairfield': 3})
print(prc_dic['Freshwater'])





























