#import necessary packages
import requests
from bs4 import BeautifulSoup
#create a class
class PriceTracker:
        def __init__(self,url):
                self.url = url
                self.user_agent = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
                self.response = requests.get(url=self.url,headers = self.user_agent).text
                self.soup = BeautifulSoup(self.response,"lxml")
        def product_title(self):
                title = self.soup.find("span",{"id":"productTitle"})
                if title is not None:
                        return title.text.strip()
                return "Tag not found"
        def product_price(self):
                price = self.soup.find("span",{"id":"taxInclusiveMessage"})
                if price is not None:
                        return price.text
                return "Tag not found"
samsung = PriceTracker(url = "https://www.amazon.in/Samsung-Storage-Titanium-Compatible-Android/dp/B0C6LN9J1X/ref=sr_1_3?crid=2HQBF82998XGE&keywords=samsung+s23+ultra+5g&qid=1702624821&sprefix=samsun%2Caps%2C268&sr=8-3")
#call the functions
print(samsung.product_title())
print(samsung.product_price())
