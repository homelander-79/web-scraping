from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver



class BookingFiltration:
    def __init__(self,driver: WebDriver) :
        self.driver=driver

    def apply_star_rating(self):
        try:
            star_filtration_box = self.driver.find_element(By.XPATH,'//div[@data-filters-group="class" and @data-testid="filters-group"]')
            print('\ngame over',star_filtration_box)
            star_child_elements = star_filtration_box.find_elements(By.CSS_SELECTOR, "*")
            print(len(star_child_elements))
        except Exception as e:
            print('error\n', e)

        