#importar el paquete webdriver que viene de la libreria selenium
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


#Aperturar mi navegador
driver = webdriver.Chrome()

#Ruta dentro del navegador
driver.get("https://evirtual.utm.edu.ec")

#Actualizar
driver.refresh()

#Usuario
usuario = driver.find_element(By.NAME,"username")
usuario.send_keys("jalcivar2478@utm.edu.ec")

#Contraseña
password = driver.find_element(By.NAME,"password")
password.send_keys("*********")

#Acciones
login = driver.find_element(By.ID,"loginbtn").click()
#Cursos
cursos = driver.find_element(By.CLASS_NAME,"nav-link").click()
#Control de la calidad del Software
ccs = driver.find_element(By.LINK_TEXT,"CONTROL DE CALIDAD DEL SOFTWARE (ING SOFT 2021) - 2024P1 - oscar.lopez").click()

#ingresar a la unidad 3 y 4
u3y4=driver.find_element(By.LINK_TEXT,"UNIDAD 3 y 4").click()

# ingreso al foro 
fr=driver.find_element(By.LINK_TEXT,"FORO - Estrategias para la tolerancia ante fallos").click()

#añadir tema de debate
tma=driver.find_element(By.LINK_TEXT,"Añadir un nuevo tema de debate").click()

#Insertar el foro con Selenium
ttle=driver.find_element(By.ID,"id_subject")
ttle.send_keys("Estrategias para la tolerancia a fallos")


sleep(3)

# Cambiar al iframe utilizando su ID
iframe = driver.find_element(By.ID, "id_message_ifr")
driver.switch_to.frame(iframe)

# Leer el contenido del archivo HTML
with open('foro.html', 'r', encoding='utf-8') as file:
    foro = file.read()

# Encontrar el elemento dentro del iframe y escribir el texto deseado
elem = driver.find_element(By.ID, "tinymce")
driver.execute_script("arguments[0].innerHTML = arguments[1];", elem, foro)


#volver al contexto principal de la página
driver.switch_to.default_content()

#enviar el foro 
enviar_foro=driver.find_element(By.ID, 'id_submitbutton').click()


#Espera
sleep(100)