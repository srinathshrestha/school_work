# n = []
# k = len(n)
# for i in range(10):
#     ellement = int(input(f"Enter the {i+1}.Numbers : "))
#     n.append(ellement)
# def bubble(n):
#     if len(n)==10:
#         for i in range(len(n) - 1, 0, -1):
#             for j in range(i):
#                 if n[j] > n[j + 1]:
#                     t = n[j]
#                     n[j] = n[j + 1]
#                     n[j + 1] = t
#
# print('the greatest number in that you have entered is',n[k-1])
#
#
#
#

l=[]
g=0
for i in range(10):
    a = int(input("enter the elements : "))
    l.append(a)

for i in range(10):
    if l[i]>g:
        l[i]=g
        print(f"{g} is the greates number.")
