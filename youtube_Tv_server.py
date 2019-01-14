import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def check_url(browser, url, max_attemps, xpath):# solo devuelve valores de verdad, pero igual se puede ejecutar sin guardar el valor
        #esta funcion revisa la pagina, si funciona devuelve un valor de verdad, pero no es necesario guardarlo siempre
        attemps = 0
        timeout = 5
        print 'Esperando pagina'
        fail = 'ok'
        while attemps < max_attemps:
            try:
                browser.get(url)
                element_present = EC.presence_of_element_located((By.XPATH, xpath))
                WebDriverWait(browser, timeout).until(element_present)
                return True
                break
            except TimeoutException:
                attemps +=1
                print "Timed out waiting for page to load"
                fail = 'Fail'
        if attemps == max_attemps:
            return False
                #return "Fail"

headless = raw_input('Desea ver el driver?(y/n)')
path_driver = '/usr/lib/chromium-browser/chromedriver'
if headless == 'y':
    driver = webdriver.Chrome(path_driver)
    # la siguiente linea funciona con la raspberry pi
    #driver = webdriver.Chrome(path_driver)
else:
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    #driver = webdriver.Chrome(path_driver, chrome_options=chrome_options)

link = 'https://www.youtube.com/tv#'
#driver.get(link)
# este le da click en skip
xpath = '//*[@id="overlay-stage"]/div[2]/div[2]/div[2]/div[2]'
check_url(driver, link, 3, xpath)
time.sleep(1)# estos sleep dejan pasar un momento para que la pagina se "estabilice" y no salgan errores
driver.find_element_by_xpath('//*[@id="overlay-stage"]/div[2]/div[2]/div[2]/div[2]/div[1]').click()
time.sleep(1)
#aqui hace click en settings
driver.find_element_by_xpath('//*[@id="guide-list"]/div/div[7]/div/div[1]/div').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="surface"]/div[2]/div/div[3]/div[3]/div/div[7]/div').click()
time.sleep(3)
#aqui hace click en conectar por codigo
#driver.find_element_by_xpath('//*[@id="guide-list"]/div/div[7]/div/div[1]/div').click()
# aqui saca el codigo
code = driver.find_element_by_xpath('//*[@id="surface-content"]/div[1]/div[2]/div[4]')
print code.text
try:
    cond = 'hola'
    while cond == 'hola':
        cond = raw_input('deseas salir?')
        print 'dentro'
    driver.quit()
except Exception as e:
    print e
    driver.quit()
