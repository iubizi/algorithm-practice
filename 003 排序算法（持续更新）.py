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
    val(bubble_sort) # 对分器

    
