import requests
from twilio.rest import Client

STOCK_NAME = "AMZN"
COMPANY_NAME = "Amazon Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "YOUR STOCK API KEY HERE"
NEWS_API_KEY = "YOUR NEWS API KEY"

TWILIO_SID = "YOUR TWILIO SID"
TWILIO_AUTH_TOKEN = "YOUR TWILIO AUTH TOKEN"

# Get yesterday's closing stock price.
stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}
response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_lst = [value for (key, value) in data.items()]
print(data_lst)
yesterday_data = data_lst[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

# Get the day before yesterday's closing stock price
day_before_yesterday_data = data_lst[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

# Find the POSITIVE (with abs() function) difference between 1 and 2.
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percentage = round((difference/float(yesterday_closing_price)) * 100)
print(diff_percentage)

# Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

if abs(diff_percentage) > 1:   # I chose this value for testing purposes only (should be 5-10%)
    news_params = {
        "apiKey": NEWS_API_KEY,
        "q": COMPANY_NAME,
        "searchIn": "title",
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

# Get a hold of the first three articles
three_articles = articles[:3]
# print(three_articles)

# Create a new list of the first 3 articles' headline and description using list comprehension.
formatted_articles = [f"{STOCK_NAME}:{up_down}{diff_percentage}% \nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
# Send each article as a separate message via Twilio.
client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
for article in formatted_articles:
    message = client.messages.create(
        body=article,
        from_="YOUR TWILIO NUMBER",
        to="YOUR VERIFIED NUMBER HERE"
    )
