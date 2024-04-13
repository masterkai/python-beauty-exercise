print(None is None)
print(-5 < 0 < 5)
list_1 = [1, 2, 3]

list_2 = [4, 5, 6]

list_3 = list_1 + list_2
print(list_3 * 2)

students = {"1": 'John', "2": 'Mary'}

id = input('輸入學生座號: ')

if not id in students:
    print('該學生並不存在.')
else:
    print("學生姓名為： " + students[id])

alph = "abcdefghijklmnopqrstuvwxyz"
print(alph[15:3:-3])
print(alph[::-3])
age = eval(input("enter your age: "))
n1 = 2
n2 = 2
if n2 != n1:
    print("The two numbers are the same.")

