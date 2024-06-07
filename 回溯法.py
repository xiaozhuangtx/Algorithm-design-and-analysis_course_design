class Knap:
    def __init__(self):
        self.c = 0  #背包容量
        self.n = 0  #物品个数
        self.w = [] #物品重量
        self.p = [] #物品价值
        self.cw = 0 #当前重量
        self.cp = 0 #当前价值
        self.bestp = 0 #当前最优价值
        self.x = []
    def Backtrack(self, i):
        if i > self.n:
            self.bestp = self.cp
            return
        if self.cw + self.w[i] <= self.c:
            self.x[i] = 1
            self.cw += self.w[i]
            self.cp += self.p[i]
            self.Backtrack(i + 1)
            self.cw -= self.w[i]
            self.cp -= self.p[i]
        if self.Bound(i + 1) > self.bestp:
            self.Backtrack(i + 1)
    def Bound(self, i):
        cleft = self.c - self.cw
        b = self.cp
        while i <= self.n and self.w[i] <= cleft:
            cleft -= self.w[i]
            b += self.p[i]
            i += 1
        if i <= self.n:
            b += self.p[i] / self.w[i] * cleft
        return b

    def main(self):
        k = Knap()
        w = [0, 3,5,2,1]
        p = [0, 9.5,10.5,7.5,2]
        c = 7
        n = len(w) - 1
        k.c = c
        k.n = n
        k.w = w
        k.p = p
        k.x=[0 for i in range(n + 1)]
        k.Backtrack(1)
        print('最大价值：', k.bestp)
        print('背包选择：', k.x[1:])


if __name__ == '__main__':
    Knap().main()
