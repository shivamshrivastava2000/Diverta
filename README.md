# Diverta
Simple Console App for Comment Management

I have designed a very simple console application for Comment Management in Python from Scratch.
I believe my application uses optimal memory and time to cover all the requirements of the application (except MultiMedia Management)

This repository comprises 5 .py files namely :

1. driver.py - This is the main file driving file of the application which performs basic interaction with the user. It calls other functions as and when necessary.
2. add_comments.py - This class is used for inserting comments in the application along with the Username and it also stores the timestamp of the comment.
3. view_comments.py - This class is used to display all the comments and the replies entered.
4. search_comments.py - This class searches for a particular comment by 4 different approaches :
                        a. Searching all Comments by UserName - This process takes O(N) time where N is the total number of comments.
                        b. Searching by Some Text - This process takes O(NxM) time where N is the number of Comments and M is the average length of a sentence.
                        c. Searching by Keywords - This process takes relatively less time than the previous method because I have already stored the Keywords of the comments                                                        separately using the NLTK library.
                        d. Seaching by TimeStamp - This process is the fastest and the most ideal because it takes O(log N) to search through the whole space. This is because I                                                      have used Binary Search to search for the entered timestamp making use of the fact that the timestamps are arranged in ascendig                                                      order always. 
5. reply_comments.py - This class is used to reply to a specific comment after entering the index number of the comment.
