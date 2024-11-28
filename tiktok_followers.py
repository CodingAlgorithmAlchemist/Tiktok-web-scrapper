from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def get_tiktok_followers(username):
    try:
        url = f"https://www.tiktok.com/@{username}"
        driver = webdriver.Chrome() 
        driver.get(url)
        time.sleep(5)  

        
        followers = driver.find_element(By.CSS_SELECTOR, '[data-e2e="followers-count"]').text
        following = driver.find_element(By.CSS_SELECTOR, '[data-e2e="following-count"]').text

        driver.quit()
        return {"followers": followers, "following": following}
    except Exception as e:
        return f"Error occurred: {e}"

username = "simplyspeakin"
result = get_tiktok_followers(username)
print(result)