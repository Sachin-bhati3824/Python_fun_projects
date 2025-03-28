import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime
from datetime import date 



name = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  # Use `-` instead of `:`
print(name)
file = open(name+'.txt','a')


book = [] 
book_info = [] 
book_info= [] 
while True :
    book_name = str(input())
    book_name_list = book_name.split('by')
    if len(book_name_list) ==1 :
        book_author = []
        book_name_list.append(book_author)
    if book_name == 'end':
        break
    book_info.append(book_name_list)
print(book_info)
for s in range(len(book_info)):
# book info contains two list , first one is the name of the book and the next one is the name of the author , now go on , and only deal with the book info 
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    path = "C:/Users/ASUS/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"
    service =  Service(path)
    url = 'https://www.goodreads.com' 
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(url)
    element = driver.find_element(By.CSS_SELECTOR,"input[name='q'], input[type='text'], input[placeholder='Search books']")
    element.send_keys(book_info[s][0])
    element.send_keys(Keys.ENTER)

    #okay so remember , wehenever we have to click and it is not finding the element use this , first ec.presenceof element located then use the xpath or the css selector  , and in the last just use the click method of the js metthod not the simple one 
    close_button = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "body > div:nth-child(4) div div.modal__close > button")))
    driver.execute_script("arguments[0].click();", close_button)
    book_tag = driver.find_element(By.CSS_SELECTOR, "#bodycontainer table tbody tr:first-child td:nth-child(2) a span")
    book_tag.click()
    #these data-test id are made to easily scrap the data from the web , so try to use it , but don't use the data-raectid because it is dynamicaly generated and will be different every time it is loaded 

    author_1  = driver.find_element(By.CSS_SELECTOR,'[data-testid*=name]')
    book_1   = driver.find_element(By.CSS_SELECTOR,'[data-testid*=bookTitle]')


    author_1_i = author_1.text 
    book_1_i = book_1.text
    book_info[s][0] = book_1_i
    if author_1_i == book_info[s][1]:
        pass
    else:
        book_info[s][1] = author_1_i 
    book_description = driver.find_element(By.CSS_SELECTOR,'[data-testid*=contentContainer]')
    info = book_description.text
    # genres_list_1 = driver.find_element(By.CSS_SELECTOR,'[aria-label*="Show all items in the list"]')
    # genres_list_1.click()
    try:
    # Wait for the "More" button and click it
        genres_list_1 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label*="Show all items in the list"]'))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", genres_list_1)
        time.sleep(1)  # Small delay for stability
        driver.execute_script("arguments[0].click();", genres_list_1)

        # Wait for genres to be visible
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid*=genresList]'))
        )

    except Exception as e:
        print(f"Error clicking 'More' button: {e}")

    genres_list = driver.find_elements(By.CSS_SELECTOR,'[data-testid*=genresList]')
    lista = []
    for m in range(len(genres_list)):
        a = genres_list[m].text 
        lista.append(a)
    listb = lista[0].split("\n")
    print(listb)
    listb.pop()
    listb.pop(0)
    for i in range(len(listb)):
        if listb[i] == "Audiobook":
            listb.pop(i)
            break
    book_info.append(listb)
    
    driver.quit()
    file.write("\n"+ str(book_info[s][0]))
    file.write("\n"+ str(book_info[s][1]))


    file.write("\n"+ 'Genre'+'\t')

    for j in range(len(listb)):
        file.write(str(listb[j]))
        file.write('\t')

    file.write("\n"+ info)
    for i in range(9):
        file.write('\n')
    print(info)
    

file.close()

