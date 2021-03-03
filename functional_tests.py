from selenium import webdriver

browser = webdriver.Firefox()

# Bob has heard about this awesome new to-do app.
browser.get('http://localhost:8000')

# He notices 'to-do' in the title.
assert 'To-Do' in browser.title

browser.quit()
