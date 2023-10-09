#!/usr/bin/env python
# coding: utf-8

# In[15]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import 
from datetime import datetime, timedelta

 

# Define the start and end dates
start_date = datetime(2019, 1, 1)
end_date = datetime(2023, 12, 31)

 

# Initialize an empty list to store the extracted data
data_list = []

 

# Define the base URL
base_url = "https://admn5015-340805.uc.r.appspot.com/"

 

# Define the step size for incrementing the date (1 day in this case)
step_size = timedelta(days=1)

 

# Loop through the range of dates
current_date = start_date
while current_date <= end_date:
    # Generate the URL for the current date
    formatted_date = current_date.strftime("%Y-%m-%d")
    url = base_url + formatted_date + ".html"

    response = requests.get(url, timeout=15)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")

    # Extract data for the current date
    price = soup.find("td", {"id": "price"}).text
    likes = soup.find("td", {"id": "likes"}).text
    dislikes = soup.find("td", {"id": "dislikes"}).text
    followers = soup.find("td", {"id": "followers"}).text

    # Create a dictionary with the data
    data = {
        "Date": formatted_date,
        "Price": price,
        "Likes": likes,
        "Dislikes": dislikes,
        "Followers": followers
    }

    # Append the data to the list
    data_list.append(data)

    # Increment the current date by the specified step size (1 day)
    current_date += step_size

 

# Create a DataFrame from the list of data
df = pd.DataFrame(data_list)

 






# In[17]:


print(df)


# In[22]:


# Write the DataFrame to an Excel file

 

csv_file =r"C:\Users\aravi\OneDrive\Desktop\Outputdata.csv"

df.to_csv(csv_file, index=False)



print(f"Data has been written to {csv_file}")


# In[ ]:




