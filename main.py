from multiprocessing.connection import wait
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome('/Applications/chromedriver')

driver.get('https://www.linkedin.com')
sleep(2)

username = driver.find_element(By.ID, 'session_key')
password = driver.find_element(By.ID, 'session_password')
button = driver.find_element(By.CLASS_NAME, 'sign-in-form__submit-button')

username.send_keys('drobdilamenace@gmail.com')
password.send_keys('ynx9gry3fpb6qae_NVR')
button.click()
sleep(2)

# button = driver.find_element(By.CLASS_NAME, 'secondary-action')
# button.click()
# sleep(5)

driver.get('https://www.linkedin.com/in/aymerickmichelet')
sleep(2)


# main
main = driver.find_element(By.TAG_NAME, 'main')

# sections
sections = main.find_elements(By.TAG_NAME, 'section')

# header_section
header = sections[0]
header_imgs = header.find_elements(By.TAG_NAME, 'img')
header_activity = header.find_elements(By.TAG_NAME, 'h2')

# background picture
background_picture = header_imgs[0].get_property('src')

# profile picture
profile_picture = header_imgs[1].get_property('src')

# job picture
job_picture = header_imgs[2].get_property('src')

# formation picture
formation_picture = header_imgs[3].get_property('src')

# name
name = header.find_element(By.TAG_NAME, 'h1').text

# profile_title
profile_title = header.find_element(By.XPATH, 'div[2]/div[2]/div[1]/div[2]').text

# job name
job_name = header_activity[0].text

# formation name
formation_name = header_activity[1].text

# info
info = sections[1]

# description
description = info.find_element(By.XPATH, 'div[3]')

# Formation actuel
# currently_formation = driver.find_element_by_id(By.ID, '#education')
# currently_formation_logo = currently_formation.find_element_by_class_name(By.CLASS_NAME, 'ember-view pv-text-details__right-panel-item-text-image EntityPhoto-square-1')
# currently_formation_name = currently_formation.find_element_by_class_name(By.CLASS_NAME, 'pv-text-details__right-panel-item-text hoverable-link-text break-words text-body-small inline')

# Description (info)
# info = driver.find_element_by_xpath(By.XPATH, '//*[@id="ember95"]/div[3]/div/div/div/span[1]')

# Expérience pro
# Formation
# Compétence

# print(currently_job_name.text)

print(background_picture)
print(profile_picture)
print(job_picture)
print(formation_picture)
print(name)
print(profile_title)
print(job_name)
print(formation_name)

driver.close()