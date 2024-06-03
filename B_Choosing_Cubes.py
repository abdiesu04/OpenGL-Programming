t = int(input())
for _ in range(t):
    n , f , k = map(int , input().split())
    arr = list(map(int , input().split()))
    target = arr[f-1]
    arr.sort(reverse=True)
    first  = arr[:k]
    second = arr[k:]
    # print(arr , k , target , first , second)
    if target in first and target in second:
        print("MAYBE")
    elif target in first and target not in second:
        print("YES")
    elif target not in first:
        print("NO")
    

