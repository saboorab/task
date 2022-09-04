from Pages.HomePageLocators import HomePageLocators
from Pages.NavigationBarLocators import NavigationBarLocators
from selenium.webdriver.common.keys import Keys
import time


class Home:
    def select_where_destination(self):
        self.driver.find_element_by_xpath(HomePageLocators.search_where).send_keys('India')
        self.driver.find_element_by_xpath(HomePageLocators.search_where).send_keys(Keys.TAB)
        time.sleep(2)

    def downlaod_broshure(self):
        self.driver.find_element_by_xpath(HomePageLocators.download_brochure).click()
        time.sleep(2)

    def getemailbroshure(self):
        self.driver.find_element_by_xpath(HomePageLocators.enter_email).send_keys("07se81@gmail.com")
        time.sleep(2)

    def downlaod_broshure_email_popup(self):
        self.driver.find_element_by_xpath(HomePageLocators.downlaodbrochureemail_popup).click()
        time.sleep(2)

    def get_rating(self):

        overallrating=self.driver.find_element_by_xpath(HomePageLocators.overallrating).text
        return overallrating


    def get_checkavailability_month(self):

        self.driver.find_element_by_xpath(HomePageLocators.Checkavailabilitymonth).click()
        time.sleep(2)

    def get_hold_space(self):
        self.driver.find_element_by_xpath(HomePageLocators.holdspaceforhours).click()
        time.sleep(10)



    def broshure_sent(self):
        broshuretext=self.driver.find_element_by_xpath(HomePageLocators.broshuresuccessfullysent).text
        return broshuretext
        time.sleep(2)

    def select_when_destination(self):
        self.driver.find_element_by_xpath(HomePageLocators.search_when).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(HomePageLocators.search_month).click()

    def select_who_destination(self):
        self.driver.find_element_by_xpath(HomePageLocators.search_who).click()
        time.sleep(1)

    def click_search_btn(self):
        self.driver.find_element_by_xpath(HomePageLocators.search_btn).click()
        time.sleep(2)

    def click_first_wishlist_icon(self):
        time.sleep(1)
        self.driver.find_element_by_xpath(HomePageLocators.search_icon_wishlist).click()

    def click_navbar_wishlist_icon(self):
        self.driver.find_element_by_xpath(NavigationBarLocators.saved_tours).click()

    def click_first_tour_view(self):
        time.sleep(1)
        self.driver.find_element_by_xpath(HomePageLocators.tour_view_btn).click()

    def click_tour_wishlist_icon(self):
        p = self.driver.current_window_handle
        chwd = self.driver.window_handles
        for w in chwd:
            if (w != p):
                self.driver.switch_to.window(w)
        time.sleep(1)
        element = self.driver.find_element_by_xpath("//*[contains(@class, 'price-block')]")
        element.location_once_scrolled_into_view
        time.sleep(2)
        self.driver.find_element_by_xpath(HomePageLocators.tour_view_wishlist_button).click()

    def get_search_result_title_text(self):
        search_text = self.driver.find_element_by_xpath(HomePageLocators.search_title_result).text
        return search_text

    def select_budget_range(self):
        self.driver.get(self.driver.current_url + "#budget=1000-1500")
        self.driver.refresh()

    def get_all_description_values(self):
       return self.driver.find_elements_by_xpath(HomePageLocators.description_value)


    def assert_budget_range(self):
        time.sleep(2)
        values = Home.get_all_description_values(self)
        for value in values:
            if int(value.text) >1000 and int(value.text) <1500:
                return True
            else:
                return False



        
