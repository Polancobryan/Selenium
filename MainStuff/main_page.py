import time
from selenium.webdriver.support import expected_conditions as EC
from MainStuff.base import Base
from selenium.webdriver.common.by import By


class Mainpage(Base):

    def __init__(self,driver,wait):
        self.url = 'http://127.0.0.1:5500/Agenda%20de%20contactos/loginvista.html'

        super().__init__(driver, wait)

    def ir_pagina_busc(self):
        self.ir_pagina(self.url)

    def chek_url(self,url):
        assert self.give_url() == url



    def login_fail_empty(self,username,password):

        self.driver.find_element(By.XPATH,"// *[@id='correo']").send_keys(username)
        self.driver.find_element(By.XPATH,"//*[@id='clave']").send_keys(password)
        self.driver.find_element(By.XPATH,"//*[@id='button']").click()

        self.wait.until(EC.presence_of_element_located((By.XPATH,"/ html / body / div / div")))
        time.sleep(3)
        self.driver.save_screenshot('C:/Users/bryan/Desktop/pyTestSwagLabs/results/login_fail.png')


    def login_success_empty(self,username,password):

        self.driver.find_element(By.XPATH,"// *[@id='correo']").send_keys(username)
        self.driver.find_element(By.XPATH,"//*[@id='clave']").send_keys(password)
        self.driver.find_element(By.XPATH,"//*[@id='button']").click()

        self.wait.until(EC.presence_of_element_located((By.XPATH,"/ html / body / div / div")))
        time.sleep(3)
        self.driver.save_screenshot('C:/Users/bryan/Desktop/pyTestSwagLabs/results/login_succes.png')




    def login_success(self,username,password):

        self.driver.find_element(By.XPATH,"// *[@id='correo']").send_keys(username)
        self.driver.find_element(By.XPATH,"//*[@id='clave']").send_keys(password)
        self.driver.find_element(By.XPATH,"//*[@id='button']").click()

        self.wait.until(EC.presence_of_element_located((By.XPATH,"/ html / body / div / div")))
        time.sleep(2)

        self.driver.save_screenshot('C:/Users/bryan/Desktop/pyTestSwagLabs/results/login_succes.png')

    def login_fail(self,username,password):

        self.driver.find_element(By.XPATH,"// *[@id='correo']").send_keys(username)
        self.driver.find_element(By.XPATH,"//*[@id='clave']").send_keys(password)
        self.driver.find_element(By.XPATH,"//*[@id='button']").click()

        self.wait.until(EC.presence_of_element_located((By.XPATH,"/ html / body / div / div")))
        time.sleep(2)

        self.driver.save_screenshot('C:/Users/bryan/Desktop/pyTestSwagLabs/results/login_fail.png')



    def log_baneo_fail(self,username,password):

        self.driver.find_element(By.XPATH,"// *[@id='correo']").send_keys(username)
        self.driver.find_element(By.XPATH,"//*[@id='clave']").send_keys(password)
        self.driver.find_element(By.XPATH,"//*[@id='button']").click()

        self.wait.until(EC.presence_of_element_located((By.XPATH,"/ html / body / div / div")))
        time.sleep(2)

        self.driver.save_screenshot('C:/Users/bryan/Desktop/pyTestSwagLabs/results/login_baneo_fail.png')

    def log_baneo_succes(self,username,password):

        self.driver.find_element(By.XPATH,"// *[@id='correo']").send_keys(username)
        self.driver.find_element(By.XPATH,"//*[@id='clave']").send_keys(password)
        self.driver.find_element(By.XPATH,"//*[@id='button']").click()

        self.wait.until(EC.presence_of_element_located((By.XPATH,"/ html / body / div / div")))


        self.driver.save_screenshot('C:/Users/bryan/Desktop/pyTestSwagLabs/results/login_baneo_succes.png')



    def success_add_contacts(self,username,password,nombre,apellido,telefono,correo):


        self.driver.find_element(By.XPATH,"// *[@id='correo']").send_keys(username)
        self.driver.find_element(By.XPATH,"//*[@id='clave']").send_keys(password)
        self.driver.find_element(By.XPATH,"//*[@id='button']").click()
        time.sleep(12)
        self.driver.find_element(By.XPATH,"/html/body/div/div[1]/form/input[1]").send_keys(nombre)
        self.driver.find_element(By.XPATH,"/html/body/div/div[1]/form/input[2]").send_keys(apellido)
        self.driver.find_element(By.XPATH,"/html/body/div/div[1]/form/input[3]").send_keys(telefono)
        self.driver.find_element(By.XPATH,"/html/body/div/div[1]/form/input[4]").send_keys(correo)
        self.driver.find_element(By.XPATH,"/html/body/div/div[1]/form/button/img").click()

        self.wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='swal2-html-container']")))

        self.driver.save_screenshot('C:/Users/bryan/Desktop/pyTestSwagLabs/results/success_add_contacts.png')




    def fail_add_contacts(self,username,password,nombre,apellido,telefono,correo):
        self.driver.find_element(By.XPATH, "// *[@id='correo']").send_keys(username)
        self.driver.find_element(By.XPATH, "//*[@id='clave']").send_keys(password)
        self.driver.find_element(By.XPATH, "//*[@id='button']").click()
        time.sleep(12)
        self.driver.find_element(By.XPATH,"/html/body/div/div[1]/form/input[1]").send_keys(nombre)
        self.driver.find_element(By.XPATH,"/html/body/div/div[1]/form/input[2]").send_keys(apellido)
        self.driver.find_element(By.XPATH,"/html/body/div/div[1]/form/input[3]").send_keys(telefono)
        self.driver.find_element(By.XPATH,"/html/body/div/div[1]/form/input[4]").send_keys(correo)
        self.driver.find_element(By.XPATH,"/html/body/div/div[1]/form/button/img").click()

        self.wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='swal2-html-container']")))

        time.sleep(2)
        self.driver.save_screenshot('C:/Users/bryan/Desktop/pyTestSwagLabs/results/fail_add_contacts.png')




    def success_busqueda(self,username,password,nombre,apellido,telefono,correo,nombre1,apellido1,telefono1,correo1,busqueda):

        self.driver.find_element(By.XPATH, "// *[@id='correo']").send_keys(username)
        self.driver.find_element(By.XPATH, "//*[@id='clave']").send_keys(password)
        self.driver.find_element(By.XPATH, "//*[@id='button']").click()
        time.sleep(12)
        self.driver.find_element(By.XPATH,"/html/body/div/div[1]/form/input[1]").send_keys(nombre)
        self.driver.find_element(By.XPATH,"/html/body/div/div[1]/form/input[2]").send_keys(apellido)
        self.driver.find_element(By.XPATH,"/html/body/div/div[1]/form/input[3]").send_keys(telefono)
        self.driver.find_element(By.XPATH,"/html/body/div/div[1]/form/input[4]").send_keys(correo)
        self.driver.find_element(By.XPATH,"/html/body/div/div[1]/form/button/img").click()
        time.sleep(4)
        self.driver.find_element(By.XPATH,"/html/body/div/div[1]/form/input[1]").send_keys(nombre1)
        self.driver.find_element(By.XPATH,"/html/body/div/div[1]/form/input[2]").send_keys(apellido1)
        self.driver.find_element(By.XPATH,"/html/body/div/div[1]/form/input[3]").send_keys(telefono1)
        self.driver.find_element(By.XPATH,"/html/body/div/div[1]/form/input[4]").send_keys(correo1)
        self.driver.find_element(By.XPATH,"/html/body/div/div[1]/form/button/img").click()
        self.driver.save_screenshot('C:/Users/bryan/Desktop/pyTestSwagLabs/results/success_busqueda1.png')
        self.driver.find_element(By.XPATH,"/html/body/form/input").send_keys(busqueda)
        # screenshot cuando es exitoso
        time.sleep(3)
        self.driver.save_screenshot('C:/Users/bryan/Desktop/pyTestSwagLabs/results/success_busqueda2.png')

    def fail_busqueda(self,username,password,busqueda):
        self.driver.find_element(By.XPATH, "// *[@id='correo']").send_keys(username)
        self.driver.find_element(By.XPATH, "//*[@id='clave']").send_keys(password)
        self.driver.find_element(By.XPATH, "//*[@id='button']").click()
        time.sleep(12)
        self.driver.find_element(By.XPATH,"/html/body/form/input").send_keys(busqueda)
        self.driver.save_screenshot('C:/Users/bryan/Desktop/pyTestSwagLabs/results/fail_busqueda.png')


    def success_almacenamiento(self,username,password,nombre,apellido,telefono,correo,nombre1,apellido1,telefono1,correo1):

        self.driver.find_element(By.XPATH, "// *[@id='correo']").send_keys(username)
        self.driver.find_element(By.XPATH, "//*[@id='clave']").send_keys(password)
        self.driver.find_element(By.XPATH, "//*[@id='button']").click()
        time.sleep(12)
        self.driver.find_element(By.XPATH,"/html/body/div/div[1]/form/input[1]").send_keys(nombre)
        self.driver.find_element(By.XPATH,"/html/body/div/div[1]/form/input[2]").send_keys(apellido)
        self.driver.find_element(By.XPATH,"/html/body/div/div[1]/form/input[3]").send_keys(telefono)
        self.driver.find_element(By.XPATH,"/html/body/div/div[1]/form/input[4]").send_keys(correo)
        self.driver.find_element(By.XPATH,"/html/body/div/div[1]/form/button/img").click()
        time.sleep(4)
        self.driver.find_element(By.XPATH,"/html/body/div/div[1]/form/input[1]").send_keys(nombre1)
        self.driver.find_element(By.XPATH,"/html/body/div/div[1]/form/input[2]").send_keys(apellido1)
        self.driver.find_element(By.XPATH,"/html/body/div/div[1]/form/input[3]").send_keys(telefono1)
        self.driver.find_element(By.XPATH,"/html/body/div/div[1]/form/input[4]").send_keys(correo1)
        self.driver.find_element(By.XPATH,"/html/body/div/div[1]/form/button/img").click()
        time.sleep(3)
        self.driver.save_screenshot('C:/Users/bryan/Desktop/pyTestSwagLabs/results/success_almacenamiento.png')

    def fail_almacenamiento(self,username,password):
        self.driver.find_element(By.XPATH, "// *[@id='correo']").send_keys(username)
        self.driver.find_element(By.XPATH, "//*[@id='clave']").send_keys(password)
        self.driver.find_element(By.XPATH, "//*[@id='button']").click()
        time.sleep(12)
        self.driver.save_screenshot('C:/Users/bryan/Desktop/pyTestSwagLabs/results/fail_almacenamiento.png')

    def success_registro(self,nombre,correo,contrasena):

        self.driver.find_element(By.XPATH, "/html/body/form/div/p/a").click()
        self.driver.find_element(By.XPATH,"/html/body/form/div/div[1]/input").send_keys(nombre)
        self.driver.find_element(By.XPATH,"/html/body/form/div/div[2]/input").send_keys(correo)
        self.driver.find_element(By.XPATH,"/html/body/form/div/div[3]/input").send_keys(contrasena)
        self.driver.find_element(By.XPATH,"/html/body/form/div/button").click()

        self.wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='swal2-html-container']")))

        time.sleep(3)
        self.driver.save_screenshot('C:/Users/bryan/Desktop/pyTestSwagLabs/results/success_registro.png')


    def fail_registro(self,nombre,correo,contrasena):

        self.driver.find_element(By.XPATH, "/html/body/form/div/p/a").click()
        self.driver.find_element(By.XPATH,"/html/body/form/div/div[1]/input").send_keys(nombre)
        self.driver.find_element(By.XPATH,"/html/body/form/div/div[2]/input").send_keys(correo)
        self.driver.find_element(By.XPATH,"/html/body/form/div/div[3]/input").send_keys(contrasena)
        self.driver.find_element(By.XPATH,"/html/body/form/div/button").click()

        self.wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='swal2-html-container']")))

        time.sleep(3)
        self.driver.save_screenshot('C:/Users/bryan/Desktop/pyTestSwagLabs/results/fail_registro.png')


    def success_logout(self,username,password):


        self.driver.find_element(By.XPATH,"// *[@id='correo']").send_keys(username)
        self.driver.find_element(By.XPATH,"//*[@id='clave']").send_keys(password)
        self.driver.find_element(By.XPATH,"//*[@id='button']").click()
        time.sleep(12)
        self.driver.find_element(By.XPATH,"// *[ @ id = 'Layer_1']").click()
        self.driver.find_element(By.XPATH,"/ html / body / div[2] / div / div[6] / button[1]").click()
        self.driver.save_screenshot('C:/Users/bryan/Desktop/pyTestSwagLabs/results/success_logout.png')


    def fail_logout(self,username,password):


        self.driver.find_element(By.XPATH,"// *[@id='correo']").send_keys(username)
        self.driver.find_element(By.XPATH,"//*[@id='clave']").send_keys(password)
        self.driver.find_element(By.XPATH,"//*[@id='button']").click()
        time.sleep(12)
        self.driver.find_element(By.XPATH,"// *[ @ id = 'Layer_1']").click()
        self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div[6]/button[2]").click()

        self.driver.save_screenshot('C:/Users/bryan/Desktop/pyTestSwagLabs/results/fail_logout.png')


    def success_eliminar(self, username, password,nombre,apellido,telefono,correo,nombre1,apellido1,telefono1,correo1):


        self.driver.find_element(By.XPATH,"// *[@id='correo']").send_keys(username)
        self.driver.find_element(By.XPATH,"//*[@id='clave']").send_keys(password)
        self.driver.find_element(By.XPATH,"//*[@id='button']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,"/html/body/div/div[1]/form/input[1]").send_keys(nombre)
        self.driver.find_element(By.XPATH,"/html/body/div/div[1]/form/input[2]").send_keys(apellido)
        self.driver.find_element(By.XPATH,"/html/body/div/div[1]/form/input[3]").send_keys(telefono)
        self.driver.find_element(By.XPATH,"/html/body/div/div[1]/form/input[4]").send_keys(correo)
        self.driver.find_element(By.XPATH,"/html/body/div/div[1]/form/button/img").click()
        time.sleep(4)
        self.driver.find_element(By.XPATH,"/html/body/div/div[1]/form/input[1]").send_keys(nombre1)
        self.driver.find_element(By.XPATH,"/html/body/div/div[1]/form/input[2]").send_keys(apellido1)
        self.driver.find_element(By.XPATH,"/html/body/div/div[1]/form/input[3]").send_keys(telefono1)
        self.driver.find_element(By.XPATH,"/html/body/div/div[1]/form/input[4]").send_keys(correo1)
        self.driver.find_element(By.XPATH,"/html/body/div/div[1]/form/button/img").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"/html/body/div/div[2]/ul/li/div/button").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div[6]/button[1]").click()
        time.sleep(2)
        self.driver.save_screenshot('C:/Users/bryan/Desktop/pyTestSwagLabs/results/success_eliminar.png')




    def fail_eliminar(self, username, password,nombre,apellido,telefono,correo,nombre1,apellido1,telefono1,correo1):

        self.driver.find_element(By.XPATH,"// *[@id='correo']").send_keys(username)
        self.driver.find_element(By.XPATH,"//*[@id='clave']").send_keys(password)
        self.driver.find_element(By.XPATH,"//*[@id='button']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,"/html/body/div/div[1]/form/input[1]").send_keys(nombre)
        self.driver.find_element(By.XPATH,"/html/body/div/div[1]/form/input[2]").send_keys(apellido)
        self.driver.find_element(By.XPATH,"/html/body/div/div[1]/form/input[3]").send_keys(telefono)
        self.driver.find_element(By.XPATH,"/html/body/div/div[1]/form/input[4]").send_keys(correo)
        self.driver.find_element(By.XPATH,"/html/body/div/div[1]/form/button/img").click()
        time.sleep(4)
        self.driver.find_element(By.XPATH,"/html/body/div/div[1]/form/input[1]").send_keys(nombre1)
        self.driver.find_element(By.XPATH,"/html/body/div/div[1]/form/input[2]").send_keys(apellido1)
        self.driver.find_element(By.XPATH,"/html/body/div/div[1]/form/input[3]").send_keys(telefono1)
        self.driver.find_element(By.XPATH,"/html/body/div/div[1]/form/input[4]").send_keys(correo1)
        self.driver.find_element(By.XPATH,"/html/body/div/div[1]/form/button/img").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"/html/body/div/div[2]/ul/li/div/button").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div[6]/button[2]").click()
        time.sleep(2)

        self.driver.save_screenshot('C:/Users/bryan/Desktop/pyTestSwagLabs/results/fail_eliminar.png')


