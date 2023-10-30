import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.remote.webdriver import By
from time import sleep
import requests
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import requests
from pprint import pprint
from datetime import datetime


class Login:

    def logging(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://web.whatsapp.com/")
        count = 0
        while True:
            element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[3]/div[1]/div/div/div[2]/div/div/span')))
            if element:
                pprint("leia o qr-code para efetuar o login do seu whatsapp 😁")
                break
            else:
                print("Not qr_code")
                self.driver.get("https://web.whatsapp.com/")
                count += 1
                if count == 3:
                    print("O bot tentou logar 3 vezes,\nmas infelizmente o site não está carregando.")
    def verify(self):
        try:
            verificando = WebDriverWait(self.driver,50).until(EC.presence_of_element_located((By.XPATH,'//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p')))
            print("login realizado com sucesso!")
        except: 
            print("Infelizmente não conseguiu realizar login.")
    def automation(self):
        pass
        
            
       
                


            


    
    

whatsap = Login()
whatsap.logging()
whatsap.verify()

