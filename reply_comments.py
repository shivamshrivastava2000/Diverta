# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 11:24:30 2021

@author: Win10
"""
import pandas as pd
from datetime import datetime
import os
def comment_replier(indexr):
    
       
    
    df = pd.DataFrame(columns=['UserName','Reply','TimeStamp'])
    if not(os.path.exists(f"Comments{indexr}.csv")):
        df.to_csv(f"Comments{indexr}.csv",index='False')
    
    data = pd.read_csv(f"Comments{indexr}.csv",index_col=0)
    
    username = input("Enter your UserName: ")
    
    reply = input("Enter your reply: ")
    
    t = datetime.now() 
    t = t.replace(microsecond=0)
    
    row = { "UserName" : username,
            "Reply": reply,
           "TimeStamp":t,
            }
    data = data.append(row, ignore_index=True)
    
    data.to_csv(f"Comments{indexr}.csv",index="False")
    