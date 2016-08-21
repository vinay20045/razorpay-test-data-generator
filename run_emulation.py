##
# This is as simple as a license can get. Please read
# carefully and understand before using.
#
# I wrote this script because I needed it. I am opening
# up the source code to the world because I believe in
# the power of royalty free knowledge and shared ideas.
#
# 1. This piece of code comes to you at no cost and no
#    obligations.
# 2. You get NO WARRANTIES OR GUARANTEES OR PROMISES of
#    any kind.
# 3. If you are using this script you understand the risks
#    completely.
# 4. I request and insist that you retain this notice without
#    modification, but if you can't... I understand.
#
# --
# Vinay Kumar NP
# vinay@askvinay.com
# www.askVinay.com
##

import sys
import os
import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def write(ele, value):
    ele.clear()
    ele.send_keys(str(value))

    return None

def get_details():
    customer_emails = ['Pravuil@gmail.com','Ridwan@gmail.com','Castiel@gmail.com','Appolyon@gmail.com','Kabshiel@gmail.com','Kezef@gmail.com','Ambriel@gmail.com','Vohamanah@gmail.com','Jehoel@gmail.com','Cassiel@gmail.com','Barbiel@gmail.com','Dardariel@gmail.com','Madan@gmail.com','Ahiah@gmail.com','Rahatiel@gmail.com','Halaliel@gmail.com','Duma@gmail.com','Isda@gmail.com','Nemamiah@gmail.com','Jophiel@gmail.com','Yofiel@gmail.com','Haniel@gmail.com','Salathiel@gmail.com','Usiel@gmail.com','Ophiel@gmail.com','Yahoel@gmail.com','Anahel@gmail.com','Peliel@gmail.com','Gabriel@gmail.com','Aarin@gmail.com']

    customer_numbers = [7438412299,8669280018,9245214780,8454076190,9025447065,8895663384,9748602501,9053510467,9952118825,8740392163,8167477437,7131953730,9327892222,9187498968,9155154670,7720861616,9261017562,8917332737,7459307761,7437489937,8175739894,9572426845,9581304142,7630182084,8456989468,8115504447,7070752684,8366125503,9877747637,9333648008]

    i = random.randint(0,29)
    return {
        'number': customer_numbers[i],
        'email': customer_emails[i]
    }


if __name__ == "__main__":
    #mandatory items
    html_file = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'payment_page.html'
    )
    razorpay_key = sys.argv[1]

    #optional items
    try:
        no_of_records = int(sys.argv[2])
    except:
        no_of_records = 1
    try:
        min_amount = int(sys.argv[3])
        max_amount = int(sys.argv[4])
    except:
        min_amount = 1000
        max_amount = 9999

    #open page
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)

    driver.get('file://' + html_file)

    #write the info
    write(
        driver.find_element_by_id('rzp_key_id'),
        razorpay_key
    )
    write(
        driver.find_element_by_id('no_of_records'),
        no_of_records
    )
    write(
        driver.find_element_by_id('amt_range_start'),
        min_amount
    )
    write(
        driver.find_element_by_id('amt_range_end'),
        max_amount
    )

    #loop to generate as many records necessary
    i = 1
    while i <= no_of_records:
        #print 'set amount'
        write(
            driver.find_element_by_id('amount'),
            random.randint(min_amount,max_amount) * 100
        )

        #print 'click button'
        ele = driver.find_element_by_id('generate')
        ele.click()

        #print 'switch to payment frame'
        payment_frame = driver.find_element_by_tag_name('iframe')
        driver.switch_to_frame(payment_frame)
        driver.implicitly_wait(10)
        
        #print 'fill in customer details'
        customer = get_details()
        write(
            driver.find_element_by_id('contact'),
            customer['number']
        )
        write(
            driver.find_element_by_id('email'),
            customer['email']
        )

        #print 'select netbanking - as it seems to be the easiest to continue with'
        ele = driver.find_element_by_xpath("//div[@tab='netbanking']")
        ele.click()

        #print 'select hdfc bank'
        ele = driver.find_element_by_xpath("//label[@for='bank-radio-HDFC']")
        ele.click()

        #print 'click pay'
        ele = driver.find_element_by_xpath("//button[@id='footer']")
        ele.click()

        #print 'switch to the last of the windows'
        x = 1
        while x < 5:
            try:
                driver.switch_to_window(driver.window_handles[1])
                driver.implicitly_wait(10)
                break
            except:
                #print 'try clicking pay again'
                ele = driver.find_element_by_xpath("//button[@id='footer']")
                ele.click()
            x = x + 1

        #print 'click success'
        ele = driver.find_element_by_xpath("//input[@data-value='S']")
        ele.click()

        #print 'switch back to the first of windows'
        driver.switch_to_window(driver.window_handles[0])
        driver.implicitly_wait(10)

        i = i + 1
        time.sleep(1)
