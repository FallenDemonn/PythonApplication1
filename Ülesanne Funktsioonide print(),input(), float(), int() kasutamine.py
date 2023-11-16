import math
import statistics


#1
print("Tere, maailm!")
name = str(input("Nimi: "))
age = int(input("Vanus: "))
print("Tere, maailm! Tervitav sind {0}! Ma olen {1} aastat vana".format(name, age))

print()
#2
vanus = 18
eesnimi = "Jaak"
pikkus = 16.5
kas_kaib_koolis = True #False

print(type(vanus))
print(type(eesnimi))
print(type(pikkus))
print(type(kas_kaib_koolis))


print()
#3
candies = int(input("Сколько конфет лежит на столе? "))
delete = int(input("Сколько конфет хотите убрать? "))
now = candies - delete
if(now < 0):
    print("Вы не можете убрать больше конфет, чем есть на столе")
else:
    print("Теперь на столе " + str(now) + " конфет")

print()
#4
C = float(input("Какая длинна окружности дерева? "))
d = C / math.pi
print("Диаметр дерева равен " + str(d))

print()
#5
N = float(input("Введите длинну участка: "))
M = float(input("Введите ширину участка: "))
diag = math.sqrt(N**2 + M**2)
print("Длина диагонали прямоугольного участка земли равен " + str(diag))

print()
#6
aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = teepikkus / aeg 

print("Sinu kiirus oli " + str(kiirus) + " km/h")

print()
#7
num1 = int(input("Введите первое число "))
num2 = int(input("Введите второе число "))
num3 = int(input("Введите третье число "))
num4 = int(input("Введите четвертое число "))
num5 = int(input("Введите пятое число "))
allnums =[num1, num2, num3, num4, num5]
average = statistics.mean(allnums)
print("среднее арифметическое " + str(average))

print()
#8
print(" @..@")
print("(----)")
print("(\__/)")
print('^^""^^')

print()
#9
a = int(input("Введите первую сторону треугольника "))
b = int(input("Введите вторую сторону треугольника "))
c = int(input("Введите третью сторону треугольника "))
P = a + b + c
print("Периметр треугольника равен " + str(P))

print()
#10
price = float(12.90)
tips = price * 0.1
total = round((tips + price) / 2, 2)
print("Каждый должен заплатить по " + str(total))
