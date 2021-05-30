import sys
import unittest
import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By


class TestReto1(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.close()

    def test_reto1(self):
        driver = self.driver
        driver.get("http://www.rpachallenge.com/")
        # codigo here!
        start = driver.find_element_by_xpath("//button[contains(text(),'Start')]")
        submit = driver.find_element_by_xpath("//body/app-root[1]/div[2]/app-rpa1[1]/div[1]/div[2]/form[1]/input[1]")

        data = [
        {
            "First Name": "John",
            "Last Name ": "Smith",
            "Company Name": "IT Solutions",
            "Role in Company": "Analyst",
            "Address": "98 North Road",
            "Email": "jsmith@itsolutions.co.uk",
            "Phone Number": "40716543298"
        },
        {
            "First Name": "Jane",
            "Last Name ": "Dorsey",
            "Company Name": "MediCare",
            "Role in Company": "Medical Engineer",
            "Address": "11 Crown Street",
            "Email": "jdorsey@mc.com",
            "Phone Number": "40791345621"
        },
        {
            "First Name": "Albert",
            "Last Name ": "Kipling",
            "Company Name": "Waterfront",
            "Role in Company": "Accountant",
            "Address": "22 Guild Street",
            "Email": "kipling@waterfront.com",
            "Phone Number": "40735416854"
        },
        {
            "First Name": "Michael",
            "Last Name ": "Robertson",
            "Company Name": "MediCare",
            "Role in Company": "IT Specialist",
            "Address": "17 Farburn Terrace",
            "Email": "mrobertson@mc.com",
            "Phone Number": "40733652145"
        },
        {
            "First Name": "Doug",
            "Last Name ": "Derrick",
            "Company Name": "Timepath Inc.",
            "Role in Company": "Analyst",
            "Address": "99 Shire Oak Road",
            "Email": "dderrick@timepath.co.uk",
            "Phone Number": "40799885412"
        },
        {
            "First Name": "Jessie",
            "Last Name ": "Marlowe",
            "Company Name": "Aperture Inc.",
            "Role in Company": "Scientist",
            "Address": "27 Cheshire Street",
            "Email": "jmarlowe@aperture.us",
            "Phone Number": "40733154268"
        },
        {
            "First Name": "Stan",
            "Last Name ": "Hamm",
            "Company Name": "Sugarwell",
            "Role in Company": "Advisor",
            "Address": "10 Dam Road",
            "Email": "shamm@sugarwell.org",
            "Phone Number": "40712462257"
        },
        {
            "First Name": "Michelle",
            "Last Name ": "Norton",
            "Company Name": "Aperture Inc.",
            "Role in Company": "Scientist",
            "Address": "13 White Rabbit Street",
            "Email": "mnorton@aperture.us",
            "Phone Number": "40731254562"
        },
        {
            "First Name": "Stacy",
            "Last Name ": "Shelby",
            "Company Name": "TechDev",
            "Role in Company": "HR Manager",
            "Address": "19 Pineapple Boulevard",
            "Email": "sshelby@techdev.com",
            "Phone Number": "40741785214"
        },
        {
            "First Name": "Lara",
            "Last Name ": "Palmer",
            "Company Name": "Timepath Inc.",
            "Role in Company": "Programmer",
            "Address": "87 Orange Street",
            "Email": "lpalmer@timepath.co.uk",
            "Phone Number": "40731653845"
        }
    ]

        start.click()
        for x in range(0,10):
            first_name = driver.find_element_by_xpath("//label[contains(text(),'First Name')]/following-sibling::input")
            email = driver.find_element_by_xpath("//label[contains(text(),'Email')]/following-sibling::input")
            phone = driver.find_element_by_xpath("//label[contains(text(),'Phone Number')]/following-sibling::input")
            company = driver.find_element_by_xpath("//label[contains(text(),'Company Name')]/following-sibling::input")
            role = driver.find_element_by_xpath("//label[contains(text(),'Role in Company')]/following-sibling::input")
            last_name = driver.find_element_by_xpath("//label[contains(text(),'Last Name')]/following-sibling::input")
            address = driver.find_element_by_xpath("//label[contains(text(),'Address')]/following-sibling::input")

            first_name.send_keys(data[x]["First Name"])
            email.send_keys(data[x]["Email"])
            phone.send_keys(data[x]["Phone Number"])
            company.send_keys(data[x]["Company Name"])
            role.send_keys(data[x]["Role in Company"])
            last_name.send_keys(data[x]["Last Name "])
            address.send_keys(data[x]["Address"])
            #time.sleep(8)
            submit.click()

        time.sleep(2)

        message = driver.find_element_by_class_name("message2")
        res = re.findall('\d*%', message.text)
        print(message.text)
        self.assertGreater(int(str(res[0]).strip('%')), 90)


if __name__ == '__main__':
    unittest.main()
