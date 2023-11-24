import csv
import asyncio
from pyppeteer import launch
from bs4 import BeautifulSoup as bs
import re
from datetime import datetime
import sys

def extract_numeric(string):
    numeric_values = re.findall(r'\d+', string.replace(",", ""))
    return int(numeric_values[0]) if numeric_values else None

async def scrape_page(url, product, page_number):
    browser = await launch(headless=False,timeout=10000000)
    page = await browser.newPage()
    page_url = f'{url}&page={page_number}' 
    await page.goto(page_url, timeout=100000)
    content = await page.content()
    html = bs(content, 'html.parser')

    products_list = html.find_all('div', {"class": '_1AtVbE col-12-12'})

    names = []
    prices = []
    ratings = []
    n_reviews = []
    n_ratings = []
    desc = []
    img_urls = []

    for i in products_list:
        try:
            names.append(i.find_all('div', {"class": '_4rR01T'})[0].text)
            prices.append(i.find_all('div', {"class": "_30jeq3 _1_WHN1"})[0].text)
            ratings.append(i.find_all('div', {"class": '_3LWZlK'})[0].text)
            n_reviews.append(extract_numeric(i.find_all('div', {"class": '_3pLy-c row'})[0].find_all('div', class_='gUuXy-')[0].find_all('span')[5].text))
            n_ratings.append(extract_numeric(i.div.div.a.find_all('div', {"class": '_3pLy-c row'})[0].find_all('div', class_='gUuXy-')[0].find_all('span')[3].text))
            des = i.find_all('li', {"class": 'rgWa7D'})
            img_urls.append(i.find_all('img', class_="_396cs4")[0].get('src'))
            d = [j.text for j in des]
            desc.append(d)
        except IndexError:
            ratings.append('Sponsored')

    await browser.close()

    return names, prices, ratings, n_reviews, n_ratings, desc, img_urls

async def main():
    if len(sys.argv) != 4:
        sys.exit(1)

    url = sys.argv[1]
    product = sys.argv[2]
    num_pages = int(sys.argv[3])

    with open(f'{product}_info_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv', 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Name', 'Price', 'Rating', 'Number of Reviews', 'Number of Ratings', 'Description', 'Image URL'])

        for page_number in range(1, num_pages + 1):
            names, prices, ratings, n_reviews, n_ratings, desc, img_urls = await scrape_page(url, product, page_number)

            for name, price, rating, num_reviews, num_ratings, description, imgurl in zip(names, prices, ratings, n_reviews, n_ratings, desc, img_urls):
                csv_writer.writerow([name, price, rating, num_reviews, num_ratings, '\n'.join(description), imgurl])
                

if __name__ == '__main__':
    asyncio.run(main())
    print("Data scraped and saved to CSV files")
