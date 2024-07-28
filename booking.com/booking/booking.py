from booking.constant import BASE_URL
from booking.booking_filtration import BookingFiltration
from booking.bookingreport import BookingReport

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

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
        
        try: self.find_element(By.CSS_SELECTOR,'button.b02ceec9d7').click()
        except: pass

    def change_currency(self, currency=None):

        currency_element = self.find_element(By.CSS_SELECTOR, 'button.dba1b3bddf.e99c25fd33.aabf155f9a.f1c8772a7d.a8c0f5611f')
        currency_element.click()

        selected_currency_element = self.find_element(By.XPATH, f'//button//span[@class="f7411e05ae"]//div[text()="{currency}"]')
        ActionChains(self).pause(1).click(selected_currency_element).pause(3).perform()


    def selecte_palce_to_go(self,palce_to_go):

        search_field= WebDriverWait(self,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'input.ada65db9b5'))) 
        ActionChains(self).click(search_field).send_keys(palce_to_go).pause(3).perform()

        ok= WebDriverWait(self,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'li#autocomplete-result-0')))
        ActionChains(self).click(ok).pause(2).perform()
    
    
    def selecte_date(self, check_in, check_out):

        check_in_element= self.find_element(By.XPATH,f'//div[@class="e9d4960a84"]//table//tbody//tr//td//span[@data-date="{check_in}"]')
        check_out_element= self.find_element(By.XPATH,f'//div[@class="e9d4960a84"]//table//tbody//tr//td//span[@data-date="{check_out}"]')
        
        ActionChains(self).click(check_in_element).click(check_out_element).pause(1).perform()
        
    
    def selecte_adualt(self,count=1):

        selecte_adualt_element= WebDriverWait(self,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'div.a6391e882c')))
        selecte_adualt_element.click()
        
        adualt_num=int(self.find_element(By.CSS_SELECTOR,'div.f71ad9bb14 span.fb7047f72a').text)

        up_down= None
        up=False

        if adualt_num>count:
            up_down=  WebDriverWait(self,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'button.af4d87ec2f')))
        elif adualt_num< count:
            up_down=  WebDriverWait(self,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'button.e137a4dfeb.d1821e6945')))
            up=True
        
        
        while adualt_num!= count:
            if up == True : adualt_num+=1
            else: adualt_num -= 1
            up_down.click()


        WebDriverWait(self,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'button.ed852f1b1f.c437808707'))).click()
        

    def click_serach(self):

        WebDriverWait(self,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'button[type=submit]'))).click()

    def booking_filtration(self):
        
        filtration= BookingFiltration(driver=self)
        filtration.sort_price_lowest_first()
        filtration.apply_star_rating(1,5)

    def report_result(self):

        scrolller= self.find_element(By.TAG_NAME,'body')

        while True:
            try:
                if self.find_element(By.CSS_SELECTOR,'div.e01df12ddf.d399a62c2a'):
                    break
            except :
                scrolller.send_keys(Keys.END)

        container= WebDriverWait(self,10).until(EC.presence_of_element_located((By.CLASS_NAME,'f9958fb57b')))

        report= BookingReport(container)
        data= report.pull_deal_box_attributes()
        print(data)
        
            

        