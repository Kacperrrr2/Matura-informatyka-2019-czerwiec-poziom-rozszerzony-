# informatyka-2019-czerwiec-matura-rozszerzona-2


# wiersze=open('liczby_przyklad.txt','r')
# wiersze_pierwszych=open('pierwsze.txt','r')
# liczby=[]
# pierwsze=[]
# wynik=[]
# for wiersz in wiersze:
#     liczby.append(int(wiersz.strip()))
# for wiersz in wiersze_pierwszych:
#     pierwsze.append(int(wiersz.strip()))
# def czy_pierwsza(n):
#     if n == 2:
#         return True
#     if n % 2 == 0 or n <= 1:
#         return False
#
#     pierw = int(n**0.5) + 1
#     for dzielnik in range(3, pierw, 2):
#         if n % dzielnik == 0:
#             return False
#     return True
#
# for i in liczby:
#     if i>99 and i<5001 and czy_pierwsza(i):
#         wynik.append(i)
#
#
#
# print(wynik)

# zad.2

# wiersze=open('liczby_przyklad.txt','r')
# wiersze_pierwszych=open('pierwsze.txt','r')
# liczby=[]
# pierwsze=[]
# wynik=[]
# for wiersz in wiersze:
#     liczby.append(str(wiersz.strip()))
# for wiersz in wiersze_pierwszych:
#     pierwsze.append(str(wiersz.strip()))
# for j in range(len(pierwsze)):
#     for i in range(len(pierwsze)):
#         if pierwsze[j]==pierwsze[i][::-1]:
#             wynik.append(pierwsze[j])
#             wynik.append(pierwsze[i])
#
# print(wynik)

# zad.3

# wiersze=open('liczby_przyklad.txt','r')
# wiersze_pierwszych=open('pierwsze.txt','r')
# liczby=[]
# pierwsze=[]
# wynik=[]
# n3=0
# n2=0
# n1=0
# for wiersz in wiersze:
#     liczby.append(str(wiersz.strip()))
# for wiersz in wiersze_pierwszych:
#     pierwsze.append(str(wiersz.strip()))
# for j in liczby:
#     for i in j:
#         n1+=int(i)
#     if n1==1:
#         wynik.append(j)
#         n3 = 0
#         n1 = 0
#         n2 = 0
#         continue
#     for k in str(n1):
#
#         n3+=int(k)
#     if n3==1:
#         wynik.append(j)
#         n3 = 0
#         n1 = 0
#         n2 = 0
#         continue
#     for p in str(n3):
#         n2+=int(p)
#     if n2==1:
#         wynik.append(j)
#         n3 = 0
#         n1 = 0
#         n2 = 0
#         continue
#
#     n3 = 0
#     n1 = 0
#     n2 = 0
#
# print(wynik)