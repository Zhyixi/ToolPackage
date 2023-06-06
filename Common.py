# -*- coding: utf-8 -*-
"""
Created on Thu May  4 13:39:21 2023

@author: ur08366
"""
import time


class timeManipulate():
    def __init__(self):
        self.time_ticks = []
        self.time_start = None
        self.time_end = None
    
    def timeStart(self):
        self.time_start = time.time()
    
    def timeEnd(self):
        self.time_end = time.time()
        cost = self.time_end - self.time_start
        self.time_start = None
        self.time_end = None
        print(f"耗時:{cost:.2f}秒")

    
