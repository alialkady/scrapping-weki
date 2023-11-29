import requests
import pandas as pd
from bs4 import BeautifulSoup

#lists
titles = []
rows = []
rows_text = []

# fetch
url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

# get content
page = requests.get(url)

# soup
soup = BeautifulSoup(page.text, "html.parser")

# get the table
table = soup.find_all("table")[1]

# get the titles
title = table.find_all("th")
for tit in title:
    titles.append(tit.text.strip())
#pandas process
df =pd.DataFrame(columns= titles)

# get the rows
column_data = table.find_all("tr")
i=0
for i, row in enumerate(column_data[1:]):
    cells = row.find_all("td")
    row_text = [cell.text.strip() for cell in cells]
    df.loc[i] = row_text
#print dataframe
print(df)

#create csv file from pandas
df.to_csv(r'D:\datascience\web scraping\linkedin scraper using selenium\data.csv',index=False)


