from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from django.urls import reverse

class EquipamentoE2ETest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_create_equipamento(self):
        self.browser.get(f'{self.live_server_url}{reverse("equipamento-create")}')
    
        nome_input = self.browser.find_element(By.NAME, 'nome')
        nome_input.send_keys('Equipamento Teste')
        
        tipo_input = self.browser.find_element(By.NAME, 'tipo')
        tipo_input.send_keys('Tipo Teste')
    
        fabricante_input = self.browser.find_element(By.NAME, 'fabricante')
        fabricante_input.send_keys('Fabricante Teste')
    
        modelo_input = self.browser.find_element(By.NAME, 'modelo')
        modelo_input.send_keys('Modelo Teste')
    
        numero_serie_input = self.browser.find_element(By.NAME, 'numero_serie')
        numero_serie_input.send_keys('123456')
    
        data_compra_input = self.browser.find_element(By.NAME, 'data_compra')
        data_compra_input.send_keys('2024-09-01')
    
        valor_compra_input = self.browser.find_element(By.NAME, 'valor_compra')
        valor_compra_input.send_keys('1000.00')
    
        status_input = self.browser.find_element(By.NAME, 'status')
        status_input.send_keys('Ativo')
    
        data_ultima_manutencao_input = self.browser.find_element(By.NAME, 'data_ultima_manutencao')
        data_ultima_manutencao_input.send_keys('2024-08-01')
    
        data_proxima_manutencao_input = self.browser.find_element(By.NAME, 'data_proxima_manutencao')
        data_proxima_manutencao_input.send_keys('2024-12-01')
    
        descricao_input = self.browser.find_element(By.NAME, 'descricao')
        descricao_input.send_keys('Descrição do equipamento de teste.')
    
        submit_button = self.browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        submit_button.click()
    
        self.assertIn('Equipamento Teste', self.browser.page_source)
