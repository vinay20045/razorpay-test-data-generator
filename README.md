razorpay-test-data-generator
============================
Generate payment data, as needed, using razorpay checkout script for testing purposes.

Usage
-----

```
python2.7 /path/to/run_emulation.py <razorpay_key_id> <no_of_records> <min_amount> <max_amount>
```
`razorpay_key_id` --> Required. Available in your razorpay dashboard   
`no_of_records` --> Optional. # of records to generate. Default is 1   
`min_amount` --> Optional. Minimum amount in paise. Default is 1000   
`max_amount` --> Optional. Maximum amount in paise. Default is 9999

Requirements
------------

Python2.7 | Firefox (latest version) | [Selenium Python Bindings][1]

Working and Limitations
-----------------------

1. This python script uses selenium webdriver to generate a set number of payment records for your Razorpay account using their checkout.js script.
2. It is recommended to be used (tested too) only in test mode.
3. It will make all payment entries using net banking and with random details for customer, but a customer's mobile number and email address will be consistent.
4. As the timestamp for payment event is generated at server, there is a limitation of not being able to obtain even distribution over time for the data generated.

Issues
------

Please raise an issue and/or send me an email at vinay@askvinay.com

[1] http://selenium-python.readthedocs.io/installation.html
