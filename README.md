Dele Alli Bot
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

His exploits have inspired the following chant, to the tune of Billy Ray Cyrus' "Achy Breaky Heart" from Tottenham Hotspur fans:

"We've got Alli,
 Delle Alli,
 I just don't think you understand,
 He only cost 5 mill
 He's better than Ozil,
 We've got Dele Alli"

 Original:
[![Achy-Breaky-Heart](https://img.youtube.com/vi/byQIPdHMpjc/0.jpg)](https://www.youtube.com/watch?v=byQIPdHMpjc)

 Dele Alli chant:
 [![Dele_Alli_Chant](https://img.youtube.com/vi/qvBqHMK49xQ/0.jpg)](https://www.youtube.com/watch?v=qvBqHMK49xQ)

The Bot:
==========
Making use of PRAW (Python Reddit API Wrapper) and it's comment_stream to continuously pull new comments.
It then scans the comments read in until it is interrupted manually.

Currently the authentication details are stored in a config file, simply change the key/value pairs to the appropriate
account set up for the bot to run on.

Deployment Instructions:
========================
1. Install PRAW (along with Python)

2. In the config file, remove the .dist extension and configure the user/pass for your account

3. Run the bot from the command line via the following command:
  `python DeleAlli.py`


To-Do List:
===========

1. Investigate case-sensitivity, ensure all different edge cases are being monitored, include misspellings? IE: Dele Alli vs. Delle Ali

2. Annoyance Control:
  2a. Limit responses to 1 per page? 1 Per comment tree?
  2b. Point to specific relevant subreddit(s)? /r/coys, /r/soccer, /r/ThreeLions?

3. green_light boolean is a weak cotrol structure, comments are seemingly being evaluated twice potentially as certain batches
are evaluated twice, currently this is being fixed by the sleep feature which is itself problematic as comments can be missed.
[HIGH PRIORITY]

4. Investigate further into PRAW functionality to further populate to-do list

5. Investigate YT video/img embedding in README on GitHub to pretty up the page a bit
