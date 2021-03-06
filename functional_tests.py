from selenium import webdriver
import unittest

class TestToDo(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Bob has heard about this awesome new to-do app.
        self.browser.get('http://localhost:8000')

        # He notices 'to-do' in the title.

        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main()