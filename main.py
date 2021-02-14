
from selenium import webdriver

try:

    driver = webdriver.Chrome('chromedriver')
    driver.implicitly_wait(3)

    driver.get('https://www.greating.co.kr/login/login?reurl=https%3A%2F%2Fwww.greating.co.kr%2Findex#')
    driver.maximize_window()
    driver.find_element_by_xpath('//*[@id="contents"]/div/div[1]/ul[1]/li[2]/a').click()
    driver.find_element_by_id('id').send_keys('ipadorusa')
    driver.find_element_by_id('pw').send_keys('6_u8!v9g2dq')
    driver.find_element_by_id('loginBtn').click()
    driver.implicitly_wait(3)
    driver.get('https://www.greating.co.kr/event/eventCheckAttendance?evEventId=2978#page1')
    submit = driver.find_element_by_id('btnCheck')
    submit.click()

finally:
    driver.implicitly_wait(5)
    driver.quit()