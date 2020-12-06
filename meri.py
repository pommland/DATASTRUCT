def insert(l):
    for i in range(1, len(l)): 
        key = l[i] 
        j = i-1
        while j >= 0 and key < l[j] : 
                l[j + 1] = l[j] 
                j -= 1
        l[j + 1] = key 

l = [e for e in input("Enter Input : ").split()]
if l[0] == 'EX':
    Ans = "minHeap and maxHeap"
    print("Extra Question : What is a suitable sort algorithm?")
    print("   Your Answer : "+Ans)
else:
    l=list(map(int, l))
    s = []
    for i in l:
        s.append(i)
        insert(s)
        median = s[int(len(s) / 2)] if len(s) % 2 else (s[int(len(s) / 2)] + s[int(len(s) / 2) - 1])/2
        print('list =',l[:len(s)],': median = {:.1f}'.format(median))
