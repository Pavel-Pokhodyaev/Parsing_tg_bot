import telebot
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
# Токен Telegram бота
TOKEN = '6380283448: ' #Insert Telegram Token
# Создаем экземпляр бота
bot = telebot.TeleBot(TOKEN)
options = webdriver.ChromeOptions()
options.add_argument('headless')  # Enabling/Disabling Visual
driver = webdriver.Chrome(options=options)
driver.get("https://d-dymok.ru/katalog/odnostennye-dymohody/")
tovar_elements = driver.find_elements(By.XPATH, '//*[@id="center_column"]/ul/li')
result_message = ""
for element in tovar_elements:
    name_tovar = element.find_element(By.XPATH, './div/div/div[3]/div/div[1]/div/span').text
    price_tovar = element.find_element(By.XPATH, './div/div/div[3]/div/div[1]/div/div/div[1]/div[1]/span').text
    result_message += f"{name_tovar}\n{price_tovar}\n\n"
driver.quit()
# Отправляем результат в телеграм
chat_id = '791695629'
bot.send_message(chat_id=chat_id, text=result_message)
