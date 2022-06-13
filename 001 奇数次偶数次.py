# 一个数组，只有一个数出现了奇数次，其余出现偶数次，找出那个数

test = [2,2,2,3,3,4,4,4,4,5,5,6,6,6,6,7,7]

import random
random.shuffle(test)

eor = 0
for i in test:
    eor ^= i
    
print(eor)

# 一个数组，只有两个数出现了奇数次，其余出现偶数次，找出那两个数

test = [2,2,2,3,3,4,4,4,4,5,5,6,6,6,6,7,7,10,10,10]

import random
random.shuffle(test)

eor = 0
for i in test:
    eor ^= i

get_right = eor & (~eor + 1)
eor_1 = 0
for i in test:
    if i & get_right:
        eor_1 ^= i

print(eor_1)
eor ^= eor_1
    
print(eor)
