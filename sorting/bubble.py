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