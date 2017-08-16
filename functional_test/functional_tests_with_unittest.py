from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

# this unittest library will give me the details what was actual and expected result

class NewVersionTest(unittest.TestCase):
  def setUp(self):
      self.browser = webdriver.Chrome()
 
  def tearDown(self):
      self.browser.quit()

  def test_the_browser(self):
      # get the chrome execution path
      self.browser.get("http://localhost:8000")
      # assertIn if the title is same as page title
      #self.assertIn('TO-DO lists', self.browser.title)
      
      # get the text of <h1>
      header_text = self.browser.find_element_by_tag_name('h1').text
      # assertIn if the header_text is same as 'TO-DO lists'
      self.assertIn('TO-DO lists', header_text)

      # test the input_box 
      input_box = self.browser.find_element_by_id('input_text_item')
      self.assertEqual(input_box.get_attribute('placeholder'), 'Enter a to-do item')
      input_box.send_keys('Buy my Tesla X model')
      
      input_box.send_keys(keys.ENTER)
      time.sleep(1)
      
      table = self.browser.find_element_by_id('id_list_table')
      rows = table.find_elements_by_tag_name('tr')
      self.assertTrue(any(row.text == '1.Buy my Tesla X model' for row in rows))
      
      self.fail('Finish the test')
      # to do lists

if __name__ == '__main__':
    unittest.main(warnings='ignore')  
