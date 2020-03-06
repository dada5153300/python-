# 命令式编程和函数式编程

# 命令式编程
print("命令式编程")
x1 = list(range(10))
print(x1)
y1 = []
for num in x1:
    y1.append(num+5)

print(y1)
y1 = []
print(y1)
y1 = [num+5 for num in x1]    # 列表推导式
print(y1)

# 函数式编程
print("函数式编程")
x2 = list(range(10))
print(x2)


def add5(num):
    return num + 5


y2 = list(map(add5, x2))
print(y2)

y2 = []
print(y2)
y2 = list(map(lambda num : num+5, x2))  # lambda表达式等价于add5
print(y2)


class a :
    def __init__(self):
        pass