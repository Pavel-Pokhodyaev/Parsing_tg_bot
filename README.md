En/Ru
###########################################################################
Installation and Running of Selenium
###########################################################################

Download Python
https://python-scripts.com/install-python-windows
Make sure to check the option "Add Python X.Y to PATH" during installation.

Install Selenium
https://habr.com/ru/articles/248559/
Not sure if Java needs to be installed.
No need to download Selenium IDE and Selenium Server.

###########################################################################
Sending Reports to Telegram Channel
###########################################################################

Download requests

pip install requests

Create your bot using https://t.me/BotFather

Launch the bot on your Telegram account.

Visit the link, where 'token' is your bot's token:

'https://api.telegram.org/bot{token}/getUpdates'
Or send the command "/sendMyChatID" to the bot.

Find the chat ID between the bot and your account ("chat":{"id":XXXXXXXXXX}).

Visit the link, substituting 'token', 'chat_id', and 'message':

https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}
Test the automated test in conversation with the bot. If the test is ready, configure sending reports to "lum_autotest".

Add the bot to the chat.

Visit the link, substituting 'token', 'chat_id' of "lum_autotest" (791695629), and 'message':

https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}'
Useful Links:

https://www.selenium.dev/documentation/
https://python-scripts.com/install-python-windows
https://habr.com/ru/articles/248559/
https://habr.com/ru/companies/otus/articles/596071/
https://ru.stackoverflow.com/questions/1095744/%D0%BD%D0%B5-%D0%BC%D0%BE%D0%B3%D1%83-%D0%BF%D1%80%D0%B8%D1%81%D0%B2%D0%BE%D0%B8%D1%82%D1%8C-%D1%82%D0%B5%D0%BA%D1%81%D1%82-%D0%B8%D0%B7-html-%D0%B2-%D0%BF%D0%B5%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D0%BD%D1%83%D1%8E-selenium-python



###########################################################################
Установка и запуск selenium
###########################################################################
1. Скачиваем Pythone
https://python-scripts.com/install-python-windows
Обязательно установите флажок на «Add Python X.Y to PATH» 

2. Устанавливаем Selenium
https://habr.com/ru/articles/248559/
Хз, надо ли устанавливать java
Selenium ide и Selenium server скачивать не надо


Ru
###########################################################################
Отправка отчета в тг канал
###########################################################################
1. скачиваем requests 
pip install requests 

2. Создаем своего бота через https://t.me/BotFather

3. Запускаем бота в своем тг

4. Переходим по ссылке где, токен - токен бота
'https://api.telegram.org/bot{token}/getUpdates'
или пишем боту /sendMyChatID

5. Ищем id чата между ботом и своим аккаунтом ("chat":{"id":XXXXXXXXXX)

6. Переходим по ссылке, подставляя токен, id чата и сообщение
https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}

7. Тестим автотест в переписке с ботом, если автотест готов, настраиваем отправку отчетов в lum_autotest

8. Добавляем бота в чат

9. Переходим по ссылке, подставляя токен, id чата lum_autotest (791695629) и сообщение
https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}'


Полезные ссылки:
https://www.selenium.dev/documentation/
https://python-scripts.com/install-python-windows
https://habr.com/ru/articles/248559/
https://habr.com/ru/companies/otus/articles/596071/
https://ru.stackoverflow.com/questions/1095744/%D0%BD%D0%B5-%D0%BC%D0%BE%D0%B3%D1%83-%D0%BF%D1%80%D0%B8%D1%81%D0%B2%D0%BE%D0%B8%D1%82%D1%8C-%D1%82%D0%B5%D0%BA%D1%81%D1%82-%D0%B8%D0%B7-html-%D0%B2-%D0%BF%D0%B5%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D0%BD%D1%83%D1%8E-selenium-python