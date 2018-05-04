# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 17:35:55 2017

@author: Administrator
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 14:29:13 2017

@author: Administrator
"""

import similarity_indicators.CN
import similarity_indicators.Salton
import similarity_indicators.Jaccard
import similarity_indicators.Sorenson
import similarity_indicators.HPI
import similarity_indicators.HDI
import similarity_indicators.LHN_I
import similarity_indicators.PA
import similarity_indicators.AA


def mixture_index_1(MatrixAdjacency_Train):
    sim_1=similarity_indicators.PA.PA(MatrixAdjacency_Train)
    sim_2=similarity_indicators.LHN_I.LHN_I(MatrixAdjacency_Train)
    sim_3=similarity_indicators.CN.CN(MatrixAdjacency_Train)

    Matrix_similarity=(1/3)*sim_1+(1/3)*sim_2+(1/3)*sim_3
    return Matrix_similarity


def mixture_index_2(MatrixAdjacency_Train):
    sim_1=similarity_indicators.AA.AA(MatrixAdjacency_Train)
    sim_2=similarity_indicators.Jaccard.Jaccavrd(MatrixAdjacency_Train)
    sim_3=similarity_indicators.HPI.HPI(MatrixAdjacency_Train)

    Matrix_similarity=(1/3)*sim_1+(1/3)*sim_2+(1/3)*sim_3
    return Matrix_similarity


def mixture_index_3(MatrixAdjacency_Train):
    sim_1=similarity_indicators.Salton.Salton(MatrixAdjacency_Train)
    sim_2=similarity_indicators.LHN_I.LHN_I(MatrixAdjacency_Train)
    sim_3=similarity_indicators.HDI.HDI(MatrixAdjacency_Train)

    Matrix_similarity=(1/3)*sim_1+(1/3)*sim_2+(1/3)*sim_3
    return Matrix_similarity



