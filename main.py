#Zadanie1
# zbior1 = [ 1 -x for x in  range(1, 11, 1)]
# print(zbior1)
# zbior2 = [4**y for y in range(8)]
# print(zbior2)
# zbior3 = [z for z in zbior2 if z % 2 == 0]
# print(zbior3)

#Zadanie2
# Lista = [randint(0, 100) for x in range(10)]
# Lista.sort()
# print(Lista)
# parzysta = [x for x in Lista if x%2==0]
# print(parzysta)

#Zadanie3
# produkty = {"bułki": "sztuki", "mąka": "kg", "sól": "kg", "baton": "sztuki"}
# sztuki = [keys for keys, values in produkty.items() if values == "kg"]
# print(produkty)
# print(kg)

#Zadanie4
# def pit(x, y, z):
#  przy = x**2 + y**2
#  przeciw = z**2
#   if przy == przeciw:
#       print("Trójkąt o bokach", x, y, z, "jest trójkątem prostokątnym.")
#     return 1
#   else:
#       print("Trójkąt o bokach", x, y, z, "nie jest trójątem prostokątnym.")
#           return 0
# print(pit(3,4,5))
# print(pit(2,4,5))

#Zadanie5
# def trapez(a=2, b=4, h=3):
#   P = ((a+b)*h)/2
# print("Pole: ")
#   return P
# print(trapez())

#Zadanie6
# def ciag1(a1=1, y=4, ile=10):
#   for i in range(ile):
#           a1 *= y
#       return a1
# print(ciag1())

#Zadanie7
# def ciag2(a1=1, y=4, ile=10):
#     a1 = (a1*y)**ile
#     return a1
# print(ciag2())

#Zadanie8
# zakupy = {"ziemniaki": 4, "chispy": 7, "pizza": 15}
# def list(a):
#     b = 0
#     c = 0
#     for x in a.values():
#         b = b + x
#         c += 1
#     print('Wartość zakupów to',b, "zł.\nWszyskich produktów jest: ")
#     return c
# print(list(zakupy))

