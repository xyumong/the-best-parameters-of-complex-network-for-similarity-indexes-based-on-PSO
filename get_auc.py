# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 14:14:10 2018

@author: Administrator

regart:计算文件的AUC值
"""


from __future__ import division#精确除法（使用'/'时，保留小数）
from Evaluation_Indicators import Calculation_AUC
import similarity_indicators.LHN_I
import similarity_indicators.PA
import similarity_indicators.mixture_index
import get_netfile
import Initialize


def get_auc_pa(m):
    NetFile,NetName = get_netfile.get_ba_netfile(m)
    MatrixAdjacency_Net,MaxNodeNum = Initialize.Init(NetFile)
    MatrixAdjacency_Train,MatrixAdjacency_Test = Initialize.Divide(NetFile, MatrixAdjacency_Net, MaxNodeNum,NetName)    
    Matrix_similarity = similarity_indicators.PA.PA(MatrixAdjacency_Train)
    auc=Calculation_AUC(MatrixAdjacency_Train, MatrixAdjacency_Test, Matrix_similarity, MaxNodeNum)               
    return auc

def get_auc_lhi(n,p):
    NetFile,NetName = get_netfile.get_ws_netfile(n,p)
    MatrixAdjacency_Net,MaxNodeNum = Initialize.Init(NetFile)
    MatrixAdjacency_Train,MatrixAdjacency_Test = Initialize.Divide(NetFile, MatrixAdjacency_Net, MaxNodeNum,NetName)    
    Matrix_similarity = similarity_indicators.LHN_I.LHN_I(MatrixAdjacency_Train)
    auc=Calculation_AUC(MatrixAdjacency_Train, MatrixAdjacency_Test, Matrix_similarity, MaxNodeNum)               
    return auc



