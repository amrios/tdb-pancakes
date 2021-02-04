# tdb-pancakes

I'll upload the entire project later.

Auto-responder for Pancake bot written in Python 3.
Uses OpenTDB for trivia question/answer source.

## Dependencies

html
bs4
requests
discord.py

## Components

### Scrapper and Indexer

Sadly, OpenTDB doesn't provide their ID values in their public API, but we are able to get them by using the user-oriented portion of the website by searching the question. This will eventually populate your local sqlite database that we can use locally to look up questions. The scrapper is considerate with OpenTDB and delays each request. Currently, the indexer only stores the ID, question, and correct answer, but our wrapper is much more feature complete and can be used for other projects related to OpenTDB.

### Bot

Rapptz Discord.py is used for interacting with Discord. The responder is able to automatically send work, highlow, trivia, and deposit commands to the bot. See disclaimer for important notice.

## Disclaimer

This script is licensed under the MIT license.

Discord disallows unofficial clients for user accounts. Your account might get banned for using this script.

## Thanks

* Simon and Joshie for actually making me start a short side-project.
