# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 22:47:49 2021

@author: Win10
"""

import pandas as pd
import re
import math
from reply_comments import comment_replier
def comment_searcher():
    
    data = pd.read_csv('Comments.csv',index_col=0)
    
    print("Here are the choices\n")
    print("1 - Search by UserName\n")
    print("2 - Search by Comment Text\n")
    print("3 - Quick Search by Keyword\n")
    print("4 - Search by TimeStamp\n")
    
    
    choice = input("Enter choice: ")
    
    if(choice == "1"):
        qusername = input("Enter Username to be searched: ")
        flag=0
        for index in data.index:
            if(data['UserName'][index] == qusername):
                print(f"{index}. {data['UserName'][index]}: {data['Comment'][index]} - ({data['TimeStamp'][index]}) \n")
                flag=1
        if (flag==0):
            print("Not Found")
        else:
                qchoice = input("Do you want to reply to any of these comments? (Yes/No)")
                if( qchoice == "Yes"):
                    qindex = input("Enter the index of the comment you want to reply to")
                    comment_replier( qindex )    
                
        
      
    elif(choice == "2"):
        qtext =input("Enter text to be searched: ")
        flag=0
        for index in data.index:
            if re.search( qtext , data['Comment'][index]):
                print(f"{index}. {data['UserName'][index]}: {data['Comment'][index]} - ({data['TimeStamp'][index]}) \n")
                flag=1
        if(flag==0):
            print("Not Found")
        else:
                qchoice = input("Do you want to reply to any of these comments? (Yes/No)")
                if( qchoice == "Yes"):
                    qindex = input("Enter the index of the comment you want to reply to")
                    comment_replier( qindex )    
                
                
    elif(choice == "3"):
        qkey = input("Enter Keyword to be searched: ")
        flag=0
        for index in data.index:
            if qkey in data['Keywords'][index]:
                print(f"{index}. {data['UserName'][index]}: {data['Comment'][index]} - ({data['TimeStamp'][index]}) \n")
                flag=1
        if(flag==0):
            print("Not Found")
        else:
            qchoice = input("Do you want to reply to any of these comments? (Yes/No)")
            if( qchoice == "Yes"):
                qindex = input("Enter the index of the comment you want to reply to")
                comment_replier( qindex )
            
                
    else:
        qtime = input(str("Enter TimeStamp to be searched in the format YYYY-MM-DD HH:MM:SS :: "))
        lo = 0
        hi = data.shape[0]-1
        
        ans=-1
        while(lo<=hi):
            mid = math.floor((lo+hi)/2)
            if( data['TimeStamp'][mid] == qtime):
                ans=mid
                break
            elif( data['TimeStamp'][mid] > qtime):
                hi = mid-1
            else:
                lo = mid+1
 
        if(ans==-1):
             print("Not Found")
        else:
             print(f"{ans}. {data['UserName'][ans]}: {data['Comment'][ans]} - ({data['TimeStamp'][ans]}) \n")
                            
        if(ans!=-1):
            qchoice = input("Do you want to reply to any of these comments? (Yes/No)")
            if( qchoice == "Yes"):
                qindex = input("Enter the index of the comment you want to reply to")
                comment_replier( qindex )
                
                
            
        
        
        
                
                
                