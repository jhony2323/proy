from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait


browser = webdriver.Edge(executable_path='./driver/msedgedriver')

def selccionarChat(NOMBRE : str):
    buscando = True

    while buscando:
        print("Buscando el chat")
        elements = browser.find_elements_by_tag_name("span")
        for element in elements:
            if element.text == NOMBRE:
                print("Encontramos el chat")
                element.click()
                buscando = False
                break

def enviar():

    element = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]')
    element.click()
    print("mensaje enviado")
    

def datos():
    interesados = WebDriverWait(browser, 40).until(lambda browser:browser.find_elements_by_xpath('//div[@class="_2aBzC"]'))
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

    import pandas as pd
    resultado=[numero, fecha, todo]
    df=pd.DataFrame(resultado).T
    df.columns=['numero', 'fecha', 'ultimo_mensaje']
    df[['ultimo_mensaje','contador']]=df['ultimo_mensaje'].str.split("\n", expand=True)
    df2=df.dropna()
    print(df2)


#def enviarMensaje(mensaje : str):
    #chatbox = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    #chatbox.send_keys(mensaje)
    #time.sleep(2)
    #enviar()

def enviarMensaje1():
    chatbox = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    chatbox.send_keys("""*....BIENVENIDO A AUTOMARKRT....* 
    *Dónde te atenderemos al instante* 
    *Por favor digite su nombre:*""")
    time.sleep(2)
    enviar()


def leerArchivo(ruta: str):
    archivo = open(ruta, mode='r', encoding='utf-8')
    chatbox = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    
    for linea in archivo.readlines():
        print("MENSAJE : ", linea )
        chatbox.send_keys(linea)

    archivo.close()



def validaQR():
    try:
        element = browser.find_element_by_tag_name("canvas")
    except:
        return False
    return True


def estructurMsm():
    hola


def botwhatsapp():
    browser.get("https://web.whatsapp.com/")
    time.sleep(5)

    espera = True

    while espera:
        print("Estoy esperando ")
        espera = validaQR()
        time.sleep(2)
        if espera == False:
            print("Se autentico")
            break
        
    chat = selccionarChat('PRUEBA')
    time.sleep(2)
    enviarMensaje1()



botwhatsapp()

print(datos())