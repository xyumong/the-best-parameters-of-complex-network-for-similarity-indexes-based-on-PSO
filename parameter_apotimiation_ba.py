# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 20:27:31 2018

@author: Administrator

regart:一个变量的PSO优化算法（BA）
"""
import numpy as np
import random 
import matplotlib.pyplot as plt
import get_auc


 #----------------------PSO参数设置---------------------------------
class PSO():
    def __init__(self,pN,dim,max_iter): 
        self.w = 0.8
        self.c1=2
        self.c2=2
        self.r1=0.6
        self.r2=0.3
        self.pN=pN#粒子数
        self.dim = dim#搜索维度
        self.max_iter=max_iter#最大迭代次数
        self.X = np.zeros((self.pN,self.dim))#所有粒子的位置
        self.V = np.zeros((self.pN,self.dim)) #所有粒子的速度
        self.pbest = np.zeros((self.pN,self.dim))#个体经历的最佳位置
        self.gbest = np.zeros((1,self.dim))#全局最佳位置
        self.p_fit = np.zeros(self.pN) #每个个体的历史最佳适应值
        self.fit = 0.5#全局最佳适应值

#---------------------初始化种群---------------------------------- 
    def init_Population(self): 
        for i in range(self.pN): 
            self.X[i] = random.uniform(11,199)
            self.V[i] = random.uniform(0,1) 
            self.pbest[i] = self.X[i]             
            tmp = get_auc.get_auc_pa(int(self.X[i]))
            self.p_fit[i] = tmp
            if tmp > self.fit: 
                self.fit = tmp
                self.gbest = self.X[i]
#----------------------更新粒子位置----------------------------------
    def iterator(self):
        fitness = []
        weight=[]
        auc=[]
        n=[]
        for t in range(self.max_iter):
            for i in range(self.pN): 
                #更新gbest/pbest
                if int(self.X[i])<200:                    
                    self.pbest[i] = int(self.X[i])                
                    temp = get_auc.get_auc_pa(int(self.X[i]))
                    auc.append(temp)
                    n.append(int(self.X[i]))
                else:
                    break
                if temp>self.p_fit[i]:
                     #更新个体最优
                     self.p_fit[i] = temp
                     self.pbest[i] = int(self.X[i])
                if self.p_fit[i] > self.fit:
                    #更新全局最优                
                    self.fit = self.p_fit[i]
                    self.gbest = int(self.X[i])
                self.V[i] = self.w*self.V[i]+self.c1*self.r1*(self.pbest[i]-self.X[i])+self.c2*self.r2*(self.gbest-self.X[i])
                self.X[i] = self.X[i] + self.V[i]
            weight.append(self.gbest)
            fitness.append(self.fit) 
        print(self.fit,self.gbest)
        return fitness,weight,n,auc#输出最优值
#----------------------程序执行----------------------- 
my_pso = PSO(pN=5,dim=1,max_iter=10) 
my_pso.init_Population()
fitness,weight,n,auc = my_pso.iterator()
#-------------------画图--------------------
plt.figure(1)
plt.xlabel("n", size=14) 
plt.ylabel("auc", size=14) 
plt.plot(n,auc, color='b',linewidth=3) 
plt.grid(alpha=0.5,which= 'major')
plt.show()