import pandas as pd
import requests
from bs4 import BeautifulSoup

df = pd.read_csv('dataset.csv')  

# Define a function to scrape author website for contact and book details
def scrape_author_website(author_website):
    try:
        # Send an HTTP GET request to the author's website
        response = requests.get(author_website)
        if response.status_code == 200:
            # Parse the website content
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract contact and book details from the website
            contact_info = soup.find('div', class_='contact-info').text
            book_info = soup.find('div', class_='book-details').text
            
            return contact_info, book_info
    except Exception as e:
        print(f"Error scraping author website: {e}")
    return None, None


for i in range(len(df)):
    author_website = df.at[i, 'Author Website']  # Adjust column name as needed
    contact_info, book_info = scrape_author_website(author_website)
    
  
    df.at[i, 'Contact Info'] = contact_info  # Create a new column for contact info
    df.at[i, 'Book Info'] = book_info  # Create a new column for book info

# Save the updated DataFrame to a new CSV file
df.to_csv('updated_dataset.csv', index=False)
