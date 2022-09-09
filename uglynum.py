num=int(input("Enter number: "))
lst=[]
for i in range(2,num+1):
    if(num%i==0):
        lst.append(i)
k=len(lst)
count1=0
for j in range(0,k):
    if(lst[j]%2!=0 and lst[j]%3!=0 and lst[j]%5!=0):
        count1+=1    
if(count1>0):
    print("Is not an UGLY number")
else:
    print("Is an ugly number")


