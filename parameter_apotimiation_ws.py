# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 11:30:57 2018

@author: Administrator

regart：两个变量的PSO算法
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
            self.X[i][0] = int(random.uniform(11,199))#ws模拟网络的第二个参数
            self.X[i][1] = random.uniform(0,1)#ws模拟网络的第三个参数            
            self.V[i] = random.uniform(0,1) 
            self.pbest[i] = self.X[i]             
            tmp = get_auc.get_auc_lhi(int(self.X[i][0]),self.X[i][1])#计算初始化AUC值
            self.p_fit[i] = tmp
            if tmp > self.fit: 
                self.fit = tmp
                self.gbest = self.X[i]
#----------------------更新粒子位置----------------------------------
    def iterator(self):
        fitness = []
        weight=[]
        auc=[]
        x=[]
        y=[]
        for t in range(self.max_iter):
            for i in range(self.pN): 
                #更新gbest/pbest
                if 0<self.X[i][1]<1:
                    self.X[i][0]=int(self.X[i][0])
                    self.pbest[i] = self.X[i]   
                    temp = get_auc.get_auc_lhi(int(self.X[i][0]),self.X[i][1])
                    auc.append(temp)
                    x.append(self.X[i][0])
                    y.append(self.X[i][1])
                    if temp>self.p_fit[i]:
                     #更新个体最优
                         self.p_fit[i] = temp
                         self.pbest[i] = self.X[i]
                    if self.p_fit[i] > self.fit:
                    #更新全局最优                
                        self.fit = self.p_fit[i]
                        self.gbest = self.X[i]
                else:
                    pass
                self.V[i] = self.w*self.V[i]+self.c1*self.r1*(self.pbest[i]-self.X[i])+self.c2*self.r2*(self.gbest-self.X[i])
                self.X[i] = self.X[i] + self.V[i]
                self.X[i][0]=int(self.X[i][0])
            weight.append(self.gbest)
            fitness.append(self.fit) 
        print(self.fit,self.gbest)
        return fitness,weight,x,y,auc#输出最优值
#----------------------程序执行----------------------- 
my_pso = PSO(pN=50,dim=2,max_iter=5) 
my_pso.init_Population()
fitness,weight,x,y,auc = my_pso.iterator()
#-------------------画图--------------------
#考虑邻居节点数对AUC的影响
plt.figure(1)
plt.xlabel("", size=14) 
plt.ylabel("auc", size=14) 
plt.scatter(x,auc, color='b',linewidth=1) 
plt.grid(alpha=0.5,which= 'major')
plt.show()
#考虑重连概率对AUC的影响
plt.figure(1)
plt.xlabel("", size=14) 
plt.ylabel("auc", size=14) 
plt.scatter(y,auc, color='b',linewidth=1) 
plt.grid(alpha=0.5,which= 'major')
plt.show()
#联合三维图
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
plt.xlabel("n", size=14) 
plt.ylabel("p", size=14)
ax.plot_trisurf(x, y, auc,cmap=plt.get_cmap('rainbow'))
plt.grid(alpha=0.5,which= 'major')
ax.contourf(x,y,auc,zdir='auc',offset=-2) 
plt.show()

