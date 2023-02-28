# # def chislo(f, a):
# #     if f < 1:
# #         return a[::-1]
# #     else:
# #         a.append(f % 10)
# #         return chislo(f // 10, a)
# #
# #
# # a = []
# # b = []
# # k = chislo(123456, a)
# # h = chislo(987654, b)
# # print(k)
# # print(h)
# # #
# # #
# # # def chislo(f,count11=0):
# # #     if f<0:
# # #         f*=-1
# # #     if f==0:
# # #         return 1
# # #     if f < 1:
# # #         return count11
# # #     else:
# # #         count11+=1
# # #         return chislo(f / 10,count11)
# # #
# # # print(chislo(-312))
# #
# import random
# def chislo(f,x):
#     if f<1:
#         return x[::-1]
#     else:
#         x.append(f%10)
#         return chislo(f//10,x)
#
#
# def randNum():
#     a=random.randint(1000,9999)
#     ad=[]
#     b = chislo(a,ad)
#     print(b)
#     countDub=0
#     for i in b:
#         if b.count(i)>1:
#             print(b.count(i))
#             countDub+=1
#     if countDub!=0:
#         return randNum()
#     else:
#         return a
#
# print(randNum())


# x=[6, 6, 9, 9, 2, 10, 4, 7, 1, 5, 9, 0, 9, 4, 3, 10, 7, 3, 1, 6, 5, 3, 6, 4, 7, 6, 4, 7, 3, 10]
#
# for i in range(len(x),9,-1):
#     print(i-10,sum(x[i-

# ddh=[31,29,31,30,31,30,31,31,30,31,30,31]
# dd=[31,28,31,30,31,30,31,31,30,31,30,31]
#
# import random
# import random
# varmove={1:[10,17],8:[6,15],64:[-17,-10],57:[-15,16],
#          11:[-10,-6,6,10,15,17],12:[-10,-6,6,10,15,17],13:[-10,-6,6,10,15,17],14:[-10,-6,6,10,15,17],
#          18:[-17,-15,-6,10,15,17],26:[-17,-15,-6,10,15,17],34:[-17,-15,-6,10,15,17],42:[-17,-15,-6,10,15,17]}
#
# def nextnum (num):
#     return num + varmove[num][random.randint(0, (len(varmove[num]) - 1))]
#
# for i in varmove[1]:
#     print(i)


def solution(s):
    a = ''
    for i in range(len(s)):
        print(s[i].isupper())
        if s[i].isupper:
            a += ' '
            a += s[i]
        else:
            a += s[i]
    return print(a)


solution('bFaaR')
