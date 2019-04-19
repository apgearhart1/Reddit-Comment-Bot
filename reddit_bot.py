import praw
import pdb
import re
import time
import os
import csv
#link for finding reddit comment data https://www.reddit.com/api/info.json?id=t1_<id>
subs = []
sub=' '
i = 0
#open csv file of various subs
with open('subs.csv') as f:
    readCSV = csv.reader(f, delimiter='\n')
    for row in readCSV:
        subs.append(row)

# Create the Reddit instance and log in
reddit = praw.Reddit(client_id='B3dcYGjak4DUHw',
                    client_secret='LiHxe8oEZc6dz3V_v0vmmdvOBTM',
                    user_agent='<console:MobileScoutBot:0.0.1 (by /u/apgearhart1)>',
                    username='Mobile_Scout_Bot',
                    password='Thecatgoesquack')
print("Logged In!")


#reddit.login(username, password)






def run(reddit, comments_replied):
    print("Searching through comments...\n")
    for comment in reddit.subreddit('all').stream.comments(): #change which subreddits to check
        sub = comment.body
        if 'R/' in sub:
            if comment.id not in comments_replied and comment.author != reddit.user.me():
                r = comment.body.find('R')
                s = comment.body.find('/')
                if s - r == 1: #check if R and / are next to each other
                    
                    locate_space = comment.body.find(' ', r)
                    found = sub[s+1:locate_space] #forms the subreddit string
                    print(found)
                    if found not in subs:
                        subs.append(found)
                        with open('subs.csv', 'a') as f:
                            f.write(found + '\n')
                    print("Mobile User Found!\n")
                    bot_phrase = "/r/"+ found + " -- Some people don't know how to link subreddits these days."
                    print("Capital R found while linking subs \n")
                    comment.reply(bot_phrase)
                    print("Replied to comment", comment.id)
                    comments_replied.append(comment.id)       


                        
                      
                    with open('replies.txt', 'a') as fr:
                        fr.write(comment.id + '\n')
    time.sleep(420) #7 minute intervals so it doesn't spam




def get_replies():
    if not os.path.isfile('replies.txt'):
        print("Creating array of ids")
        replied_to = []
    else:
        with open('replies.txt', 'r') as fr:
            replied_to = fr.read()
            replied_to = replied_to.split('\n')
    return replied_to


comments_replied = get_replies()

while 1:
    run(reddit, comments_replied)