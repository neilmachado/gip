import praw 
import time
import pyfiglet
import random 
import requests
import sys
from sys import exit



reddit = praw.Reddit(client_id="BQGsLJUHf1DQoQ", #14 letter key
                     client_secret="u9en5iZCkuqR0QuJGhw6nTBpZn2w-w", #27 letter key
                     password="Mobile-Leadership836",
                     user_agent="testscript by u/Mobile-Leadership836",
                     username="Mobile-Leadership836")
 
result = pyfiglet.figlet_format("Dylan OP") 
print(result) 

print("Starting Magic............")

print(reddit.user.me())

REDDIT_USERNAME=(reddit.user.me())

response = requests.get("https://www.reddit.com/user/{}/about.json".format(REDDIT_USERNAME),  headers = {'User-agent': 'hiiii its {}'.format(REDDIT_USERNAME)}).json()
if "error" in response:
 if response["error"] == 404:
      print("account {} is shadowbanned. poor bot :( shutting down the script...".format(REDDIT_USERNAME))
      sys.exit()
 else:
      print(response)
else:
    print("{} is not shadowbanned! We think..".format(REDDIT_USERNAME))

name = input("Enter a name : ") 

title = input("Enter an epic title: ") 
url = input("Enter a sassy link: ") 
comment = input ("Enter your comment : ")

title2 = input("Enter an epic title: ") 
url2 = input("Enter a sassy link: ") 
comment2 = input ("Enter your comment : ")

title3 = input("Enter an epic title: ") 
url3 = input("Enter a sassy link: ") 
comment3 = input ("Enter your comment : ")

print("Reading reddit list")
subredit_list = open("data.txt", "r")
subreddits = subredit_list.read().split(',')

for subreddit in subreddits:
  try:
    print(subreddit)
    reddit.validate_on_submit = True
    submission = reddit.subreddit(subreddit).submit(title,url=url)
    com = " #[Meg@]({}) {}".format(comment, name)
    time.sleep(10)
    submission.reply(com)
    print ("done")
  except Exception as err:
    print("Exception for subreddit {}, {}".format(subreddit, err))
  t= random.randint(815,1125)
  seconds = "Sleeping for {} seconds before proceeding".format(t)
  print(seconds)
  time.sleep(t)


print("Reading reddit list")
subredit_list = open("data.txt", "r")
subreddits = subredit_list.read().split(',')

for subreddit in subreddits:
  try:
    print(subreddit)
    reddit.validate_on_submit = True
    submission = reddit.subreddit(subreddit).submit(title2,url=url2)
    com = " #[Meg@]({}) {}".format(comment2, name)
    time.sleep(10)
    submission.reply(com)
    print ("done")
  except Exception as err:
    print("Exception for subreddit {}, {}".format(subreddit, err))
  t= random.randint(805,1025)
  seconds = "Sleeping for {} seconds before proceeding".format(t)
  print(seconds)
  time.sleep(t)


print("Reading reddit list")
subredit_list = open("data.txt", "r")
subreddits = subredit_list.read().split(',')

for subreddit in subreddits:
  try:
    print(subreddit)
    reddit.validate_on_submit = True
    submission = reddit.subreddit(subreddit).submit(title3,url=url3)
    com = " #[Meg@]({}) {}".format(comment3, name)
    time.sleep(10)
    submission.reply(com)
    print ("done")
  except Exception as err:
    print("Exception for subreddit {}, {}".format(subreddit, err))
  t= random.randint(815,1025)
  seconds = "Sleeping for {} seconds before proceeding".format(t)
  print(seconds)
  time.sleep(t)