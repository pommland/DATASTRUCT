def selection(li):
    for i in range(len(li)-1,-1,-1):
        c_j = 0 
        c_max = 0
        for j in range(i+1):
            if li[j] > c_max :
                c_max = li[j]
                c_j = j
            
            li[c_j],li[i] = li[i], li[c_j]

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


def bubble(input_data):
    for i in range(len(input_data)-1,-1,-1):
        swap = False
        for j in range(i) :
            if input_data[j] > input_data[j+1]:
                input_data[j],input_data[j+1] = input_data[j+1] , input_data[j]
                swap = True

        if not swap:
            break
    return input_data
print(input_data)
input_data = bubble(input_data)
print(input_data)


def shell(li,deIn):
    for gap in deIn:
        for i in range(gap,len(li)):
            temp = li[i]
            for j in range(i,-1,-gap):
                if li[j-gap] > temp and j>= gap :
                    li[j] = li[j-gap]
                else :
                    li[j] = temp
                    break


input_data = [int(x) for x in input("Enter input : ").split(" ")]

# li = input_data
# shell(li,[5,3,1])
# print(li)


print(input_data)
print("")
selection(input_data)
print(input_data)