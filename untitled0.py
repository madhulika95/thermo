# -*- coding: utf-8 -*-
"""
Created on Sun May 01 12:27:30 2016

@author: Madhu
"""

import pandas as pd
import numpy as np

'''df=pd.read__csv('ExamProblemData.csv')
time=np.array(df[[0]]);
time=np.reshape(time,(time.shape[0],))
print time'''

data=pd.read_excel('C:/Users/Madhu/Desktop/xxx/ExamProblemData.xlsx')
time=data["Col1"].values 
time=time.astype(np.int)
print time

