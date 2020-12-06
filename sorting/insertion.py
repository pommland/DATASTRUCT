input_data = [int(x) for x in input("Enter input : ").split(" ")]


def insertion(input_data):
    for i in range(1,len(input_data)):
        temp = input_data[i]
        for j in range(i,-1,-1):
            if input_data[j-1] > temp and j > 0 :
                input_data[j] = input_data[j-1]

            else :
                input_data[j] = temp 
                break



insertion(input_data)
print(input_data)