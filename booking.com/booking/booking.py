from time import sleep
from booking.constant import BASE_URL
from booking.booking_filtration import BookingFiltration

from selenium import webdriver
from selenium.webdriver.common.by import By


import os

class Booking(webdriver.Chrome):


    def __init__(self,driver_path='../',teardown=False) :

        self.driver_path = driver_path
        self.teardown= teardown
        os.environ['PATH'] += self.driver_path

        super(Booking,self).__init__()

        self.implicitly_wait(15)
        self.maximize_window()

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc, traceback):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(BASE_URL)
        try:
            popup= self.find_element(By.CSS_SELECTOR,'button[class="dba1b3bddf e99c25fd33 aabf155f9a f42ee7b31a a86bcdb87f b02ceec9d7"]')
            popup.click()
        except :
            pass

    def change_currency(self, currency=None):
        currency_element = self.find_element(By.CSS_SELECTOR, 'button.dba1b3bddf.e99c25fd33.aabf155f9a.f1c8772a7d.a8c0f5611f')
        currency_element.click()

        selected_currency_element = self.find_element(By.XPATH, f'//button//span[@class="f7411e05ae"]//div[text()="{currency}"]')
        selected_currency_element.click()

        sleep(3)


    def selecte_palce_to_go(self,palce_to_go):
        search_field=  self.find_element(By.CSS_SELECTOR,'input.ada65db9b5')
        search_field.clear()
        search_field.send_keys(palce_to_go)
        
        sleep(3)

        first_result= self.find_element(By.CSS_SELECTOR,'li#autocomplete-result-0')
        first_result.click()
    
    def selecte_date(self, check_in, check_out):
        check_in_element= self.find_element(By.XPATH,f'//div[@class="e9d4960a84"]//table//tbody//tr//td//span[@data-date="{check_in}"]')
        check_in_element.click()

        check_out_element= self.find_element(By.XPATH,f'//div[@class="e9d4960a84"]//table//tbody//tr//td//span[@data-date="{check_out}"]')
        check_out_element.click()
    
    def selecte_adualt(self,count=1):
        selecte_adualt_element= self.find_element(By.CSS_SELECTOR,'div.a6391e882c')
        selecte_adualt_element.click()
        
        adualt_num=int(self.find_element(By.CSS_SELECTOR,'div.f71ad9bb14 span.fb7047f72a').text)

        up_down= None
        up=False

        if adualt_num>count:
            up_down=  self.find_element(By.CSS_SELECTOR,'button.af4d87ec2f')
        elif adualt_num< count:
            up_down= self.find_element(By.CSS_SELECTOR,'button.e137a4dfeb.d1821e6945')
            up=True
        
        
        while adualt_num!= count:
            if up == True : adualt_num+=1
            else: adualt_num -= 1
            up_down.click()


        done_element= self.find_element(By.CSS_SELECTOR,'button.ed852f1b1f.c437808707')
        done_element.click()
        

    def click_serach(self):
        search_button= self.find_element(By.CSS_SELECTOR,'button[type=submit]')
        search_button.click()

    def booking_filtration(self):
        
        filtration= BookingFiltration(driver=self)
        filtration.apply_star_rating()