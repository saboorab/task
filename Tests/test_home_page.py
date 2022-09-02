import time
from BaseSetup.logger import Logger

from BaseSetup.BaseSetup import Base
from Pages.NavigationBarPage import NavigationBar
from Pages.AccountPage import Account
from Pages.HomePage import Home


class TestHomePage(Base):
    log = Logger().get_logger()

    #This method will create a new account for the traveller and will login successfully
    def test_create_an_account(self):
        try:
            self.log.info("creating the new account of traveller test case")
            NavigationBar.hover_action_profile_btn(self)
            NavigationBar.click_on_signup(self)
            NavigationBar.check_as_traveller(self)
            NavigationBar.fill_form_full_name(self)
            NavigationBar.fill_form_email(self)
            NavigationBar.fill_form_password(self)
            NavigationBar.fill_form_repeat_password(self)
            NavigationBar.click_send_form(self)
            assert str(Account.get_greetings_txt(self)) == str("Hello " + NavigationBar.get_form_full_name(self) + "!")
        except Exception as e:
            self.log.error("An Exception occurred:" + str(e))
            raise Exception



    # test_search_for_a_trip will verify search and the result title agaisnt the selected adventures
    def test_search_a_trip(self):
        try:
            self.log.info("test_search_for_a_trip will verify search and the result title agaisnt the selected adventures")
            Home.click_search_btn(self)
            Home.select_where_destination(self)
            Home.click_search_btn(self)
            assert Home.get_search_result_title_text(self) == 'India Tours & Trips'
        except Exception as e:
            self.log.error("An Exception occurred:" + str(e))
            raise Exception

    # test_sent_broshure_email will send broshure to the email address provided
    def test_sent_broshure_email(self):
        try:
            self.log.info("test_sent_broshure_email will send broshure to the email address provided")
            Home.click_search_btn(self)
            Home.select_where_destination(self)
            Home.click_search_btn(self)
            Home.downlaod_broshure(self)
            Home.getemailbroshure(self)
            Home.downlaod_broshure_email_popup(self)
            assert Home.broshure_sent(self) =='Brochure successfully sent!'
        except Exception as e:
            self.log.error("An Exception occurred:" + str(e))
            raise Exception

    #This method will filter on the basis of amount range and verify the result
    def test_search_filter_budget(self):
        try:
            self.log.info("This method will filter on the basis of amount range and verify the result")
            Home.click_search_btn(self)
            Home.select_where_destination(self)
            Home.click_search_btn(self)
            Home.select_budget_range(self)
            Home.assert_budget_range(self)
        except Exception as e:
            self.log.error("An Exception occurred:" + str(e))
            raise Exception


    #End to End scenario for entering any tour in the wishlist and then removing it
    def test_wishlist_save_delete(self):
        try:
            self.log.info("End to End scenario for entering any tour in the wishlist and then removing it")
            NavigationBar.hover_action_profile_btn(self)
            NavigationBar.click_on_login(self)
            NavigationBar.fill_form_login_email(self)
            NavigationBar.fill_form_login_password(self)
            NavigationBar.click_send_form(self)
            Home.select_where_destination(self)
            Home.click_search_btn(self)
            Home.click_first_tour_view(self)
            Home.click_tour_wishlist_icon(self)
            Home.click_navbar_wishlist_icon(self)
            assert Account.count_wishlist_items(self) == 1
            Account.click_on_account_wishlist_icon(self)
            Account.click_on_modal_wishlist_icon(self)
            Account.click_on_modal_done_btn(self)
            assert Account.count_wishlist_items(self) == 0
        except Exception as e:
            self.log.error("An Exception occurred:" + str(e))
            raise Exception

