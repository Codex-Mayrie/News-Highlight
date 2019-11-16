from .models import Sources, Articles
from urllib.request,json
import request
import os

# Getting the api key
api_key = None

# Getting the Source url
s_url = None

# Getting the Articles url
art_url = None

def configure_request(app):
  global api_key, s_url, art_url
  api_key = app.config['API_KEY']
  s_url = app.config['NEWS_API_BASE_URL']
  art_url = app.config['NEWS_ARTICLES_API_URL']
  articles_url = app.config['SOURCE_ARTICLES_URL']
  
def get_sources(category):
  """
  Function that gets the response from json to the url request
  """
  get_sources_url = s_url.format(category, api_key)
  
   with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None
        
        if get_sources_response['results']:
          sources_results_items = get_sources_response['results']
          sources_results = process_results(sources_results_items)
          
          return sources_results
        
def process_new_sources(sources_list):
      """
      Function that processes the sources result and transform them to a list of Objects
      Args:
      source_list:A list of dictionaries that contain source details
      Returns:
          sources_results: A list of sources objects
      """
      sources_results = []
          
      for one_source_item in sources_list:
                name = one_source_item.get('name')
                id = one_source_item.get('id')
                url = one_source_item.get('url')
                category = one_source_item.get('category')
                language = one_source_item.get('language')
                country = one_source_item.get('country')
                description = one_source_item.get('description')
                
                new_source = Sources(name,id,url,category,language,country, description)
        sources_results.append(new_source)
      return sources_results