from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BookingFiltration:
    def __init__(self,driver: WebDriver) :
        self.driver=driver

    def apply_star_rating(self,*stars):
        try:
            star_filtration_box = self.driver.find_element(By.XPATH,'//div[@data-filters-group="class" and @data-testid="filters-group"]')
            star_child_elements = star_filtration_box.find_elements(By.CSS_SELECTOR, "div input.f8f9295ba2")

            for star in stars:
                for star_element in star_child_elements :

                    if  str(star_element.get_attribute('aria-label'))[0]==str(star):
                        star_element.click()
                
        except Exception as e:
            self.apply_star_rating(self,*stars)

        
    def sort_price_lowest_first(self):

        sort_options = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'f202e3a5e2'))
        )
        sort_options.click()
        
        # Wait for the "Price (lowest first)" option to be clickable and click it
        lowest_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "dba1b3bddf") and contains(@class, "da38b23449") and contains(@class, "c944eb558d") and contains(@class, "a2ce59f28d")]//div//span[text()="Price (lowest first)"]'))
        )
        lowest_element.click()
        