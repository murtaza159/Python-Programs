n=int(input("Enter the number of elements: "))

lst=[]

for i in range(0,n):
    inp=input()
    lst.append(inp)

print("Old list: ",lst)

temp=lst[0]
lst[0]=lst[n-1]
lst[n-1]=temp

print("New list: ",lst)