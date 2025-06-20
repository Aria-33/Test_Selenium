# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class Test003_test_cTCATDELETE():
    def test_cTCATDELETE003(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        
        # Connexion
        self.driver.get("http://localhost:3000/admin/login")
        email_field = self.wait.until(EC.presence_of_element_located((By.NAME, "email")))
        email_field.send_keys("oddone.lea@gmail.com")
        
        password_field = self.wait.until(EC.presence_of_element_located((By.NAME, "password")))
        password_field.send_keys("a123456789")
        
        login_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button")))
        login_button.click()
        
        # Navigation vers Categories
        categories_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Categories")))
        categories_link.click()
        
        # Création de la catégorie initiale
        add_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button > span")))
        add_button.click()
        
        # Remplissage du formulaire
        name_field = self.wait.until(EC.presence_of_element_located((By.ID, "name")))
        name_field.send_keys("Mariage")
        
        url_key_field = self.wait.until(EC.presence_of_element_located((By.ID, "urlKey")))
        url_key_field.send_keys("mariage")
        
        meta_title_field = self.wait.until(EC.presence_of_element_located((By.ID, "metaTitle")))
        meta_title_field.send_keys("Mariage")
        
        meta_keywords_field = self.wait.until(EC.presence_of_element_located((By.ID, "metakeywords")))
        meta_keywords_field.send_keys("mariage")
        
        meta_description_field = self.wait.until(EC.presence_of_element_located((By.ID, "meta_description")))
        meta_description_field.send_keys("Mariage")
        
        # Sauvegarde de la catégorie
        save_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".primary > span")))
        save_button.click()
        
        # Attendre que la catégorie soit créée et cliquer dessus
        category_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Mariage")))
        category_link.click()
        
        # Modification de la catégorie
        name_field = self.wait.until(EC.presence_of_element_located((By.ID, "name")))
        name_field.clear()
        name_field.send_keys("Mariage et pacs")
        
        url_key_field = self.wait.until(EC.presence_of_element_located((By.ID, "urlKey")))
        url_key_field.clear()
        url_key_field.send_keys("mariage-et-pacs")
        
        meta_title_field = self.wait.until(EC.presence_of_element_located((By.ID, "metaTitle")))
        meta_title_field.clear()
        meta_title_field.send_keys("Mariage et pacs")
        
        meta_keywords_field = self.wait.until(EC.presence_of_element_located((By.ID, "metakeywords")))
        meta_keywords_field.clear()
        meta_keywords_field.send_keys("mariage et pacs")
        
        meta_description_field = self.wait.until(EC.presence_of_element_located((By.ID, "meta_description")))
        meta_description_field.clear()
        meta_description_field.send_keys("Mariage et pacs")
        
        # Sauvegarde des modifications
        save_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".primary")))
        save_button.click()
        
        # Retour à la liste des catégories
        categories_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Categories")))
        categories_link.click()
        
        # Sélection de la catégorie à supprimer
        checkbox = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "tr:nth-child(2) .checkbox-unchecked")))
        checkbox.click()
        
        # Clic sur le bouton de suppression
        delete_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".font-semibold > span")))
        delete_button.click()
        
        # Confirmation de la suppression
        confirm_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".critical > span")))
        confirm_button.click()
  
