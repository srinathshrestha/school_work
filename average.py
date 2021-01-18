"""write a program to print the number divisible by 3 & 5 with in 1000 """
# for a in range(1000+1):
#     if a%3==0 and a%5==0:
#         print(a)
#

#---------------------------------------------------------------------------------
'''average of no.s divisible by 3 with in 100'''
lis = []
t = 0
for i in range(100):
    if i%3==0:
        lis.append(i)

for ele in range(0, len(lis)):
    t+= lis[ele]
print('sum of the average of no.s divisible by 3 with in 100 is', t/2)

