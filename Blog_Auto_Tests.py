from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep

class blog_driver:

    def __init__(self, un, pw, sleep=3):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.username = un
        self.password = pw
        self.wait_time = sleep

    def login(self):
        self.driver.get("http://127.0.0.1:8000/admin")
        sleep(self.wait_time)
        login_box = self.driver.find_element_by_xpath('/html/body/div/div[2]/div/form/div[1]/input')
        login_box.send_keys(self.username)
        sleep(self.wait_time)
        pass_box = self.driver.find_element_by_xpath('/html/body/div/div[2]/div/form/div[2]/input[1]')
        pass_box.send_keys(self.password)
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div/div[2]/div/form/div[3]/input').click()

    def add_blog_admin(self):
        sleep(self.wait_time)
        self.driver.get("http://127.0.0.1:8000/admin")
        self.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[2]/table/tbody/tr/td[1]/a').click()
        # Author
        sleep(self.wait_time)
        select = Select(self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/form/div/fieldset/div[1]/div/div/select'))
        select.select_by_visible_text(self.username)

        # Title
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/form/div/fieldset/div[2]/div/input').send_keys('Automation Test Title - Admin Panel')

        # Text
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/form/div/fieldset/div[3]/div/textarea').send_keys('Automation Test Text Input.\n'
                                                      'Test Test Test Test\n'
                                                      'Test Test Test Test.')

        # Create Date / Publish Date
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/form/div/fieldset/div[4]/div/p/span[1]/a[1]').click()
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/form/div/fieldset/div[4]/div/p/span[2]/a[1]').click()
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/form/div/fieldset/div[5]/div/p/span[1]/a[1]').click()
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/form/div/fieldset/div[5]/div/p/span[2]/a[1]').click()

        # Save
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/form/div/div/input[1]').click()

    def add_blog_home(self):
        sleep(self.wait_time)
        self.driver.get("http://127.0.0.1:8000")
        self.driver.find_element_by_xpath('/html/body/div[1]/a/span').click()

        # Title
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/form/p[1]/input').send_keys('Automation Test Title - Homepage')

        # Text
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/form/p[2]/textarea').send_keys(
            'Automation Test Text Input.\n'
            'Test Test Test Test\n'
            'Test Test Test Test.')

        # Save
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/form/button').click()


    def delete_all_posts_admin(self):
        self.driver.get('http://127.0.0.1:8000/admin')

        # Click Post table
        self.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[2]/table/tbody/tr/th/a').click()

        # Check all deletes
        self.driver.find_element_by_xpath('/html/body/div/div[3]/div/div/form/div[2]/table/thead/tr/th[1]/div[1]/span/input').click()

        # Select delete
        sleep(self.wait_time)
        select = Select(self.driver.find_element_by_xpath('/html/body/div/div[3]/div/div/form/div[1]/label/select'))
        select.select_by_index(1)

        # Confirm delete
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div/div[3]/div/div/form/div[1]/button').click()
        self.driver.find_element_by_xpath('/html/body/div/div[3]/form/div/input[last()]').click()

    def edit_first_post(self):
        sleep(self.wait_time)
        self.driver.get('http://127.0.0.1:8000/')

        # Click post
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/h2/a').click()

        # Click edit
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/a/span').click()

        # Edit Title
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/form/p[1]/input').send_keys(' - EDIT First')

        # Edit Text
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/form/p[2]/textarea').send_keys(' - EDIT First')

        # Save then return home
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/form/button').click()
        self.driver.find_element_by_xpath('/html/body/div[1]/h1/a').click()


    def edit_last_post(self):
        sleep(self.wait_time)
        self.driver.get('http://127.0.0.1:8000/')

        # Click post
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div[last()]/div/div/div[1]/h2/a').click()

        # Click edit
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/a/span').click()

        # Edit Title
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/form/p[1]/input').send_keys(' - EDIT Last')

        # Edit Text
        sleep(self.wait_time)
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/form/p[2]/textarea').send_keys(' - EDIT Last')

        # Save then return home
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/form/button').click()
        self.driver.find_element_by_xpath('/html/body/div[1]/h1/a').click()


    def clean_up(self):
        # Log out
        self.driver.get("http://127.0.0.1:8000/admin/")
        self.driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/a[3]').click()

        # Close chrome driver
        self.driver.close()

if __name__ == '__main__':
    blog = blog_driver('markcoldanghise', 'pass123', 1)
    blog.login()
    blog.add_blog_admin()
    blog.add_blog_home()

    blog.edit_first_post()
    blog.edit_last_post()
    blog.delete_all_posts_admin()
    blog.clean_up()


