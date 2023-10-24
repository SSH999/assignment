import requests
from lxml import html


search_url = "https://www.upwork.com/nx/jobs/search/?sort=recency"

# Send an HTTP GET request to the Upwork search page
response = requests.get(search_url)


if response.status_code == 200:
    
    page_content = html.fromstring(response.text)

   
    project_listings = page_content.xpath('//div[@class="job-tile"]')

  
    for listing in project_listings:
       
        project_title = listing.xpath('.//h4[@class="job-title"]/text()')[0].strip()

        
        project_description = listing.xpath('.//div[@class="job-description"]/text()')[0].strip()

       
        project_budget = listing.xpath('.//div[@class="js-budget"]/text()')[0].strip()

      
        client_info = listing.xpath('.//a[@class="client-link"]/text()')[0].strip()

      
        print(f"Title: {project_title}")
        print(f"Description: {project_description}")
        print(f"Budget: {project_budget}")
        print(f"Client: {client_info}")
        print("\n")

else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
