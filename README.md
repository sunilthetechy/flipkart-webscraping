# Flipkart Web Scraping

This Python application uses Flask for the frontend and Pyppeteer for web scraping to extract product information from Flipkart. The user can enter the product name and the number of pages to scrape, and the application will display the scraped data.

## Prerequisites

- Python 3.x
- Flask (`pip install flask`)

## Usage

1. Clone the repository:

    ```bash
    git clone https://https://github.com/sunilthetechy/flipkart-webscraping.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Flask application:

    ```bash
    python app.py
    ```

4. Open your browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to access the web scraping interface.

5. Enter the product name and the number of pages you want to scrape.

6. Click the "Scrape" button to initiate the web scraping process.

7. The scraped data will be displayed, and the CSV file will be saved with the product name and timestamp.

## Folder Structure

- `static`: Contains static assets such as the Flipkart logo (`logo.png`).
- `templates`: Contains HTML templates for the Flask application.
- `app.py`: Flask application for handling web requests and executing the web scraping script.
- `scraping1.py`: Web scraping script using Pyppeteer and BeautifulSoup.

## Author

Sunil The Techy

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/)
- [Pyppeteer](https://github.com/miyakogi/pyppeteer)
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)
- [Flipkart](https://www.flipkart.com/)
```
