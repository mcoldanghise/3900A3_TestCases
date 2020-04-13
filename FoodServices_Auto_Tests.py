from selenium import webdriver
from selenium.webdriver.support.ui import Select
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
        login_box.send_keys('markcoldanghise')

        # Enter Password
        sleep(self.wait_time)
        pass_box = self.driver.find_element_by_xpath('/html/body/div/div/div/form/p[2]/input')
        pass_box.send_keys('#EDCcde3')

        # Enter
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div/div/div/form/input[2]').click()

    def go_to_customer(self):
        sleep(self.wait_time)
        self.driver.get('http://127.0.0.1:8000')

        # Click customer
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/div/div/div[1]/div/div/p[2]/a').click()

    def go_to_services(self):
        sleep(self.wait_time)
        self.driver.get('http://127.0.0.1:8000')

        # Click services
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/div/div/div[2]/div/div/p[2]/a').click()

    def go_to_products(self):
        sleep(self.wait_time)
        self.driver.get('http://127.0.0.1:8000')

        # Click products
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/div/div/div[3]/div/div/p[2]/a').click()


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


    def customer_add_admin(self):
        sleep(self.wait_time)
        # Go to admin panel
        self.driver.get("http://127.0.0.1:8000/admin/")

        # Click add forcustomer table
        self.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[1]/a').click()

        # Name
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/form/div/fieldset/div[1]/div/input').send_keys("John Doe")

        # Organization
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/form/div/fieldset/div[2]/div/input').send_keys('UNO')

        # Role
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/form/div/fieldset/div[3]/div/input').send_keys('Science Advisor')

        # Email
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/form/div/fieldset/div[4]/div/input').send_keys('jdoe@unomaha.edu')

        # bldgroom
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/form/div/fieldset/div[5]/div/input').send_keys('PKI 167')

        # Address
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/form/div/fieldset/div[6]/div/input').send_keys('1111 67th Pacific')

        # Account number
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/form/div/fieldset/div[7]/div/input').send_keys('1')

        # City
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/form/div/fieldset/div[8]/div/input').send_keys('Omaha')

        # State
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/form/div/fieldset/div[9]/div/input').send_keys('NE')

        # Zip
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/form/div/fieldset/div[10]/div/input').send_keys('68124')

        # Number
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/form/div/fieldset/div[11]/div/input').send_keys('402-351-3555')

        # Save
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/form/div/div/input[1]').click()

    def customer_edit(self):
        # Go to customer list
        sleep(self.wait_time)
        self.go_to_customer()

        # Click edit
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div/div/div/div[3]/table/tbody/tr/td[12]/a').click()

        # Edit Role
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div/div/div/form/div[3]/div/input').clear()
        self.driver.find_element_by_xpath('/html/body/div/div/div/form/div[3]/div/input').send_keys('Technology Advisor')

        # Edit Room
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div/div/div/form/div[4]/div/input').clear()
        self.driver.find_element_by_xpath('/html/body/div/div/div/form/div[4]/div/input').send_keys('PKI 171')

        # Save
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div/div/div/form/button').click()

    def customer_delete(self):
        self.go_to_customer()

        # Click delete
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div/div/div/div[3]/table/tbody/tr/td[13]/a').click()

        # Confirm
        alert_obj = self.driver.switch_to.alert
        alert_obj.accept()

    def customer_summary(self):
        self.go_to_customer()

        # Click Summary
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div/div/div/div[3]/table/tbody/tr/td[14]/a').click()

        # Customer
        sleep(self.wait_time)
        print('Customer Total:', self.driver.find_element_by_xpath('/html/body/div/div/div/table[1]/tbody/tr/td').text)

        # Services Info
        sleep(self.wait_time)
        sleep(self.wait_time)
        print('Services Total:', self.driver.find_element_by_xpath('/html/body/div/div/div/table[2]/tbody/tr/td').text)

        # Product Info
        sleep(self.wait_time)
        print('Product Total:', self.driver.find_element_by_xpath('/html/body/div/div/div/table[3]/tbody/tr/td').text)

    def service_add(self):
        self.go_to_services()

        # Click add service
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div/div/div/div[3]/div/a/span').click()

        # Customer Name
        sleep(self.wait_time)
        select = Select(self.driver.find_element_by_xpath('/html/body/div/div/div/form/div[1]/div/select'))
        select.select_by_index(1)

        # Service Category
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div/div/div/form/div[2]/div/input').send_keys('Food and Beverage')

        # Description
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div/div/div/form/div[3]/div/textarea').send_keys('20 Breakfast Sandwiches and Coffee')

        # Location
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div/div/div/form/div[4]/div/input').send_keys('PKI')

        # Set up time
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div/div/div/form/div[5]/div/input[1]').clear()
        self.driver.find_element_by_xpath('/html/body/div/div/div/form/div[5]/div/input[1]').send_keys('2020-04-15 8:00:00')

        # Clean up time
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div/div/div/form/div[6]/div/input[1]').clear()
        self.driver.find_element_by_xpath('/html/body/div/div/div/form/div[6]/div/input[1]').send_keys('2020-04-15 12:00:00')

        # Charge
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div/div/div/form/div[7]/div/input').send_keys('100')

        # Save
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div/div/div/form/button').click()

    def service_edit(self):
        # Go to service list
        self.go_to_services()

        # Click edit
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div/div/div/div[3]/table/tbody/tr/td[8]/a').click()

        # Edit setup and clean up time
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div/div/div/form/p[5]/input[1]').clear()
        self.driver.find_element_by_xpath('/html/body/div/div/div/form/p[5]/input[1]').send_keys('2020-04-15 7:00:00')
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div/div/div/form/p[6]/input[1]').clear()
        self.driver.find_element_by_xpath('/html/body/div/div/div/form/p[6]/input[1]').send_keys('2020-04-15 11:00:00')

        # Save
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div/div/div/form/button').click()

    def service_delete(self):
        self.go_to_services()

        # Click delete
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div/div/div/div[3]/table/tbody/tr/td[9]/a').click()

        # Confirm
        alert_obj = self.driver.switch_to.alert
        alert_obj.accept()


    def product_add(self):
        self.go_to_products()

        # Click add
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div/div/div/div[3]/div/a/span').click()

        # Customer Name
        sleep(self.wait_time)
        select = Select(self.driver.find_element_by_xpath('/html/body/div/div/div/form/div[1]/div/select'))
        select.select_by_index(1)

        # Product
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div/div/div/form/div[2]/div/input').send_keys('Breakfast Sandwiches')

        # Description
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div/div/div/form/div[3]/div/textarea').send_keys('Sausage/Bacon breakfast sandwiches\n'
                                                                                                       'includes meet, egg, and cheese on an '
                                                                                                       'english muffin')

        # Quantity
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div/div/div/form/div[4]/div/input').send_keys('20')

        # Pickup time
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div/div/div/form/div[5]/div/input[1]').clear()
        self.driver.find_element_by_xpath('/html/body/div/div/div/form/div[5]/div/input[1]').send_keys('2020-04-15 07:30:00')

        # Charge
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div/div/div/form/div[6]/div/input').send_keys('100')

        # Save
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div/div/div/form/button').click()

    def product_edit(self):
        self.go_to_products()

        # Click Edit
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div/div/div/div[3]/table/tbody/tr/td[7]/a').click()

        # Edit pick up time
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div/div/div/form/p[5]/input[1]').clear()
        self.driver.find_element_by_xpath('/html/body/div/div/div/form/p[5]/input[1]').send_keys('2020-04-15 06:30:00')

        # Save
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div/div/div/form/button').click()

    def product_delete(self):
        self.go_to_products()

        # Click delete
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div/div/div/div[3]/table/tbody/tr/td[8]/a').click()

        # Confirm
        alert_obj = self.driver.switch_to.alert
        alert_obj.accept()

if __name__ == '__main__':
    food_services = FoodServiceDriver('markcoldanghise', '#EDCcde3', sleep=1)
    food_services.login()

    food_services.customer_add_admin()
    food_services.customer_edit()

    food_services.service_add()
    food_services.service_edit()

    food_services.product_add()
    food_services.product_edit()

    food_services.customer_summary()

    food_services.service_delete()
    food_services.product_delete()
    food_services.customer_delete()


    food_services.clean_up()


