# -*- coding: utf-8 -*-
"""
Created on Sun May 01 22:56:10 2016

@author: JUILI
"""
import scipy
import win32com.client
xl= win32com.client.gencache.EnsureDispatch('Excel.Application')
wb=xl.Workbooks('ExamProblemData.csv')
sheet=wb.Sheets('ExamProblemData')
   
def getdata(sheet, Range):
    data= sheet.Range(Range).Value
    #print data
    data=scipy.array(data)
    #print data
    #print data.shape
    #print len(data)
    data=data.reshape((1,len(data)))
    #print data
    #print data.shape
    return data
ydata=getdata(sheet,"A2:A11")
print ydata

