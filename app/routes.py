from app import app, render_template, request
from app.crawler import Crawl
from app.clean_process import clean, tokenizer
# Create Routes
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        link = request.form["link"]
        scrap = Crawl(link=link)
        links = scrap.fetch_links()
        data = scrap.crawl_data()
        data = clean(set(data.split('%@%')))
        return render_template('output.html', links=links, data=data)
    return render_template('home.html')
