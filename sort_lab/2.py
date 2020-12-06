def selectionSort(data, n):
	if n == 0 :
		return data 
	else :
		temp = max(data[:n+1])
		data[data.index(temp)] = data[n]
		a = data[n]
		if temp != data[n] :
			print(f'swap {data[n]} <-> {temp} : ',end='')
		data[n] = temp
		if temp != a :
			print(data)
		
			
	selectionSort(data,n-1)





Data = [int(i) for i in input('Enter Input : ').split()]
selectionSort(Data,len(Data)-1)
print(Data)