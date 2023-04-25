import requests
import spacy
from textblob import TextBlob


# Set bearer token
bearer_token = "BEARER TOKEN HERE"

# Load English language model for spaCy
nlp = spacy.load("en_core_web_sm")

# Prompt user to enter a keyword for the Twitter search
keyword = input("Enter a keyword to search Twitter: ")

# Set search parameters
search_url = "https://api.twitter.com/2/tweets/search/recent"
query_params = {'query': keyword,
                'max_results': '50',
                'tweet.fields': 'text,public_metrics'}

# Send GET request to Twitter API with bearer token and search parameters
response = requests.get(search_url, headers={'Authorization': f'Bearer {bearer_token}'},
                        params=query_params)

# Extract tweet data from JSON response
tweet_data = response.json().get('data', [])

# Iterate through each tweet and perform sentiment analysis using TextBlob and named entity recognition using spaCy
for tweet in tweet_data:
    analysis = TextBlob(tweet['text'])

    # Perform named entity recognition using spaCy
    doc = nlp(tweet['text'])
    entities = [ent.text for ent in doc.ents]

    # Print the tweet, its sentiment score, and its named entities
    print(tweet['text'] + '\n')
    print("TextBlob sentiment polarity: ", analysis.sentiment.polarity, '\n')
    print("Named entities: ", entities, '\n')

