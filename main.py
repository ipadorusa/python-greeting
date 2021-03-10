from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('headless')

# chrome driver
driver = webdriver.Chrome('chromedriver', options=options)
driver.implicitly_wait(3)
driver.get('https://www.greating.co.kr/event/eventCheckAttendance?evEventId=3178#page1')
driver.find_element_by_id('btnCheck').click();
driver.implicitly_wait(3)
driver.find_element_by_id('dvConfirmOk').click();
driver.find_element_by_xpath('//*[@id="contents"]/div/div[1]/ul[1]/li[2]/a').click()
driver.find_element_by_id('id').send_keys('')
driver.find_element_by_id('pw').send_keys('')
driver.find_element_by_id('loginBtn').click()
driver.implicitly_wait(3)
driver.get('https://www.greating.co.kr/event/eventCheckAttendance?evEventId=2978#page1')
driver.find_element_by_id('btnCheck').click()
