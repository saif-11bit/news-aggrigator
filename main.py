from flask import Flask, render_template
from newsapi import NewsApiClient

app = Flask(__name__)

API_KEY = 'd5f86ab6f4ba4e139f282e1472316682'

@app.route("/")
def homepage():
    newsapi = NewsApiClient(api_key=API_KEY)
    topheadlines = newsapi.get_top_headlines(language='en', country='in')
    articles = topheadlines['articles']
    print(articles)
    desc=[]
    news=[]
    images = []
    urls = []
    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        images.append(myarticles['urlToImage'])
        urls.append(myarticles['url'])
    mylist = zip(news,desc,images,urls)
    return render_template('index.html',context=mylist)