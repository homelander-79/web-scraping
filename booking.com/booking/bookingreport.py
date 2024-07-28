from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By


class BookingReport():
    def __init__(self,box_section_element: WebElement):
        self.box_section_element= box_section_element
        self.deal_boxes=self.pull_deal_boxes()
    
    def pull_deal_boxes(self):
        return self.box_section_element.find_elements(By.CSS_SELECTOR,'div.d8ff70c6e0.bb80b6397f')
    
    def pull_deal_box_attributes(self):

        collection=list()

        for deal_boxe in self.deal_boxes:
            with open('file_name', "w", encoding="utf-8") as file:
                 file.write(deal_boxe.get_attribute('innerHTML'))
            

            name= deal_boxe.find_element(By.CSS_SELECTOR,'div[data-testid="title"]').get_attribute('innerHTML')
            price= deal_boxe.find_element(By.CSS_SELECTOR,'span.ab91cb3011').get_attribute('innerHTML')
            score=None
            reviews=None

            try:
                score = deal_boxe.find_element(By.CSS_SELECTOR, 'div.fd44f541d8').get_attribute('innerHTML')
                reviews = deal_boxe.find_element(By.CSS_SELECTOR, 'div.c60bada9e4').get_attribute('innerHTML')
            except: pass
           
            print([name,score,reviews,price])
            collection.append([name,score,reviews,price])
        
        return collection