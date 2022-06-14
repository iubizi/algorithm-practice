import random

####################
# 冒泡
####################

def bubble_sort(arr):

    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr

####################
# 插入
####################

def insert_sort(arr):

    for i in range(1, len(arr)):
        key = arr[i]

        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

    return arr

####################
# 对分器
####################

def val(test_name):
    
    for _ in range(10000): # 测试10000次
        arr = list(range(50))
        random.shuffle(arr)
        if list(range(50)) != test_name(arr):
            print('\nerror:')
            print(arr)
            return
    print('\nok')



if __name__ == '__main__':

    arr = list(range(20))
    random.shuffle(arr)
    print(arr)

    # 冒泡
    print(bubble_sort(arr))
    # 插入
    print(insert_sort(arr))

    val(insert_sort) # 对分器
