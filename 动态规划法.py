import random
import time
import matplotlib.pyplot as plt




# 动态规划法求解0-1背包问题

def knapsack(n, c, w, v):
    # 确定状态转移方程
    # 初始化二维状态数组
    m = [[0 for j in range(c + 1)] for i in range(n + 1)]
    for i in range(1, n+1):
        for j in range(1, c + 1):
            # 第i个物品放不下
            if w[i]<=j:
                m[i][j] = max(m[i-1][j], m[i-1][j-w[i]]+v[i])
            else:
                m[i][j] = m[i-1][j]
    j=c
    x=[False for i in range(n+1)]
    for i in range(n, 0, -1):
        if m[i][j]==m[i-1][j]:
            x[i]=0
        else:
            x[i]=1
            j-=w[i]
    return m,x

#随机生成物品重量和价值
def random_items(n):
    w = [random.randint(1, 15) for i in range(n)]
    w.insert(0, 0)
    v = [random.randint(1, 15) for i in range(n)]
    v.insert(0, 0)
    return w, v

#改进的动态规划法求解0-1背包问题
def knapsack2(n, c, w, v):
    p=[[0,0] for i in range(n*c)]
    head=[0 for i in range(n+2)]
    left=0
    right=0
    Next=1
    head[1]=1
    for i in range(1,n+1):
        k=left
        for j in range(left,right+1):
            if p[j][0]+w[i]>c:
                break
            y=p[j][0]+w[i]
            m=p[j][1]+v[i]
            while k<=right and p[k][0]<y:
                p[Next][0]=p[k][0]
                p[Next][1]=p[k][1]
                Next+=1
                k+=1
            if k<=right and p[k][0]==y:
                if m<p[k][1]:
                    m=p[k][1]
                    k+=1
            if m>p[Next-1][1]:
                p[Next][0]=y
                p[Next][1]=m
                Next+=1
            while k<=right and p[k][1]>=p[Next-1][1]:
                k+=1
        while k<=right:
            p[Next][0]=p[k][0]
            p[Next][1]=p[k][1]
            Next+=1
            k+=1
        left=right+1;   right=Next-1;   head[i+1]=Next
    return p,head

def Traceback(n, w, v,p, head):
    x=[0 for i in range(n+1)]
    j=p[head[n+1]-1][0]
    m=p[head[n+1]-1][1]
    for i in range(n,0,-1):
        for k in range(head[i-1],head[i]):
            if p[k][0]+w[i]==j and p[k][1]+v[i]==m:
                x[i]=1
                j=p[k][0]
                m=p[k][1]
                break
    return x


def normal_dp_for01():
    w = [0, 2, 3, 4, 2]
    v = [0, 3, 6, 9, 7]
    c = 5
    n = len(w)-1
    m,x=knapsack(n, c, w, v)
    print('背包容量：', c)
    print('物品重量：', w)
    print('物品价值：', v)
    print('最大价值为：', m[n][c])
    print('装入背包的物品编号为：')
    for i in range(len(x)):
        if x[i]:
            print(i, '  ', end='')

def normal_dp_complex_anlysis():
    time_list = []
    for n in [10, 50, 100, 500, 1000]:
        for c in [5, 25, 50, 250, 500]:
            w, v = random_items(n)
            start = time.time()
            m,x = knapsack(n, c, w, v)
            end = time.time()
            print('物品重量：', w)
            print('物品价值：', v)
            print('最大价值为：', m[n][c])
            print('装入背包的物品编号为：')
            for i in range(n):
                if x[i]:
                    print(i+1, ',', end='')
            print()
            print('Running time: %s Seconds'%(end-start))
            time_list.append(end-start)
    # x=n*c
    x = [ n * c for n in [10, 50, 100, 500, 1000] for c in [5, 25, 50, 250, 500]]
    #将x从小到大排序 且time_list也按照x的顺序排列
    x, time_list = zip(*sorted(zip(x, time_list))) #zip()将x和time_list打包成元组，sorted() 按照x的大小排序，zip(*)解压
    x = list(x)
    time_list = list(time_list)
    plt.plot(x, time_list)
    plt.xlabel(r'$n\times c$')
    plt.ylabel('Running time')
    plt.title('Complexity Analysis')
    plt.show()

def improved_dp_for01():
    w=[0,2,3,4,2]
    v=[0,3,6,9,7]
    c=5
    n=len(w)-1
    p,head=knapsack2(n,c,w,v)
    x=Traceback(n,w,v,p,head)
    print('物品重量：', w[1:])
    print('物品价值：', v[1:])
    print('最大价值为：', p[head[n+1]-1][1])
    print('装入背包的物品编号为：')
    for i in range(1,len(x)):
        if x[i]:
            print(i, ' ', end='')



def main():
    normal_dp_for01()
    normal_dp_complex_anlysis()
    improved_dp_for01()


if  __name__ == '__main__':
    main()

