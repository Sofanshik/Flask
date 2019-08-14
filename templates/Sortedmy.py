import time

print(time.process_time())

lst = [10,9,8,7,6,5,4,3,2,1,0]
lt = [4,2,6,5,3,1,10,7,9,8]
st = [1,2,3,4,5,6,7,8,9,10]
ls = [1,2,3,4,5]

#FIRST SORT
def sorte(num):
    for i in range(len(num)):
        l = i
        for k in range(i + 1, len(num)):
            if num[k] < num[l]:
                l = k
        swap(num, l, i)

def swap(v,x,y):
    v[x], v[y] = v[y], v[x]

sorte(lst)
sorte(ls)
sorte(st)
sorte(lt)


print(lst, ls, st, lt)
