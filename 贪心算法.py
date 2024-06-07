from 动态规划法 import random_items
from  动态规划法 import knapsack

def greedy(n, c, w, v):
    p = [[0, 0] for i in range(n)]
    for i in range(1, n + 1):
        p[i - 1][0] = i
        p[i - 1][1] = v[i] / w[i]
    p.sort(key=lambda x: x[1], reverse=True) # 按单位价值排序 key=lambda x: x[1]表示按照第二个元素排序
    x = [0 for i in range(n + 1)]
    m = 0
    for i in range(n):
        if w[p[i][0]] <= c:
            x[p[i][0]] = 1
            c -= w[p[i][0]]
            m += v[p[i][0]]
    return m, x

def T_1():
    w = [0, 2, 3, 4, 2]
    v = [0, 3, 6, 9, 7]
    c = 5
    n = len(w) - 1
    m, x = greedy(n, c, w, v)
    print("贪心算法")
    print('物品重量：', w[1:])
    print('物品价值：', v[1:])
    print('背包容量：', c)
    print('最大价值：', m)
    print('背包选择：', x[1:])
    m, x = knapsack(n, c, w, v)
    print("动态规划法")
    print('物品重量：', w[1:])
    print('物品价值：', v[1:])
    print('最大价值：', m[n][c])
    print('背包选择：', x[1:])

def T_2():
    right_time=0
    for i in range(100):
        w, v = random_items(10+10*i)
        c=5*i
        n=len(w)-1
        temp,x1 = greedy(n, c, w, v)
        w,x2 = knapsack(n, c, w, v)
        if  x1 ==x2:
            right_time+=1
    correct_rate=right_time/100
    print('正确率：',correct_rate)
        #如果x1[0]和x2[0]不相等，记录下来
if __name__ == '__main__':
    T_1()
    T_2()
