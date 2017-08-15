from selenium import webdriver 

browser = webdriver.Chrome()
# opens the chrome 
browser.get("http://localhost:8000")

# compares the page title and header 
#assert 'Django' in browser.title
# excpected fail, since the page title is still Django
assert 'TO-DO' in browser.title

browser.quit()


