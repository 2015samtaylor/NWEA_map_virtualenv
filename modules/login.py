#!/usr/bin/env python
# coding: utf-8

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoSuchWindowException
import logging
import os
import zipfile
import time



 
def logIn(email, password, driver):
    driver.get('https://sso.mapnwea.org/auth/login')
    driver.maximize_window()
    windowSize = driver.get_window_size()


    try:
        ok_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "ok_button"))
        )
        ok_button.click()
        logging.info('Bypassing pop up on login page')
    except:
        logging.error('Unable to click ok button to clear pop up')


    try:
        login_email = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "login-email"))
        )
        login_email.send_keys(email)
    except:
        logging.error('Unable to send keys to email field')

    try:
        continue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test-id="continue-btn"]'))
        )

        continue_button.click()
    except:
        logging.error('Unable to hit continue button')

    
    try:
        password_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "password"))
        )
        password_input.send_keys(password)
    except:
        logging.error('Unable to send password')


    try:
        login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test-id="login-btn"]'))
        )
        login_button.click()
    except:
        logging.info('Unable to login')



def get_to_data_export(driver):
    #click on image
    dropdown = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@data-testid="MAP Growth MegaMenu"]'))
    )

    dropdown.click()

    driver.get('https://teach.mapnwea.org/report/map/comprehensiveDataFile.seam')


    download_link = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.download-link'))
    )

    download_link.click()

    time.sleep(10)



def create_directory(directory_path):
    # Convert the given path to an absolute path
    absolute_path = os.path.abspath(directory_path)

    if not os.path.exists(absolute_path):
        try:
            os.makedirs(absolute_path)
            print(f"Directory '{directory_path}' created successfully.")
            logging.info(f"Directory '{directory_path}' created successfully.")
        except OSError as e:
            print(f"Error creating directory '{directory_path}': {e}")
            logging.error(f"Error creating directory '{directory_path}': {e}")
    else:
        print(f"Directory '{directory_path}' already exists.")
        logging.info(f"Directory '{directory_path}' already exists.")



def unzip_xlsx_file(file_zips, files_dir):
    
   for zip_file in file_zips:

    # Create the full path for the zip file
    zip_path = os.path.join(files_dir, zip_file)

    # Extract the first file with a '.xlsx' extension from each zip_path
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        xlsx_file = [f for f in zip_ref.namelist() if f.endswith('.xlsx')]

        if xlsx_file:
            xlsx_file_to_extract = xlsx_file[0]
            zip_ref.extract(xlsx_file_to_extract, files_dir)
       
        else:
            print("No .xlsx file found in the zip archive.")
            logging.info('No .xlsx files found in the zip archive.')
            return(None)



def unzip_all_files(file_zips, files_dir):
    for zip_file in file_zips:
        try:
            zip_path = os.path.join(files_dir, zip_file)
            
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                # Extract all files in the zip archive
                zip_ref.extractall(files_dir)
                
                logging.info(f'Extracted all files from {zip_file}')
        except Exception as e:
            logging.error(f'Error extracting files from {zip_file}: {e}')




def unzip_files_in_same_dir():
    try:
        # Get the current working directory and the 'downloads' subdirectory
        files_dir = os.path.join(os.getcwd(), 'downloads')
        
        # List all files in the 'downloads' directory
        files_list = os.listdir(files_dir)
        
        # Filter out only files ending with .zip
        file_zips = [file for file in files_list if file.endswith('.zip')]
        
        if file_zips:
            unzip_all_files(file_zips, files_dir)
            logging.info(f'Unzipped all files into {files_dir}')
        else:
            print("No .zip files found in the 'downloads' directory.")
            logging.info('No .zip files found in the "downloads" directory.')
    except Exception as e:
        logging.error(f'Unable to unzip files due to error: {e}')



    

#Automated Login to Scrape Password
# import imaplib
# import email

# username = 'gdtestingcoordinator@greendot.org'

# imap_server = imaplib.IMAP4_SSL('imap-mail.outlook.com')

# # Login to the server
# imap_server.login(username, password)
