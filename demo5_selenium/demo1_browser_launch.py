from selenium import webdriver
d=webdriver.Chrome()
d.get("https://www.facebook.com/") # it will lauch & close within fraction of seconds, its beacuse that's how it was scripted in __init__
print(d.title)
