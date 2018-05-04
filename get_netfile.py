# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 15:53:46 2018

@author: Administrator

regart:根据PSO算法随机生成的参数生成网络连边文件
"""

import networkx as nx
import pandas as pd
'''for m in range(101,200,5):
    BA = nx.random_graphs.barabasi_albert_graph(200,m)    
    l=[]
    ba=nx.to_numpy_matrix(BA)
    ba=pd.DataFrame(ba)
    for i in range(200):
        for j in range(200):
            if ba[i][j] == 1:
                l.append((i,j))
    with open(r'E:\数据\模拟网络\BA\ba_200_'+str(m)+'.txt','w') as fh:
        for link in l:
            link=str(link)
            link=link.replace('[','')
            link=link.replace(']','')
            link=link.replace('(','')
            link=link.replace(')','')
            link=link.replace("'",'')
            link=link.replace(",",'   ')
            fh.write(link+'\n')


import networkx as nx
import pandas as pd
import numpy as np

for m in np.arange(0,1,0.1) :
    WS=nx.random_graphs.watts_strogatz_graph(1000,40,m)    
    l=[]
    ws=nx.to_numpy_matrix(WS)
    ws=pd.DataFrame(ws)
    for i in range(1000):
        for j in range(1000):
            if ws[i][j] == 1:
                l.append((i,j))
    with open(r'E:\数据\模拟网络\WS\ws_1000_40_'+str(m)+'.txt','w') as fh:
        for link in l:
            link=str(link)
            link=link.replace('[','')
            link=link.replace(']','')
            link=link.replace('(','')
            link=link.replace(')','')
            link=link.replace("'",'')
            link=link.replace(",",'   ')
            fh.write(link+'\n')'''


def get_ba_netfile(m):
    BA = nx.random_graphs.barabasi_albert_graph(200,m)    
    l=[]
    ba=nx.to_numpy_matrix(BA)
    ba=pd.DataFrame(ba)
    for i in range(200):
        for j in range(200):
            if ba[i][j] == 1:
                l.append((i,j))
    with open(r'E:\数据\模拟网络\BA\ba_200_'+str(m)+'.txt','w') as fh:
        for link in l:
            link=str(link)
            link=link.replace('[','')
            link=link.replace(']','')
            link=link.replace('(','')
            link=link.replace(')','')
            link=link.replace("'",'')
            link=link.replace(",",'   ')
            fh.write(link+'\n')
    NetFile=r'E:\数据\模拟网络\BA\ba_200_'+str(m)+'.txt'
    NetName = 'ba_200_'+str(m)
    return NetFile,NetName

def get_ws_netfile(n,p):
    WS=nx.random_graphs.watts_strogatz_graph(200,n,p)    
    l=[]
    ws=nx.to_numpy_matrix(WS)
    ws=pd.DataFrame(ws)
    for i in range(200):
        for j in range(200):
            if ws[i][j] == 1:
                l.append((i,j))
    with open(r'E:\数据\模拟网络\WS\ws_200_'+str(n)+'_'+str(p)+'.txt','w') as fh:
        for link in l:
            link=str(link)
            link=link.replace('[','')
            link=link.replace(']','')
            link=link.replace('(','')
            link=link.replace(')','')
            link=link.replace("'",'')
            link=link.replace(",",'   ')
            fh.write(link+'\n')
    NetFile=r'E:\数据\模拟网络\WS\ws_200_'+str(n)+'_'+str(p)+'.txt'
    NetName = 'ws_200_'+str(n)+'_'+str(p)
    return NetFile,NetName

