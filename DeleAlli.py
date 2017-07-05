import praw
import sys
import time
import threading
import urllib.request
import urllib.error
import configparser #to read config file

#reading the config file

config = configparser.ConfigParser()
config.read('Dele_Alli_Bot.ini')

green_light = True  #boolean to prevent dulpicate comments
# reading from config file

USERNAME = config.get('Authentication', 'Username')
PASSWORD = config.get('Authentication', 'Password')

USER_AGENT = "Dele_Alli_Bot"
MESSAGE = "We've got Alli! Dele Alli! \n I JUST! DON'T! THINK! YOU UNDERSTAAAAAND! \n HE ONLY COST 5 MILL! \n HE'S BETTER THAN ÖZIL! \n WE'VE GOT DELE ALLIIIIII!"

def main():
    #r is going to be the reddit object from here on out
    r = praw.Reddit(USER_AGENT)
    r.login(USERNAME, PASSWORD)

    print >> sys.stderr, "Logged in."

    #Scans and deletes old comments with <1 point every half hour
    thread = threading.Thread(target=delete_downvoted_posts, args=(r,))
    thread.start()

    # do i need these to be logged in an case-sensitive way?
    what_to_look_for = ("Dele Alli", "dele alli", "DELE ALLI", "dele allI", "dele alLi",
    "dele aLli", "dele Alli", "delE alli", "deLe alli", "dEle alli", "Dele alli",
    "dele alLI")

    #neverending loop to run bot continuously

    while (True):
        print >> sys.stderr, "Initializing scanner..."
        comment_scanner(r, what_to_look_for)
        #sleep for 15 seconds, currently to fix repeat comments for now
        print >> sys.stderr, "Taking a 15 second donut break..."
        time.sleep(15)
        print >> sys.stderr, "I'm full"

'''
The following function uses a series of for-loops to read comments from the comment-stream
and scan for phrases. For each fetched comment in a batch, the bot scans for a phrase it is watching for
and if it finds one, it posts the song. Also seeks to scan usernams of everyone that has replied to each comment,
and turns off the green_lightif the bot has commented.'''

# Parameters: session: the reddit session to use (r), phrases

def comment_scanner(session, phrases):
    print >> sys.stderr, "Fetching comments..."

    # comments now stores all the comments pulled using the comment stream
    # Change "all" to "subreddit-name" to scan a particular subreddit
    # limit = None fetches max possible comments (1000)
    # See PRAW documentation for verbosity explanation
    comments = praw.helpers.comment_stream(session, "all", limit = None, verbosity = 0)
    comment_count = 0 #number of comments scanned

    #read each comment
    for scanning in comments:
        print >> sys.stderr, "Scanning comments..."
        comment_count += 1
        green_light = True
        for phrase in phrases:
            print >> sys.stderr, "Searching for phrases..."
            #if a phrase is found
            if phrase in scanning.body:
                #check replies to see if alredy replied
                for reply in scanning.replies:
                    if reply.author.name == "Dele_Alli_Bot":
                        print >> sys.stderr, "Already replied."
                        green_light = False
                        break

                    #if not already replied
                    if (green_light == True):
                        print >> sys.stderr, "Something found!"
                        post_the_song(scanning)
                        print >> sys.stderr, "Posted the song"
                        break

        #main () fetches more comments if this batch is done
        #comment_stream seems to grab more than 1000 comments at a time
        # currently hard coding a limit, let's re-work this

        if comment_count == 1000:
            return;

''' Method that simply replies to the comment passed in as a Parameter
Parameters: reply_to : the comment to relpy to'''

def post_the_song(reply_to):
    # Post comment

    try:
        print >> sys.stderr, "Posting the song..."
        reply_to.reply(MESSAGE)

    #If Reddit returns an error ((when the bot tries to post in an unauthorized sub))
    except urllib2.HTTPError as e:
        print >> sys.stderr, "Got HTTPError from reddit:" + e.code
        if e.code == 403:
            print >> sys.stderr, "Posting in a restricted sub-reddit"
        print << sys.stderr, "Nothing to see here."

    except Exception as e:
        print >> sys.stderr, "Got some non-HTTPError exception"

# Method to delete old comments that have been downvoted
# Scans 25 comments every half hour, parameters: session

def delete_downvoted_posts(session):
    while (True):
        print >> sys.stderr, "\n" + "Starting to scan old comments"
        my_account = session.get_redditor(USERNAME)
        my_comments = my_account.get_comments(limit = 10)

        for old_comment in my_comments:
            if old_comment.score <= 0:
                print >> sys.stderr, "Unpopular comment, deleting"
                old_comment.delete()

        print >> sys.stderr, "Turning off old comment scanner for 30 mins..."
        time.sleep(1800)

if __name__ == '__main__':
    main()
