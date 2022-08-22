import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from MainStuff.main_page import Mainpage

class TestSearh():

    @pytest.fixture
    def Test_inicialP(self):

        #******************* configuraciones de selenium *******************

        option = webdriver.ChromeOptions()
        option.add_argument("start-maximized")


        option.add_experimental_option("detach", True) # chrome to stay open

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
        self.wait = WebDriverWait(self.driver,10)

        # ****************************************************************************************************

        self.page = Mainpage(self.driver,self.wait)
        self.page.ir_pagina_busc()

    #################### TESTS ######################

    ###### puebas url ##############################

    def test_url(self,Test_inicialP):
        self.page.chek_url("https://youtube.com")

    #################### Login tests ########################

    def test_login_fail_empty(self,Test_inicialP):
        self.page.login_fail_empty('','')

    def test_login_success_empty(self,Test_inicialP):
        self.page.login_success_empty('brpolanco14@gmail.com','123456')


    def test_login_fail(self,Test_inicialP):
        self.page.login_success_empty('brpolanco14','123456')


    def test_login_success(self,Test_inicialP):
        self.page.login_success('brpolanco14@gmail.com','123456')

    ################## Login baneado ########################
    def test_login_baneo_fail(self,Test_inicialP):
        self.page.log_baneo_fail('carlos@gmail.com','123456')

    def test_login_baneo_succes(self,Test_inicialP):
        self.page.log_baneo_succes('br@gmail.com','123456')
    ###################### checkout products tests ###########

    def test_fail_add_contacts(self,Test_inicialP):
        self.page.fail_add_contacts('bryan@gmail.com','123456','','','','')


    def test_success_add_contacts(self,Test_inicialP):
        self.page.success_add_contacts('bryan@gmail.com','123456','Bryan','Polanco','8494556438','brpolanco14@gmail.com')

    def test_success_busqueda(self,Test_inicialP):
        self.page.success_busqueda('bryan@gmail.com','123456','Bryan','Polanco','8494556438','brpolanco14@gmail.com','Carlos','Castillo','8096665585','carlos3@gmail.com','Bryan')

    def test_fail_busqueda(self,Test_inicialP):
        self.page.fail_busqueda('brpolanco14@gmail.com','123456','Bryan')

    def test_success_almacenamiento(self,Test_inicialP):
        self.page.success_almacenamiento('brpolanco14@gmail.com','123456','Bryan','Polanco','8494556438','brpolanco14@gmail.com','Carlos','Almonte','8097660603','carlos@gmail.com')

    def test_fail_almacenamiento(self,Test_inicialP):
        self.page.fail_almacenamiento('brpolanco14@gmail.com','123456')


    def test_success_registro(self,Test_inicialP):
        self.page.success_registro('Bryan Polanco','bryanpolanco14@hotmail.com','123456')

    def test_fail_registro(self,Test_inicialP):
        self.page.fail_registro('','','')

    def test_success_logout(self,Test_inicialP):
        self.page.success_logout('brpolanco14@gmail.com','123456')

    def test_fail_logout(self,Test_inicialP):
        self.page.fail_logout('brpolanco14@gmail.com','123456')

    def test_success_eliminar(self,Test_inicialP):
        self.page.success_eliminar('brpolanco14@gmail.com','123456','Bryan','Polanco','8494556438','brpolanco14@gmail.com','Carlos','Jimenez','8097660603','carlos@gmail.com')

    def test_fail_eliminar(self,Test_inicialP):
        self.page.fail_eliminar('brpolanco14@gmail.com','123456','Bryan','Polanco','8494556438','brpolanco14@gmail.com','Carlos','Jimenez','8097660603','carlos@gmail.com')





