import requests
from bs4 import BeautifulSoup
import smtplib
import lxml

my_email = 'krahs123@mail.ru'
my_password = 'gpkbmZY8t4AFXjmAv7sb'

URL = "https://www.amazon.com/dp/B08GM5PSKP/ref=sbl_dpx_kitchen-electric-cookware_B08GC6PL3D_0"

header = {
"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
"Accept-Language":'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7'
}

response = requests.get(URL,headers=header)

soup = BeautifulSoup(response.text, 'lxml')

price = float(soup.select('.a-offscreen')[0].text.split('$')[1])


if int(price) <= 100:
    connection = smtplib.SMTP('smtp.mail.ru')
    connection.starttls()
    connection.login(my_email, my_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="krahs123@gmail.com",
        msg='Опа, скидочка. Вкуснооо'.encode('utf-8').strip()
    )

