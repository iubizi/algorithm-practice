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

def bucket_sort(arr, bucket_num=None): # 默认为空

    arr_min = min(arr)
    arr_max = max(arr)

    if bucket_num == None:
        bucket_num = len(arr) # 空间换时间

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
# 归并
####################

def merge_sort(arr, left, right):

    if left == right: return

    mid = left + (right-left)//2

    merge_sort(arr, left, mid)
    merge_sort(arr, mid+1, right)

    merge(arr, left, mid, right)

def merge(arr, left, mid, right):
    
    help_list = [0] * (right-left+1)
    
    i = 0
    left_index = left
    right_index = mid + 1
    
    while left_index <= mid and right_index <= right:
        if arr[left_index] < arr[right_index]:
            help_list[i] = arr[left_index]
            left_index += 1
        else:
            help_list[i] = arr[right_index]
            right_index += 1
        i += 1
    while left_index <= mid:
        help_list[i] = arr[left_index]
        left_index += 1
        i += 1
    while right_index <= right:
        help_list[i] = arr[right_index]
        right_index += 1
        i += 1
        
    for i in range(right-left+1):
        arr[left+i] = help_list[i]



####################
# 对分器
####################

def val(test_name):
    
    for _ in range(10000): # 测试10000次
        arr = list(range(50))
        random.shuffle(arr)
        test_name(arr, 0, len(arr)-1)
        if list(range(50)) != arr: # test_name(arr):
            print('\nerror:')
            print(arr)
            return
    print('\nok')

####################
# 主函数
####################

if __name__ == '__main__':

    arr = list(range(20))
    random.shuffle(arr)
    print(arr)
    print()

    # 冒泡
    print(bubble_sort(arr))
    # 插入
    print(insert_sort(arr))
    # 选择
    print(select_sort(arr))
    # 希尔
    print(shell_sort(arr))
    # 桶（标准写法）
    print(bucket_sort(arr, len(arr))) # 空间换时间
    # 归并
    merge_sort(arr, 0, len(arr)-1)
    print(arr)

    val(merge_sort) # 对分器
