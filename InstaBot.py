from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class InstaBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome()
        self.driver.get("https://instagram.com")
        sleep(2)
        try:
            self.driver.find_element(By.XPATH, "//input[@name='username']").send_keys(username)
            self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(pw)
            self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        except Exception as e:
            print(f"Error during login: {e}")
        sleep(10)
    def get_unfollowers(self):
        self.driver.find_element(By.XPATH, f"//a[contains(@href, '/{username}/')]")\
            .click()
        sleep(5)
        self.driver.find_element(By.XPATH, "//a[contains(@href,'/following')]").click()
        following=self._get_names()
        self.driver.find_element(By.XPATH, "//a[contains(@href,'/followers')]").click()
        followers=self._get_names()
        not_following_back=[user for user in following if user not in followers]
        print("Unfollowers:",not_following_back)
    def _get_names(self):
        sleep(2)  
        scroll_box=self.driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]")
        #Enter your own scroll box Xpath by inspecting the screen.(right click>inspect>copy xpath)
        last_ht,ht=0,1
        while last_ht !=ht:
            last_ht=ht
            sleep(2)
            ht=self.driver.execute_script("""
            arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight;
            """, scroll_box)
        links=scroll_box.find_elements(By.TAG_NAME, "a")
        names=[name.text for name in links if name !='']
        #close button, Enter your own close button Xpath by inspecting the screen.(Right click>inspect>copy xpath)
        self.driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/button")\
            .click()
        return names
if __name__ == "__main__":
    username = input("Enter your Instagram username: ")
    password = input("Enter your Instagram password: ")
    my_bot = InstaBot(username, password)
    my_bot.get_unfollowers()
   