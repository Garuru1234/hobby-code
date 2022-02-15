from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
# import pyautogui  # Chrome拡張のアクションボタンクリック用
import chromedriver_binary
import time
import random
n = 1


def login():

    while True:
        try:
            driver.get(
                'https://www.instagram.com/accounts/login/?source=auth_switcher')
            print("accessed instagram\n")
            time.sleep(1)

            # メアドと、パスワードを入力
            driver.find_element_by_name(
                'username').send_keys('')
            time.sleep(1)
            driver.find_element_by_name('password').send_keys('')
            time.sleep(random.randint(1, 2))

        # ログインボタンを押す
            driver.find_element_by_class_name('L3NKy       ').click()
            time.sleep(random.randint(4, 5))
            print("logged in instagram\n")
            time.sleep(1)
            return

        except WebDriverException:
            driver.close
            time.sleep(5)
            exit


def tagsearch(tag):
    instaurl = 'https://www.instagram.com/explore/tags/'
    driver.get(instaurl + tag)
    time.sleep(random.randint(5, 10))
    print("searched tag\n")
    time.sleep(1)


def clicknice():
    target = driver.find_elements_by_class_name('_9AhH0')[10]
    actions = ActionChains(driver)
    actions.move_to_element(target)
    actions.perform()
    print("viewing latest pictures\n")
    time.sleep(1)

    driver.find_elements_by_class_name('_9AhH0')[9].click()
    time.sleep(random.randint(2, 4))
    print("clicked a picture\n")
    time.sleep(1)

    try:
        for i in range(random.randint(100, 150)):
            driver.find_element_by_class_name('fr66n').click()
            print("pushed like\n")
            n = +1
            time.sleep(random.randint(
                random.randint(2, 4), random.randint(5, 7)))

            driver.execute_script('arguments[0].click();', driver.find_element_by_xpath(
                "/html/body/div[7]/div[2]/div/div[2]/button"))  # driver.find_element_by_class_name("wpO6b  ").click()
            print("moved to new picture\n")
            time.sleep(random.randint(
                random.randint(2, 5), random.randint(10, 15)))

            if random.randint(1, 7) < 3:
                driver.execute_script('arguments[0].click();', driver.find_element_by_xpath(
                    "/html/body/div[7]/div[2]/div/div[2]/button"))  # driver.find_element_by_class_name("wpO6b  ").click()
                print("moved to new picture\n")
                time.sleep(random.randint(
                    random.randint(2, 5), random.randint(10, 15)))

    except WebDriverException:
        driver.refresh()
        time.sleep(random.randint(5, 8))
        print("errow was detected\n")


if __name__ == '__main__':

    taglist = ['料理好き', "ごはん好きな人とつながりたい", "料理好きな人と繋がりたい", "f4f", "男子ごはん"]

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_extension(
        "")

    driver = webdriver.Chrome(options=chrome_options)

    login()

    while True:
        tagsearch(random.choice(taglist))
        if driver.find_elements_by_class_name('_9AhH0'):
            break
        else:
            exit

    clicknice()
    driver.close()
    print(n)
    print("program has successfully done")
