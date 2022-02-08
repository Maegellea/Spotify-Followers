
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import json
from userInformation import spotifyId



driver = webdriver.Chrome()

url = f"https://open.spotify.com/user/{spotifyId}/followers"
driver.get(url)
while True:
    file = open("log.txt","a",encoding="utf-8")
    followerList = []
    arc = driver.find_elements(By.CLASS_NAME,"Nqa6Cw3RkDMV8QnYreTr")
    sleep(1)

    for i in arc:
        arc = i.get_attribute("title")
        followerList.append(arc)  
    
    followerList.insert(0,len(followerList))
    result = json.dumps(followerList)
    file.write(result+"\n")
    driver.refresh()
    sleep(10)
    
