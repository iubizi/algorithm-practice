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
# 选择
####################

def select_sort(arr):

    for i in range(len(arr)):
        index = i
        for j in range(i+1, len(arr)):
            if arr[index] > arr[j]:
                index = j # 直到找到最大元素
                
        if index != i:
            arr[i], arr[index] = arr[index], arr[i]
            
    return arr

####################
# 希尔
####################

def shell_sort(arr):
    
    gap = len(arr) // 2

    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i
            while j >= gap and arr[j-gap] > temp:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
        gap //= 2

    return arr

####################
# 桶
####################

def bucket_sort(arr, bucket_num=5): # 默认五桶

    arr_min = min(arr)
    arr_max = max(arr)

    # bucket_num = len(arr) # 空间换时间

    bucket_size = (arr_max - arr_min + 1) // bucket_num

    bucket = [ [] for _ in range(bucket_num) ] # 2D方便

    for i in arr: # 分桶
        index = (i - arr_min) // bucket_size
        bucket[index].append(i)

    for i in bucket: # 桶内排序，使用快排或者归并
        i.sort() # 稳定排序方法

    ans = [] # 输出
    for i in bucket: # 拆掉数组合并在一起
        ans.extend(i)

    return ans



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
    # 选择
    print(select_sort(arr))
    # 希尔
    print(shell_sort(arr))
    # 桶
    print(bucket_sort(arr, len(arr))) # 空间换时间

    val(bucket_sort) # 对分器
