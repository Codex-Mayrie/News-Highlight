import os

class Config:
  """
  General configuration parent class
  """
  NEWS_API_BASE_URL ='https://newsapi.org/v2/sources?&category=general&apiKey=6e618bbf6b0840d69f59b04985d67b2c'
  NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
  NEWS_ARTICLES_API_URL='https://newsapi.org/v2/everything?q={}&apiKey={}'
  SOURCE_ARTICLES_URL='https://newsapi.org/v2/everything?sources={}&apiKey='
  SECRET_KEY = os.environ.get('SECRET_KEY')

class ProdConfig(Config):
  """
  Production configuration child class
  Args:
      Config:The parent configuration class with General configuration settings
  """
  pass
class DevConfig(Config):
  """
  Development configuration child class
  Args:
     Config:The parent configuration class with General configuration settings
  """
  DEBUG =True
  
config_options = {
  'development':DevConfig,
  'production':ProdConfig
}