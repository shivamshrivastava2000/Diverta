# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 22:10:24 2021

@author: Win10
"""

import pandas as pd
import os
def comment_viewer():
    
    data = pd.read_csv('Comments.csv',index_col=0)
    if(data.shape[0]==0):
        print("No Comments")
    else:
        print("Comments are:\n")
    for index in data.index:
        
        print(f"{index}. {data['UserName'][index]}: {data['Comment'][index]} - ({data['TimeStamp'][index]})")
        
        if (os.path.exists(f"Comments{index}.csv")):
            data1 = pd.read_csv(f"Comments{index}.csv",index_col=0)
            
            print("Replies are:")
            for index1 in data1.index:
                print(f"{index}.{index1} . {data1['UserName'][index1]}: {data1['Reply'][index1]} - ({data1['TimeStamp'][index1]})")
        else:
            print("No Replies")
        
        print("\n")            