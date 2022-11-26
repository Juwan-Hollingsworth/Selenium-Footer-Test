from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

  
# Main Function
if __name__ == '__main__':
  
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument('--log-level=3')
  
    # Provide the path of chromedriver present on your system.
    driver = webdriver.Chrome(executable_path="chromedriver",
                              chrome_options=options)
    driver.set_window_size(1440, 877)
  
    # Launch Google home page automatically
    driver.get("https://www.google.com/")
    time.sleep(5)

    # Check and verify all the footer links

    driver.find_element(By.LINK_TEXT,"Advertising").click()
    time.sleep(5)

    expected_title = "Google Ads - Get More Customers & Generate Leads with Online Ads"
    actual_title = driver.title

    # print("Window Title:" + actual_title)

    if actual_title == expected_title:
        print("Window Title Matched:" + actual_title)
        print("Page Loaded - Test 1 Successful!")
    else:
        print("Test Failed")

    # Open google homepage again
    driver.get("https://www.google.com/")
    time.sleep(5)

    driver.find_element(By.LINK_TEXT,"Business").click()
    time.sleep(5)

    expected_title = "Google for Small Business - Resources to get your small business online"
    actual_title = driver.title

    # print("Window Title:" + actual_title)

    if actual_title == expected_title:
        print("Window Title Matched:" + actual_title)
        print("Page Loaded - Test 2 Successful!")
    else:
        print("Test Failed")

     # Open google homepage again
    driver.get("https://www.google.com/")
    time.sleep(5)

    driver.find_element(By.LINK_TEXT,"Privacy").click()
    time.sleep(5)

    expected_title = "Privacy Policy – Privacy & Terms – Google"
    actual_title = driver.title

    # print("Window Title:" + actual_title)

    if actual_title == expected_title:
        print("Window Title Matched:" + actual_title)
        print("Page Loaded - Test 3 Successful!")
    else:
        print("Test Failed")


         # Open google homepage again
    driver.get("https://www.google.com/")
    time.sleep(5)

    driver.find_element(By.LINK_TEXT,"Terms").click()
    time.sleep(5)

    expected_title = "Google Terms of Service – Privacy & Terms – Google"
    actual_title = driver.title

    # print("Window Title:" + actual_title)

    if actual_title == expected_title:
        print("Window Title Matched:" + actual_title)
        print("Page Loaded - Test 4 Successful!")
    else:
        print("Test Failed")


        # Open google homepage again
    driver.get("https://www.google.com/")
    time.sleep(5)

    # select "Settings" menu
    driver.find_element(By.CSS_SELECTOR,".ayzqOc").click()
    time.sleep(5)

    driver.find_element(By.LINK_TEXT,"Search settings").click()
    time.sleep(5)

    expected_title = "Search Settings"
    actual_title = driver.title

    # print("Window Title:" + actual_title)

    if actual_title == expected_title:
        print("Window Title Matched:" + actual_title)
        print("Page Loaded - Test 5 Successful!")
    else:
        print("Test Failed")


        # Open google homepage again
    driver.get("https://www.google.com/")
    time.sleep(5)

    # select "Settings" menu
    driver.find_element(By.CSS_SELECTOR,".ayzqOc").click()
    time.sleep(5)

    driver.find_element(By.LINK_TEXT,"Advanced search").click()
    time.sleep(5)

    expected_title = "Google Advanced Search"
    actual_title = driver.title

    # print("Window Title:" + actual_title)

    if actual_title == expected_title:
        print("Window Title Matched:" + actual_title)
        print("Page Loaded - Test 6 Successful!")
    else:
        print("Test Failed")


       # Open google homepage again
    driver.get("https://www.google.com/")
    time.sleep(5)

    # select "Settings" menu
    driver.find_element(By.CSS_SELECTOR,".ayzqOc").click()
    time.sleep(5)

    driver.find_element(By.LINK_TEXT,"Your data in Search").click()
    time.sleep(5)

    expected_title = "Your data in Search"
    actual_title = driver.title

    # print("Window Title:" + actual_title)

    if actual_title == expected_title:
        print("Window Title Matched:" + actual_title)
        print("Page Loaded - Test 7 Successful!")
    else:
        print("Test Failed")


             # Open google homepage again
    driver.get("https://www.google.com/")
    time.sleep(5)

    # select "Settings" menu
    driver.find_element(By.CSS_SELECTOR,".ayzqOc").click()
    time.sleep(5)

    driver.find_element(By.CSS_SELECTOR,".tFYjZe > div:nth-child(1)").click()
    time.sleep(5)

    expected_title = "Google - My Activity"
    actual_title = driver.title

    # print("Window Title:" + actual_title)

    if actual_title == expected_title:
        print("Window Title Matched:" + actual_title)
        print("Page Loaded - Test 8 Successful!")
    else:
        print("Test Failed")



                # Open google homepage again
    driver.get("https://www.google.com/")
    time.sleep(5)

    # select "Settings" menu
    driver.find_element(By.CSS_SELECTOR,".ayzqOc").click()
    time.sleep(5)

    driver.find_element(By.LINK_TEXT,"Search help").click()
    time.sleep(5)

    expected_title = "Google Search Help"
    actual_title = driver.title

    # print("Window Title:" + actual_title)

    if actual_title == expected_title:
        print("Window Title Matched:" + actual_title)
        print("Page Loaded - Test 9 Successful!")
    else:
        print("Test Failed")


   
    # a = "Settings"
    # e = "Google for Small Business - Resources to get your small business online"

    # def checkTitle(z: str, y:str):
    #     driver.get("https://www.google.com/")
    #     time.sleep(5)
    #     driver.find_element(By.LINK_TEXT,[z]).click()
    #     time.sleep(5)
    #     actual_title = driver.title
    #     if actual_title == y:
    #         response = "true"
    #         # print("Window Title Matched:" + actual_title)
    #         # print("Page Loaded - Test 5 Successful!")
    #         return (response)
            
    #     else:
    #         response = "false"
    #         # print("Test Failed")
    #         return (response)

    # checkTitle(a,e)

    


    # Google Ads - Get More Customers & Generate Leads with Online Ads
    # Google for Small Business - Resources to get your small business online
    # Privacy Policy – Privacy & Terms – Google
    # Google Terms of Service – Privacy & Terms – Google


    # Check to see if   
    # String expectedWindowTitle = "Downloads"
    # String actualWindowTitle = driver.getTitle();
    # System.out.println("Window Title: " + actualWindowTitle);

    # if (actualWindowTitle.equals(expectedWindowTitle)) {
	# 			System.out.println("Window Title matched: " + actualWindowTitle);
	# 			System.out.println("Page Loaded - Test Successful!");
	# 		}
	# 		else {
	# 			String temp = "Window Title is: " + actualWindowTitle;
	# 			temp = temp + ", expected: " + expectedWindowTitle;
	# 			System.out.println(temp);
	# 			System.out.println("Test Failed!");
	# 		};

    # Settings link is clicked
    # driver.findElement(By.linkText("Advertising")).click()

    



    #Test each of the Settings options



    # driver.find_element(By.CSS_SELECTOR, ".close_button-76031-button close_button-76031-button-d2 bluecoreCloseButton").click()
    # time.sleep(60)
    # driver.quit()
    print("Done")