from flask import render_template, redirect,request, url_for
from ..requests import get_sources, search_articles, get_articles, articles_source
from .import main



@main.route('/')
def index():

  """
 A view root page function that returns the index page and its data
  """
  
  general_news = get_sources('general')
  sports_news = get_sources('sports')
  health_news = get_sources('health')
  business_news = get_sources('business')
  return render_template('index.html',general=general_news,sports=sports_news,health=health_news,business=business_news )

  

@main.route('/sourceArticles/<id>')
def sourceArticles(id):
  
  """
 A view sourceArticles page function that returns the sourceArticles details and its data
  """
  all_articles = articles_source(id)
  source = id
  return render_template('articlessource.html', articles= all_articles, source =source)
  
  
@main.route('/news-Articles')
def newsArticles():
    """
   A view function that returns the news articles details and its data
     
    """
    science_articles = get_articles('science')
    entertainment_articles = get_articles('entertainment')
    health_articles = get_articles('health')
    return render_template('articles.html',science=science_articles, entertainment=entertainment_articles,health=health_articles)
  
@main.route('/article_Search/<article_name>')
def articleSearch(article_name):
  """
  A view function that searches for the articles by name and returns the searched article
  """
  
  search_article_name = article_name.split(" ")
  search_name_format = "+".join(search_article_name)
  searched_articles = search_articles(search_name_format)
  
  return render_template('search.html',articles = searched_articles)