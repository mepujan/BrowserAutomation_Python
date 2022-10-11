
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


# Initializing Options
options = Options()

options.add_experimental_option("detach",True)

# initializing the driver
driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()),options=options)

# getting url
driver.get("http://pujangautam.com.np")

# maximizing google chrome window
driver.maximize_window()

# finding all the a tag with  href attribute

links = driver.find_elements("xpath","//a[@href]")


# looping over each link to find required button to click on
for link in links:
    # print(link.get_attribute("innerHTML"))
    if "Follow Me On GitHub" in link.get_attribute("innerHTML"):
        link.click()
        break


# switching program pointer to next github tab
driver.switch_to.window(driver.window_handles[1])

# finding span element and getting the followers data
links = driver.find_elements("xpath","//span[@class = 'text-bold color-fg-default']")

print("Number of Followers= ",links[0].get_attribute("innerHTML"))
