from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd

chrome_options=Options()
chrome_options.add_argument("--user-data-dir=chrome-data")
driver = webdriver.chrome('chromedriver.exe', Options=chrome_options)
driver.get('https://web.whatsapp.com/')

interesados = WebDriverWait(driver, 40).until(lambda driver:driver.find_elements_by_xpath('//div[@class="_2aBzC"]'))

numero = []
fecha = []
todo = []

for interesado in interesados:
    contenido1=interesado.find_element_by_xpath('.//span[@dir="auto"]').text
    numero.append(contenido1)
    contenido2=interesado.find_element_by_xpath('.//div[@class="_15smv"]').text
    fecha.append(contenido2)
    contenido3=interesado.find_element_by_xpath('.//div[@class="_1SjZ2"]').text
    todo.append(contenido3)


resultado=[numero, fecha, todo]
df=pd.DataFrame(resultado).T
df.columns=['numero', 'fecha', 'ultimo_mensaje']
print(df)
