Dele Alli Bot V2.1
==============

This is my first reddit bot based off of https://github.com/Antrikshy/InternetLyingPolice_reddit_bot

Context:
=========
This bot's purpose was inspired by Dele Alli (born Bamidele Jermaine Alli), the
21 year old midfielder who plays for Tottenham Hotspur and England.

In February of 2015, Dele Alli, then 18 year old Dele was transferred from MK Dons of the third tier of English football
to Tottenham Hotspur of the premier league, for a transfer fee of only £5 million.

He immediately earned himself a spot in the first team, and has during his two seasons at Tottenham helped them
to 3rd and 2nd place finishes in the Premier League, winning back to back young player of the year awards, and scored an impressive 28 goals in 70 appearances.

This bot's designed to simply serve a random gif of Dele Alli whenever his name is mentioned in a particular subreddit.

The Bot:
==========
Making use of PRAW (Python Reddit API Wrapper) the bot first authenticates itself based on the info the user provides in praw.ini

Additionally, the config file is used to set up additonal bot details such as the subreddit it should look in, how many comments it should scan at a time, key phrase(s) it is scanning for as well as the routes to the GIFS being supplied.


Deployment Instructions:
========================
1. Install PRAW (along with Python)

2. Properly adjust the config file to reflect your personal running instance, and fill out the praw.ini file with the necessary details

3. Run the bot from the command line via the following command:
  `python DeleAlli.py`


V.2.0 CHANGES:
===================

The bot has been completely redesigned from 1.0 which replied with text and was based  off of https://github.com/Antrikshy/InternetLyingPolice_reddit_bot. It has been upgraded to work with Python 3.0. and has cut down on the
number of imports made.

The bot's actual course of action has been made much simpler too. After authenticating the reddit instance, the bot then
uses a recursive algorithm, and the phrases in the config file to look for, and generates all case-sensitive variations
of the strings provided. Once all the casings are generated, the bot looks through the comments on the relevant sub-reddit and
responds with a random gif from the routes in config.

V.2.1 CHANGES:

- Text that links to the randomized gif changed from "hi" to "Did someone say Dele Alli?" (future consideration to matching the user's specific casing)

- Archiving system added. To prevent the bot from replying to the same comment twice. The bot now populates a list by either: reading from a txt file labelled archive.txt in the project directory, or if that file is yet to exist it will be an empty list. Then, any time a comment is judged to include Dele Alli in any casing, that comment's unique ID is appended to the archive list being used locally within the function, and writing it into an archive.txt file in the project directory for future usage.

- Because the bot now says his name in the reply, to prevent an infinite loop the bot also does a check to ensure it isn't the author of a comment before it replies
