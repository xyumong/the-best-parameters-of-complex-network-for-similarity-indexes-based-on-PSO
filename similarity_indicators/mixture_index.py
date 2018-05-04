# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 14:29:13 2017

@author: Administrator
"""

import numpy as np
import similarity_indicators.CN
import similarity_indicators.Salton
import similarity_indicators.Jaccard
import similarity_indicators.Sorenson
import similarity_indicators.HPI
import similarity_indicators.HDI
import similarity_indicators.LHN_I
import similarity_indicators.PA
import similarity_indicators.AA

data_31=[[0.873,0.780,0.716,0.664,0.619,0.579,0.542,0.508,0.476,0.446,0.418,0.391,0.365,0.340,0.316,0.293,0.270,0.249,0.227,0.207,0.187,0.167,0.148,0.129,0.111,0.093,0.075,0.058,0.041,0.024,0.008],
      [0.080,0.053,0.243,0.157,0.031,0.292,0.140,0.452,0.279,0.080,0.441,0.226,0.625,0.394,0.143,0.582,0.318,0.036,0.511,0.217,0.721,0.416,0.096,0.632,0.301,0.863,0.522,0.167,0.758,0.393,0.016],
      [0.047,0.167,0.041,0.179,0.350,0.129,0.318,0.040,0.245,0.473,0.141,0.383,0.010,0.266,0.541,0.125,0.412,0.715,0.262,0.576,0.092,0.416,0.756,0.239,0.588,0.044,0.403,0.775,0.201,0.582,0.976]]
data_19=[[0.838,0.719,0.637,0.571,0.513,0.462,0.415,0.372,0.331,0.293,0.257,0.222,0.189,0.157,0.126,0.097,0.068,0.040,0.013],
         [0.098,0.052,0.277,0.147,0.448,0.269,0.046,0.413,0.158,0.577,0.293,0.758,0.448,0.111,0.621,0.261,0.809,0.429,0.026],
         [0.064,0.229,0.086,0.282,0.038,0.269,0.539,0.215,0.510,0.130,0.450,0.020,0.363,0.732,0.253,0.642,0.123,0.530,0.961]]
data_11=[[0.787,0.631,0.523,0.436,0.360,0.293,0.231,0.174,0.121,0.071,0.023],
         [0.087,0.285,0.065,0.282,0.552,0.161,0.454,0.788,0.280,0.634,0.044],
         [0.126,0.084,0.412,0.282,0.087,0.546,0.314,0.038,0.599,0.296,0.933]]


test= np.array(data_19).T.reshape(19,3)

def mixture_index_1(MatrixAdjacency_Train):
    sim_1=similarity_indicators.AA.AA(MatrixAdjacency_Train)
    sim_2=similarity_indicators.CN.CN(MatrixAdjacency_Train)
    sim_3=similarity_indicators.PA.PA(MatrixAdjacency_Train)
    Matrix_similarity=test[0][0]*sim_1+test[0][1]*sim_2+test[0][2]*sim_3
    return Matrix_similarity

def mixture_index_2(MatrixAdjacency_Train):
    sim_1=similarity_indicators.AA.AA(MatrixAdjacency_Train)
    sim_2=similarity_indicators.CN.CN(MatrixAdjacency_Train)
    sim_3=similarity_indicators.PA.PA(MatrixAdjacency_Train)
    Matrix_similarity=test[1][0]*sim_1+test[1][1]*sim_2+test[1][2]*sim_3
    return Matrix_similarity

def mixture_index_3(MatrixAdjacency_Train):
    sim_1=similarity_indicators.AA.AA(MatrixAdjacency_Train)
    sim_2=similarity_indicators.CN.CN(MatrixAdjacency_Train)
    sim_3=similarity_indicators.PA.PA(MatrixAdjacency_Train)
    Matrix_similarity=test[2][0]*sim_1+test[2][1]*sim_2+test[2][2]*sim_3
    return Matrix_similarity

def mixture_index_4(MatrixAdjacency_Train):
    sim_1=similarity_indicators.AA.AA(MatrixAdjacency_Train)
    sim_2=similarity_indicators.CN.CN(MatrixAdjacency_Train)
    sim_3=similarity_indicators.PA.PA(MatrixAdjacency_Train)
    Matrix_similarity=test[3][0]*sim_1+test[3][1]*sim_2+test[3][2]*sim_3
    return Matrix_similarity

def mixture_index_5(MatrixAdjacency_Train):
    sim_1=similarity_indicators.AA.AA(MatrixAdjacency_Train)
    sim_2=similarity_indicators.CN.CN(MatrixAdjacency_Train)
    sim_3=similarity_indicators.PA.PA(MatrixAdjacency_Train)
    Matrix_similarity=test[4][0]*sim_1+test[4][1]*sim_2+test[4][2]*sim_3
    return Matrix_similarity

def mixture_index_6(MatrixAdjacency_Train):
    sim_1=similarity_indicators.AA.AA(MatrixAdjacency_Train)
    sim_2=similarity_indicators.CN.CN(MatrixAdjacency_Train)
    sim_3=similarity_indicators.PA.PA(MatrixAdjacency_Train)
    Matrix_similarity=test[5][0]*sim_1+test[5][1]*sim_2+test[5][2]*sim_3
    return Matrix_similarity

def mixture_index_7(MatrixAdjacency_Train):
    sim_1=similarity_indicators.AA.AA(MatrixAdjacency_Train)
    sim_2=similarity_indicators.CN.CN(MatrixAdjacency_Train)
    sim_3=similarity_indicators.PA.PA(MatrixAdjacency_Train)
    Matrix_similarity=test[6][0]*sim_1+test[6][1]*sim_2+test[6][2]*sim_3
    return Matrix_similarity

def mixture_index_8(MatrixAdjacency_Train):
    sim_1=similarity_indicators.AA.AA(MatrixAdjacency_Train)
    sim_2=similarity_indicators.CN.CN(MatrixAdjacency_Train)
    sim_3=similarity_indicators.PA.PA(MatrixAdjacency_Train)
    Matrix_similarity=test[7][0]*sim_1+test[7][1]*sim_2+test[7][2]*sim_3
    return Matrix_similarity

def mixture_index_9(MatrixAdjacency_Train):
    sim_1=similarity_indicators.AA.AA(MatrixAdjacency_Train)
    sim_2=similarity_indicators.CN.CN(MatrixAdjacency_Train)
    sim_3=similarity_indicators.PA.PA(MatrixAdjacency_Train)
    Matrix_similarity=test[8][0]*sim_1+test[8][1]*sim_2+test[8][2]*sim_3
    return Matrix_similarity

def mixture_index_10(MatrixAdjacency_Train):
    sim_1=similarity_indicators.AA.AA(MatrixAdjacency_Train)
    sim_2=similarity_indicators.CN.CN(MatrixAdjacency_Train)
    sim_3=similarity_indicators.PA.PA(MatrixAdjacency_Train)
    Matrix_similarity=test[9][0]*sim_1+test[9][1]*sim_2+test[9][2]*sim_3
    return Matrix_similarity

def mixture_index_11(MatrixAdjacency_Train):
    sim_1=similarity_indicators.AA.AA(MatrixAdjacency_Train)
    sim_2=similarity_indicators.CN.CN(MatrixAdjacency_Train)
    sim_3=similarity_indicators.PA.PA(MatrixAdjacency_Train)
    Matrix_similarity=test[10][0]*sim_1+test[10][1]*sim_2+test[10][2]*sim_3
    return Matrix_similarity

def mixture_index_12(MatrixAdjacency_Train):
    sim_1=similarity_indicators.AA.AA(MatrixAdjacency_Train)
    sim_2=similarity_indicators.CN.CN(MatrixAdjacency_Train)
    sim_3=similarity_indicators.PA.PA(MatrixAdjacency_Train)
    Matrix_similarity=test[11][0]*sim_1+test[11][1]*sim_2+test[11][2]*sim_3
    return Matrix_similarity

def mixture_index_13(MatrixAdjacency_Train):
    sim_1=similarity_indicators.AA.AA(MatrixAdjacency_Train)
    sim_2=similarity_indicators.CN.CN(MatrixAdjacency_Train)
    sim_3=similarity_indicators.PA.PA(MatrixAdjacency_Train)
    Matrix_similarity=test[12][0]*sim_1+test[12][1]*sim_2+test[12][2]*sim_3
    return Matrix_similarity

def mixture_index_14(MatrixAdjacency_Train):
    sim_1=similarity_indicators.AA.AA(MatrixAdjacency_Train)
    sim_2=similarity_indicators.CN.CN(MatrixAdjacency_Train)
    sim_3=similarity_indicators.PA.PA(MatrixAdjacency_Train)
    Matrix_similarity=test[13][0]*sim_1+test[13][1]*sim_2+test[13][2]*sim_3
    return Matrix_similarity

def mixture_index_15(MatrixAdjacency_Train):
    sim_1=similarity_indicators.AA.AA(MatrixAdjacency_Train)
    sim_2=similarity_indicators.CN.CN(MatrixAdjacency_Train)
    sim_3=similarity_indicators.PA.PA(MatrixAdjacency_Train)
    Matrix_similarity=test[14][0]*sim_1+test[14][1]*sim_2+test[14][2]*sim_3
    return Matrix_similarity

def mixture_index_16(MatrixAdjacency_Train):
    sim_1=similarity_indicators.AA.AA(MatrixAdjacency_Train)
    sim_2=similarity_indicators.CN.CN(MatrixAdjacency_Train)
    sim_3=similarity_indicators.PA.PA(MatrixAdjacency_Train)
    Matrix_similarity=test[15][0]*sim_1+test[15][1]*sim_2+test[15][2]*sim_3
    return Matrix_similarity

def mixture_index_17(MatrixAdjacency_Train):
    sim_1=similarity_indicators.AA.AA(MatrixAdjacency_Train)
    sim_2=similarity_indicators.CN.CN(MatrixAdjacency_Train)
    sim_3=similarity_indicators.PA.PA(MatrixAdjacency_Train)
    Matrix_similarity=test[16][0]*sim_1+test[16][1]*sim_2+test[16][2]*sim_3
    return Matrix_similarity

def mixture_index_18(MatrixAdjacency_Train):
    sim_1=similarity_indicators.AA.AA(MatrixAdjacency_Train)
    sim_2=similarity_indicators.CN.CN(MatrixAdjacency_Train)
    sim_3=similarity_indicators.PA.PA(MatrixAdjacency_Train)
    Matrix_similarity=test[17][0]*sim_1+test[17][1]*sim_2+test[17][2]*sim_3
    return Matrix_similarity

def mixture_index_19(MatrixAdjacency_Train):
    sim_1=similarity_indicators.AA.AA(MatrixAdjacency_Train)
    sim_2=similarity_indicators.CN.CN(MatrixAdjacency_Train)
    sim_3=similarity_indicators.PA.PA(MatrixAdjacency_Train)
    Matrix_similarity=test[18][0]*sim_1+test[18][1]*sim_2+test[18][2]*sim_3
    return Matrix_similarity




