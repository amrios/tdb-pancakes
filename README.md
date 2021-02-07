# tdb-pancakes

Auto-responder for Pancake bot written in Python 3.

## Dependencies

* html
* bs4
* requests
* discord.py

## Components

### Scrapper/Indexer

OpenTDB API only allows uses to obtain a random set of n amount of
questions and the answer for each of those questions. This means we
can't just simply query the API for a specific question.

To solve this, a scrapper is needed to record the question and answer
for each question. Our scrapper will request some amount of questions from
the API, it does a GET at the "Browse" section of the website to retrieve
the question ID (explained below), then checks to see if it is a copy of
a question that already exists in the database. If everything it fines, it
writes a new row.

The indexer is mostly stable. There is some issues needed to be worked out
since the site sometimes returns HTTP 503, which will freeze the indexer.

A script is also provided to sort the question ID in numerical order,
ascending.


I also wanted to record the question ID in the database, but also had the
same issue; the API doesn't give the ID values.
Luckily, we are able to get them by using the "Browse" function of the
website by searching the question. This will eventually populate your
local sqlite database.

The scrapper is considerate with OpenTDB and delays each request.
Currently, the indexer only stores the ID, question, and correct answer.

### Bot

Current scripts for the bot are tdb_trivia and tdb_daily. They are meant to
be run through cron. You'll have to get your user token and channel ID through
Discord. Look up online to get these two piece of information, later versions
might address this.

* tdb_trivia automatically answers the trivia questions. You'll need to populate
your database first in order to use it. The script is barebones at the moment
and needs to be improved, but it works if the question is in the DB and the bot
gives out the right reply.

* tdb_daily is very simple, just say p!daily at the selected channel.

Rapptz Discord.py is used for interacting with Discord. The responder
is able to automatically send work, highlow, trivia, and deposit commands
to the bot. See disclaimer for important notice.

## TODO

Core functionality is finished, but the following still needs to be addressed

* Exception handling
* Code clean-up/readability

## Disclaimer

This script is licensed under the MIT license.

Discord disallows bots that are using user accounts. Your account
might get banned for using this script.

