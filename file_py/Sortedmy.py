import time

print(time.process_time())

#FIRST SORT
def sorte_my(num):
    for i in range(len(num)):
        l = i
        for k in range(i + 1, len(num)):
            if num[k] < num[l]:
                l = k
        swap(num, l, i)
    return "List that was sorted: ", num, "The time in which the function sorted the numbers: ", time.process_time()

def swap(v,x,y):
    v[x], v[y] = v[y], v[x]

