import unittest
from app.models import Sources

class SourceTest(unittest.TestCase):
  """
  Test Class to test the behavior of the Source class
  """
  
  def setUp(self):
    """
    Set up method that will run before every Test
    """
    self.new_source = Sources("Fox News","fox-news","https://www.foxnews.com/media/vaping-illness-cdc-apple-vitamin-e","health","en","us", "\"I've actually had patients, very young kids, teenagers, they come in and when I listen to their lungs, it sounds like you're taking a piece of paper and crunching it together,\" said Dr. Janette Nesheiwat on the latest edition of Fox Nation's \"Nuff Said with")
  
  def test_instance(self):
    self.assertTrue(isinstance(self.new_source, Sources))
    