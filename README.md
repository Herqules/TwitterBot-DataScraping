# TwitterAnalytics-DataScraping
This repository contains a collection of Python scripts designed for scraping Twitter data, conducting sentiment analysis on tweets, retrieving stock market information, and more. The goal is to provide tools for analyzing the impact of social media on markets, populations, and commodities to better understand trends in public sentiment around various topics on Twitter.

## Projects

### NewsCollater.py

`NewsCollater.py` : script to collate recent tweets from specified news outlets or Twitter users. Utilizes Twitter API to fetch the latest tweets and organizes them by the user.

**Key Features:**
- Fetches variable amount of (default 10) most recent tweets from a list of usernames.
- Error handling for non-200 status codes.
- Outputs tweets to the console.

### SentimentKeywordBot.py

`SentimentKeywordBot.py` : performs sentiment analysis on tweets related to a specific keyword. Employs TextBlob for calculating sentiment polarity and spaCy for named entity recognition.

**Key Features:**
- Searches recent tweets based on a user-input keyword.
- Returns sentiment polarity scores and named entities present in each tweet.
- Returns graphical/statistical data in a readable format to the console.

### StockChecker.py

`StockChecker.py` : a utility script to fetch and display stock market information from the Alpha Vantage API based on a user-input stock symbol.

**Key Features:**
- Retrieves real-time stock information including price, volume, and percent change.
- Can be easily integrated into applications, webpages, and widgets

Dependencies:
- `requests`
- `json`
- `prettytable`
- `spacy`
- `textblob`
- `Python 3`

You will also need to obtain the necessary API keys:
- A bearer token for the Twitter API.
- An API key from Alpha Vantage for stock data.

Replace `"BEARER TOKEN HERE"` and `"API KEY HERE"` with your actual tokens in the scripts.

## Usage

Each script can be run independently. Follow the prompts in the console to input necessary information such as Twitter usernames, search keywords, or stock symbols.
