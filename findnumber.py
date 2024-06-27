l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
num = int(input("Enter your number: "))
for i in range(len(l)):
    if l[i] == num:
        print(i)

#or
l = [1, 2, 3, 4, 5, 1, 6, 7, 8, 9, 0]
num = int(input("Enter your number: "))
for i in range(len(l)):
    if l[i] == num:
        print(i)
#or
l = [1, 2, 3, 4, 5, 1, 6, 7, 8, 9, 0]
num = int(input("Enter your number: "))
c=l.count(num)
p=0
for i in l:
    if i == num:
        pos=l.index(num,p)
        print(pos)
        p=pos+1
        c-=1


l=["abhi",'kich','sach','hari']
for i in l:
    print(i[::-1])


l=["abhi",'kich','sach','hari']
for string in l:
    rev_str=''
    for i in string:
        rev_str=i+rev_str
        print(rev_str)