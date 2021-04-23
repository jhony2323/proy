#Aqui tenemos las librerias
import time
#funciones
def tm():
    products=p.split(",")
    np=len(products)
    return int((np*50)/60)
def enter(m):
    return orden.append(m)
orden=[]#lista donde se emplearan las colas
#mensaje para saludar al usuario y explicación de como ordenar
print("""        *BIENVENIDO A AUTOMARKET*
     donde te atendemos al instante
""")
print("*Por favor escribe tu nombre*")
n=input()
print("*Por favor escribe la dirección a la que deseas que se envie el pedido*")
d=input()
print(f"""*Hola! {n}*, para poder ayudarte, ingresa por favor los productos que deseas
*separados por comas* y *en un solo mensaje*.""")
p=input()
#En este aparteado se encuentan los datos que ingresa el usuario
enter(n)
enter(d)
T=tm()
t=(T*60)  
if T==1:
    print(f"en {T} minuto saldra tu orden")
elif T==0:
    t+=60
    print(f"en 1 minuto saldra tu orden")
else:
    print(f"en {T} minutos saldra tu orden")  #el tiempo estimado es el tiempo que tardara en enviarse el mensaje de confirmación
time.sleep(t)                             
#mesajes de confirmación
print(f"""ya esta lista su orden y se enviara a *{orden[1]}*
""") 
print(f"""*Gracias por darnos el gusto de atenderte {orden[0]}
y recuerda que en Automarkert te atendemos al instante*""")