from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

#https://chromedriver.chromium.org/downloads 
browser = webdriver.Chrome(ChromeDriverManager().install)

browser.get('https//www.facebook.com')

#email
browser.find_element_by_id('email').send_keys('')
#senha
browser.find_element_by_id('pass').send_keys('')
#clica em entrar
browser.find_element_by_name('login').click()
