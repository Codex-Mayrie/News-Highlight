import unittest
from app.models import Articles

class ArticlesTest(unittest.TestCase):
    def setUp(self):
        self.new_article = Articles("Skip the holiday rush this year — for the planet’s sake","Spend some time making a sumptuous, low-carbon chili instead.","http://grist.org/article/skip-the-holiday-rush-this-year-for-the-planets-sake/","Chip Giller","https://grist.files.wordpress.com/2019/11/balloon-package.jpg?w=1200&h=675&crop=1","2019-11-16T12:02:05Z")

    def instance_test(self):
        self.assertTrue(isinstance(self.new_article,Articles))

if __name__ == "__main__":
    unittest.main()