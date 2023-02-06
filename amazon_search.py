
from autoscraper import AutoScraper
amazon_url="https://www.amazon.in/s?k=bags"

wanted_list=["₹349","Mi Step Out 12 L Mini Backpack (Small Size, Dark Blue, Water Repellant)"]

scraper=AutoScraper()
result=scraper.build(amazon_url,wanted_list)

print(scraper.get_result_similar(amazon_url,grouped=True))  
