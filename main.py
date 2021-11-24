from selenium import webdriver
import time



chrome_driver_pass = "/Users/polis/PycharmProjects/Chrome Driver/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_pass)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_id("cookie")

time_5 = time.time() + 5
time_end = time.time() + 300

while True:
    cookie.click()

    if time.time() > time_5:
        #current money
        money = int(driver.find_element_by_id("money").text.replace(",", ""))

        #find all elements in shop
        shop = driver.find_elements_by_css_selector("#store b")[:-1]
        #slices the string to omit the last character
        all_items = [{"id": "buy"+i.text.split("-")[0].strip(), "price": int(i.text.split("-")[1].strip().replace(",", ""))} for i in shop]
        #find the most expensive item that we can buy and buy it
        for item in all_items[::-1]:
            if item["price"] <= money:
                element = driver.find_element_by_id(item["id"]).click()
                break
        #add another 5 seconds until the next check
        time_5 = time.time() + 5

    if time.time() > time_end:
        print(driver.find_element_by_id('cps').text)
        break
