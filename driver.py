# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 10:13:03 2021

@author: Win10
"""

import pandas as pd
import os
from add_comments import comment_adder
from view_comments import comment_viewer
from reply_comments import comment_replier
from search_comments import comment_searcher



def driver():
    
    print("Here are the choices\n")
    print("1 - add comment\n")
    print("2 - view comments\n")
    print("3 - reply to comments\n")
    print("4 - search for comments\n")
    print("5 - exit")
    
    filename = "Comments"
    df = pd.DataFrame(columns=['UserName','Comment','TimeStamp','Replies','Keywords'])
    if not(os.path.exists(f"{filename}.csv")):
        df.to_csv('Comments.csv',index='False')
    
    
    choice="0"
    
    while(choice!="5"):
        
        
        choice = input("Enter your choice: ")
        
        if(choice == "1"): 
            comment_adder()
            
        elif(choice == "2"):
            comment_viewer()
            
        elif(choice == "3"):
            print("Select index of the comment you want to reply to: ")
            comment_viewer()
            qindex = input("Enter index of the comment you want to reply to: ")
            comment_replier(qindex)
            
        elif(choice == "4"):
            comment_searcher()
            
        else:
            print("Thankyou!")
            break;
        print("Here are the choices\n")
        print("1 - add comment\n")
        print("2 - view comments and replies\n")
        print("3 - reply to comments\n")
        print("4 - search for comments\n")
        print("5 - exit") 

driver()               
            
            
            
    
    
    
    