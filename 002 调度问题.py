# 有n个任务，在一台机器上加工，每个任务的完成时间是累计时间
# 获取最优方案

task_time = [3, 8, 5, 10, 15]

# 贪心算法（最快的先执行，最慢的最后执行）
# 可以得到最优解
task_time.sort(reverse=True)
# task_time = [15, 10, 8, 5, 3]
time = 0

for i in range(len(task_time)):
    time += (i+1) * task_time[i]

print(time) # 94
