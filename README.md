# tdb-pancakes

Auto-responder for Pancake bot written in Python 3.

![](example.gif)

## Dependencies

* html
* bs4
* requests
* discord.py

## Components

tdb-pancakes consists of two separate components, one to keep a local
database of the questions and answers (scrapper), and the other to
interact with Discord

### Scrapper/Indexer

OpenTDB provides an API, although it is only able to get a random set
of questions and answers. This means we can't just simply query the API
for a specific question and retrieve the answer.

To solve this, a scrapper is needed to record the question and answer
for each question. Our scrapper will query the API to retrieve the random
set of questions, and check if it already exists in the database. If it
doesn't, it will create a row with the question and answer.

In addition, the script also gets the question ID. The API also doesn't
provide this, so another workaround is needed. For this, we use a user-facing
webform from OpenTDB's website to provide us with the ID.

Note that the scrapper is considerate with OpenTDB and delays each request.
Currently, the indexer only stores the ID, question, and correct answer. By
default, it only stores the hard questions.

### Bot

The scripts will be marked as tdb_*.py, where the wildcard is replaced with
their respective command. You'll have to get your user token and channel ID through
Discord in order to set it up. Look up online to see how to obtain these two
pieces of information.

Note that the scripts are one-pass only. If you want automated use, you should
use your OS task scheduler (i.e. cron) to set up automated use.

* tdb_trivia automatically answers the trivia questions. You'll need to populate
your database first in order to use it. The script is barebones at the moment
and needs to be improved, but it works if the question is in the DB and the bot
gives out the right reply.

* tdb_daily is very simple, just say p!daily at the selected channel.

## TODO

Core functionality is finished, but the following still needs to be addressed

* Exception handling
* Code clean-up/readability

## Disclaimer

Discord disallows bots that are using user accounts. Your account
might get banned for using this script.

This script is licensed under the MIT license.
