li = [int(x) for x in input("Enter input : ").split(" ")]


def shell(li,dIncrements):
    for gap in dIncrements:
        for i in range(gap,len(li)):
            temp = li[i]
            for j in range(i,-1,-gap):
                if li[j-gap] > temp and j >= gap :
                    li[j] =li[j-gap]
                else :
                    li[j] = temp
                    break

shell(li,[5,3,1])
print(li)
