
from selenium import webdriver




import unittest


class ChromeSearch(unittest.TestCase):


        
    
    def test_func(self):

        self.driver = webdriver.Chrome('./chromedriver')
        print("Setup successful")

        

        self.driver.get("http://localhost:5001/seletest?a=5&b=7")
        output=self.driver.find_element_by_tag_name('body').text
        self.assertEqual(output, str(12))

        self.driver.get("http://localhost:5001/seletest?a=5&b=4")
        output=self.driver.find_element_by_tag_name('body').text
        self.assertEqual(output, str(9))

        self.driver.get("http://localhost:5001/seletest?a=10&b=10")
        output=self.driver.find_element_by_tag_name('body').text
        self.assertEqual(output, str(20))




if __name__ == '__main__':
    unittest.main()
