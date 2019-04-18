import praw
import pdb
import re
import time
import os
import csv

subs = []
sub=' '
i = 0
#open csv file of various subs
with open('subs.csv') as f:
    readCSV = csv.reader(f, delimiter='\n')
    for row in readCSV:
        subs.append(row)

# Create the Reddit instance and log in
reddit = praw.Reddit(client_id='d7X8ZlU7VSHIfw',
                    client_secret='7KDD5L-R-i4GEBaxV_9v2EwzA_k',
                    user_agent='<console:MobileScoutBot:0.0.1 (by /u/apgearhart1)>',
                    username='apgearhart1',
                    password='Freckles0729!')


#reddit.login(username, password)




keywords = subs

def run(reddit, comments_replied):
    print("Obtaining 30 comments...\n")
    for comment in reddit.subreddit('all').comments(limit=30):
        if 'R/' in comment.body:
            if comment.id not in comments_replied and comment.author != reddit.user.me():
                r = comment.body.find('R')
                s = comment.body.find('/')
                if s - r == 1:
                    locate_space = comment.body.find(' ', s)
                    bot_phrase = "/r/"+sub[s:locate_space] + " -- Some people don't know how to link subreddits these days."
                    print("Capital R found while linking subs \n")
                    comment.reply(bot_phrase)
                    print("Replied to comment", comment.id)





comments_replied = []

while 1:
    run(reddit, comments_replied)