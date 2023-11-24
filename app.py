from flask import Flask, render_template, request
import subprocess
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    product = request.form.get('product')
    page = request.form.get('page')
    url = f'https://www.flipkart.com/search?q={product.replace(" ", "+")}'

    result = subprocess.run(['python', 'scraping1.py', url, product, page], capture_output=True, text=True)
    print(result)  
    file=product+'_'+datetime.now().strftime("%Y%m%d_%H%M%S")
    return render_template('result.html',file=file)

if __name__ == '__main__':
    app.run(debug=True)
