class Articles:
  """
  Class articles that show the objects in the article
  """
  def __init__(self, source, description, title, url, author, urlToImage):
    self.source = source
    self.description = description
    self.title = title
    self.url = url
    self.author = author
    self. urlToImage = urlToImage
    
class Sources:
  """
  A class sources that shows sources that are supposed to be displayed in the object
  """
  def __init__(self, name, id, url, category, language, country, description):
    self.name = name
    self.id = id
    self.url = url
    self.category = category
    self. language = language
    self.country = country
    self.description = description