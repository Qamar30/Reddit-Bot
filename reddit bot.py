

import praw
import time

bot = praw.Reddit(user_agent='',
                  client_id='',
                  client_secret='',
                  username='',
                  password='')

subreddit = bot.subreddit('sports')

hot_python = subreddit.hot(limit=3)
for submission in hot_python:
    if not submission.stickied:
        print('Title: {}, ups: {}, downs: {}, Have we visited?: {}, subid: {}'.format(submission.title,
                                                                                                   submission.ups,
                                                                                                   submission.downs,
                                                                                                   submission.visited,
                                                                                                   submission.id))
        submission.comments.replace_more(limit=0)
      
        for comment in submission.comments.list()[:15]:
            print(20*'#')
            print('Parent ID:',comment.parent())
            print('Comment ID:',comment.id)
           








