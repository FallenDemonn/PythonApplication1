from ctypes.wintypes import INT
import math
print("Ruudu karakteristikud")
a = float(input("Sisesta ruudu kulje pikkus: "))
S = a ** 2
print("Ruudu pindala", S)
P = 4*a
print("Ruudu umbermoot", P)
di = a*math.sqrt(2)
print("Ruudu diagonaal", round(di,2))
print()
print("Ristkuliku karakteristikud")
b = float(input("Sisesta ristkuliku 1. kulje pikkus => "))
c = float(input("Sisesta ristkuliku 2. kulje pikkus => "))
S = b * c
print("Ristkuliku pindala", S)
P = 2*(b + c)
print("Ristkuliku umbermoot", P)
di = math.sqrt((b**2)+(c**2))
print("Ristkuliku diagonaal", round(di,2))
print()
print("Ringi karakteristikud")
r = float(input('Sisesta ringi raadiusi pikkus => '))
d = 2 * r
print("Ringi labimoot", d)
S = math.pi * r ** 2
print("Ringi pindala", round(S,2))
C = 2* math.pi * r 
print("Ringjoone pikkus", round(C,2))

