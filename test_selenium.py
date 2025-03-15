from selenium import webdriver
import time

# Chrome 브라우저 실행
driver = webdriver.Chrome()

# google connect
driver.get("https://www.google.com")

# 5초 동안 대기
time.sleep(5)

# 브라우저 종료
driver.quit()
