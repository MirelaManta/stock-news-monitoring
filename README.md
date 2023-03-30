## stock-news-monitoring-project
### Program that tracks stocks prices and sends relevant news to help you choose what to do further.
I find this program extremely useful for stock trading enthusiasts. In its development I used two API endpoints to extract information related to stock prices, as well as news that might be relevant in price fluctuations and impact the traders.  

___How is this working, exactly?___   
Using the API endpoints, the appropriate parameters and the API keys, the closing price of the target stock from the last and penultimate day is extracted, and if there is an absolute difference of more than 5%, an informative message will be sent. There is also a request to fetch the top 3 most significant news about the chosen company. The message contains data about the increase and decrease in price as well as the title and description of an article.  

__Note:__  
!!! API keys for both APIs, Twilio SID, Twilio Auth Token are private and can be accessed after a free registration.
