from selenium import webdriver
import unittest

# this unittest library will give me the details what was actual and expected result

class NewVersionTest(unittest.TestCase):
  def setUp(self):
      self.browser = webdriver.Chrome()
 
  def tearDown(self):
      self.browser.quit()

  def test_the_browser(self):
      # get the chrome execution path
      self.browser.get("http://localhost:8000")
      # assertio if the title is same as page title
      self.assertIn('TO-DO lists', self.browser.title)
      self.fail('Finish the test')
      # to do lists

if __name__ == '__main__':
    unittest.main(warnings='ignore')  
