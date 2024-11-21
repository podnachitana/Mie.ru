from pages.main_page import MainPage
from pages.my_data_page import MyDataPage


def test_buy_jewelry(set_up):
    driver = set_up

    main_page = MainPage(driver)
    main_page.authorization()
    main_page.my_account()

    mdp = MyDataPage(driver)
    mdp.checking()

