from selenium import webdriver
from selenium.webdriver.support.ui import Select
import csv
from time import sleep

class FoodServiceDriver:

    def __init__(self, un, pw, sleep=3):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.username = un
        self.password = pw
        self.wait_time = sleep

    def login(self):
        self.driver.get("http://127.0.0.1:8000")
        sleep(self.wait_time)

        # Click login
        self.driver.find_element_by_xpath('/html/body/nav/div/div[2]/ul[2]/li/a').click()

        # Enter Username
        sleep(self.wait_time)
        login_box = self.driver.find_element_by_xpath('/html/body/div/div/div/form/p[1]/input')
        login_box.send_keys(self.username)

        # Enter Password
        sleep(self.wait_time)
        pass_box = self.driver.find_element_by_xpath('/html/body/div/div/div/form/p[2]/input')
        pass_box.send_keys(self.password)

        # Enter
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div/div/div/form/input[2]').click()

    def customer_add_admin(self, cust_info):
        sleep(self.wait_time)
        # Go to admin panel
        self.driver.get("http://127.0.0.1:8000/admin/")

        # Click add forcustomer table
        self.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[1]/a').click()

        # Name
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/form/div/fieldset/div[1]/div/input').send_keys(cust_info[0])

        # Organization
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/form/div/fieldset/div[2]/div/input').send_keys(cust_info[1])

        # Role
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/form/div/fieldset/div[3]/div/input').send_keys(cust_info[2])

        # Email
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/form/div/fieldset/div[4]/div/input').send_keys(cust_info[3])

        # bldgroom
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/form/div/fieldset/div[5]/div/input').send_keys(cust_info[4])

        # Address
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/form/div/fieldset/div[6]/div/input').send_keys(cust_info[5])

        # Account number
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/form/div/fieldset/div[7]/div/input').send_keys(cust_info[6])

        # City
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/form/div/fieldset/div[8]/div/input').send_keys(cust_info[7])

        # State
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/form/div/fieldset/div[9]/div/input').send_keys(cust_info[8])

        # Zip
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/form/div/fieldset/div[10]/div/input').send_keys(cust_info[9])

        # Number
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/form/div/fieldset/div[11]/div/input').send_keys(cust_info[10])

        # Save
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/form/div/div/input[1]').click()


    def clean_up(self):
        # Log out
        self.driver.get("http://127.0.0.1:8000")
        sleep(self.wait_time)

        # Click drop down menu then log out
        self.driver.find_element_by_xpath('/html/body/nav/div/div[2]/ul[2]/li/a').click()
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/nav/div/div[2]/ul[2]/li/ul/li/a').click()

        # Close chrome driver
        self.driver.close()


def read_excel_file(filename):
    with open(filename) as csv_file:
        reader = csv.reader(csv_file)
        list_data = list(reader)
    return list_data

if __name__ == '__main__':
    customer_list = read_excel_file("Maverick Food Service Sample Data - Customers.csv")

    food_services = FoodServiceDriver('markcoldanghise', 'auto_test_pass123!!', sleep=0)
    food_services.login()

    for customer in customer_list:
        food_services.customer_add_admin(customer)

    food_services.clean_up()


