from app import app, render_template, request
from app.crawler import Crawl, singleCrawl
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

@app.route('/single-crawl',methods = ['GET','POST'])
def single_crawler():
    if request.method == "POST":
        link = request.form["link"]
        scrap = singleCrawl(link=link)
        return render_template('single-output.html',data = data)

    return render_template('home.html')
