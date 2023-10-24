import pandas as pd
import requests
from bs4 import BeautifulSoup
from lxml import etree


df = pd.read_excel('input.xlsx')

scraped_data = []

for index, row in df.iterrows():
    try:
     
        url = row['URL']
        
       
        if pd.isna(url):
            print(f"Error occurred while scraping {url}: URL is NaN")
            continue
        
      
        response = requests.get(url)
        
       
        if response.status_code != 200:
            print(f"Error occurred while scraping {url}: Request was unsuccessful with status code {response.status_code}")
            continue
        
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
       
        tree = etree.HTML(str(soup))
        
        
    
        
        xpath=  tree.xpath('//div[@class="td-ss-main-content"]//text()')



       
        url_data = {
            'URL_ID': row['URL_ID'],
            'URL': url,
            'Text': xpath
        }
        
       
        scraped_data.append(url_data)
        
     
        print(f"Successfully scraped {url}")
    
    except Exception as e:
        print(f"Error occurred while scraping {url}: {e}")


scraped_df = pd.DataFrame(scraped_data)

# save the scraped data to a new excel file
scraped_df.to_excel('output3.xlsx', index=False)

print("Scraping complete!")
