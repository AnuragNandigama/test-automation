from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("prefs", {
    "download.deafult_dictionary": r"./",
    "download.prompt_for_dpwnload": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})


# driver = webdriver.Chrome('./chromedriver', options=options)
driver = webdriver.Firefox()
driver.get("https://www.python.org/")

print(driver.title)

sb = driver.find_element_by_name("q")


all_tags = driver.find_element_by_tag_name('a')

tag2 = driver.find_element_by_class_name('readmore')

cookies = driver.get_cookies()

print(all_tags.get_attribute('href'))
print(all_tags.get_attribute('title'))

print(tag2.get_attribute('href'))

# for ck in cookies:
#     print(ck)

