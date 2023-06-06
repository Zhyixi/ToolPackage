# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 16:24:46 2023

@author: ur08366
"""
import os, gc, itertools

class PathManipulation():
    
    def __init__(self):
        pass
    
    @staticmethod
    def get_path(folder_path,advFileName=".xlsx"):
        # 設置指定路徑
        original_path = os.getcwd()
        # 進入指定路徑
        os.chdir(folder_path)
        # 獲取所有檔案名稱列表，不包含隱藏檔案
        file_names = [os.path.join(folder_path, f) for f in os.listdir() if "~$" not in f and f.endswith(advFileName)]
        # 切換回原本的工作目錄
        os.chdir(original_path)
        return file_names