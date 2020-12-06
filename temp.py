# def shell(li, dein):
#     for gap in dein :
#         for i in range (gap,len(li)):
#             temp = li[i]
#             for j in range(i,-1,-gap):
#                 if li[j-gap] > temp and j >= gap :
#                     li[j] = li[j-gap]
#                 else :
#                     li[j] = temp
#                     break
# li = [1, 6, 99, 2, 3]
# # print(shell([1, 6, 99, 2, 3], [5, 3, 1]))
# shell(li,[5,3,1])
# print(li)


# def merge(li):
#     if len(li)> 1:
#         m = len(li)//2
#         r = merge(li[:m])
#         l = merge(li[m:])
#         lst = []
#         while len(lst) < len(li):
#             rP = r[0] if len(r) > 0 else None
#             lP = l[0] if len(l) > 0 else None
#             if lP == None:
#                 lst.append(r.pop(0))
#             elif rP == None:
#                 lst.append(l.pop(0))
#             elif rP > lP:
#                 lst.append(l.pop(0))
#             else:
#                 lst.append(r.pop(0))
#         return lst
#     else :
#         return li

# print(merge([1, 6, 99, 2, 3, 6, 4]))

def selection(li):
    for i in range(len(li)-1,-1,-1):
        c_j = 0 
        c_max = 0
        for j in range(i+1):
            if li[j] > c_max :
                c_max = li[j]
                c_j = i

        li[i],li[c_j] = li[c_j] ,  li[i]

def insertion(li):
    for i in range(1,len(li)):
        temp = li[i]
        for j in range(i,-1,-1):
            if li[j-1] > li[j] and j>0:
                li[j-1] , li[j] = li[j] , li[j-1]
            else :
                li[j] = temp
                break
 

input_data = [int(x) for x in input("Enter input : ").split(" ")]
