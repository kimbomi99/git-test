try:
    arr = [1,2]
    print(arr[3])
    4/0
except (ZeroDivisionError, IndexError) as e:
    print(e)