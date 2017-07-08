import praw
from random import randint # to serve a random gif from the gif file
import time
import config #read the config file


# credit to Stack Overflow user 'Amber' who provided this recursive algorithm at https://stackoverflow.com/questions/6792803/finding-all-possible-case-permutations-in-python
def all_casings(name):
    if not name:
        yield''
    else:
        first = name[:1]
        if first.lower() == first.upper():
            for sub_casing in all_casings(name[1:]):
                yield first + sub_casing
        else:
            for sub_casing in all_casings(name[1:]):
                yield first.lower() + sub_casing
                yield first.upper() + sub_casing


def botAuthenticate():
    reddit = praw.Reddit('authenticate', user_agent = config.user_agent)
    print ('Authenticated as {}'.format(reddit.user.me()))
    return reddit

def getAllCasings(lookFor, allCasings):
    for string in lookFor:
        allCasings += list(all_casings(string))
    return allCasings


def grabRandomGif():
    size = len(config.routes) - 1
    gif_path = config.routes[randint(0, size)]
    return gif_path

def reply(reddit, subreddit, limit, casings):
    for comment in reddit.subreddit(subreddit).comments(limit=limit):
        for casing in casings:
            if casing in comment.body:
                print ('found ' + casing + ' in comment ' + comment.id + ' ' + comment.body)
                gif_path = grabRandomGif()
                comment.reply('[hi]({})'.format(gif_path))
                print ('responded to a comment!')
    print("Sleeping for 10 seconds....")
    time.sleep(10)

def main():
    reddit = botAuthenticate()
    allCasings = getAllCasings(config.lookFor, [])
    while True:
        reply(reddit, config.subreddit, config.limit, allCasings)

if __name__ == '__main__':
    main()
