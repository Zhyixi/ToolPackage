# -*- coding: utf-8 -*-
"""
Created on Wed May  3 09:27:44 2023

@author: ur08366
"""

import pandas as pd

class dataframeManipulate():
    def __init__(self):
        pass
    
    @staticmethod
    def compareColumns(*dfSet):
        """
            比較兩個df的欄位是否完全一致
        """
        res = []
        for i in range(1, len(dfSet)):
            tag = dfSet[i].columns.equals(dfSet[i-1].columns)
            res.append(tag)
        return all(res)