def bubble(li ):
    for i in range(len(li)-1,-1,-1):
        swap = False 
        for j in range(i):
            if li[j] > li[j+1]:
                li[j],li[j+1] =  li[j+1],li[j]
                swap =  True
        if not swap :
            break
    return li

input_data = [int(x) for x in input("Enter input : ").split(" ")]
# print(bubble(input_data))

def selection(li):
    for i in range(len(li)-1,-1,-1):
        c_max = 0
        c_j =  0
        for j in range(i+1):
            if li[j] > c_max :
                c_max = li[j]
                c_j = i
        li[c_j],li[i] = li[i], li[c_j]
    return li

def insertion(li):
    for i in range(1,len(li)):
        temp = li[i]

print(bubble(input_data))
print(selection(input_data))