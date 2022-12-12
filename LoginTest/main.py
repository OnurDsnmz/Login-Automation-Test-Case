from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#test otomasyonu
#test beklentiyi karşılıyormu?
#1.İstenileni yapıyormu?(pozitif test)-2.İstenmeyeni yapıyormu?(negatif test)
#CASE--İnternet Login sayfasına git : https://the-internet.herokuapp.com/login
#Kullanıcı adı gir
#şifre gir
#login düğmesine tıkla
#yanlış kullanıcı adı girince : Your username is invalid!
#yanlış şifre girince: Your password is invalid!
#ikiside doğru ise: Mesaj= You logged into a secure area!- link secure içerecek- sayfa başlığında secure area yazacak.

browser = webdriver.Chrome("./chromedriver.exe")
browser.get("https://the-internet.herokuapp.com/login")
browser.maximize_window()
# #adı:tomsmith , şifre : SuperSecretPassword!
# browser.find_element(By.ID,"username").send_keys("test")
# browser.find_element(By.ID,"password").send_keys("21235")
# time.sleep(2)
# browser.find_element(By.CSS_SELECTOR,"button.radius").click()
# time.sleep(2)
# ##yanlış kullanıcı adı girince : Your username is invalid!
# mesaj = browser.find_element(By.ID,"flash").text
# if "Your username is invalid!" in mesaj:
#     print("Ok, yanlis kullanici adi - site doğru calişiyor")
# else:
#     print("HATA: yanlis kullanici adi çalismiyor")
#
# #yanlış şifre girince: Your password is invalid!
#
# browser.find_element(By.ID,"username").send_keys("tomsmith")
# browser.find_element(By.ID,"password").send_keys("21235")
# time.sleep(2)
# browser.find_element(By.CSS_SELECTOR,"button.radius").click()
# time.sleep(2)
# mesaj2 = browser.find_element(By.ID,"flash").text
# if "Your password is invalid!" in mesaj2:
#     print("Ok, yanlis şifre - site doğru calişiyor")
# else:
#     print("HATA: yanlis şifre - site çalismiyor")
# time.sleep(2)
# #ikiside doğru ise mesaj:  You logged into a secure area! -link secure olacak- baslık secure area olacak
# browser.find_element(By.ID,"username").send_keys("tomsmith")
# browser.find_element(By.ID,"password").send_keys("SuperSecretPassword!")
# time.sleep(2)
# browser.find_element(By.CSS_SELECTOR,"button.radius").click()
# time.sleep(2)
# mesaj3=browser.find_element(By.ID,"flash").text
# if "You logged into a secure area!" in mesaj3:
#     print("Ok, başarılı giriş - site doğru calişiyor")
# else:
#     print("HATA: Başarısız giriş - site çalismiyor")
# link=browser.current_url
# if "secure" in link:
#     print("Başarılı link secure içeriyor.")
# else:
#     print("Başarısız link secure içermiyor.")
# mesaj4=browser.find_element(By.CSS_SELECTOR,"h2").text
# if mesaj4 in "Secure Area":
#     print("Sayfa başlığı doğru")
# else:
#     print("sayfa başlığı yanlış")
#
# time.sleep(3)
# #Logout düğmesine tıkla
# browser.find_element(By.XPATH,"//a[@class='button secondary radius']").click()
# #login sayfasına döndük doğrula
# if "login" in browser.current_url:
#     print("Login sayfasına döndük")
# else:
#     print("Login sayfası başarısız")

##fonksiyon yazarak REFACTORING yaptık.
def login(username,password):
    browser.get("https://the-internet.herokuapp.com/login")
    browser.find_element(By.ID, "username").send_keys(username)
    browser.find_element(By.ID, "password").send_keys(password)
    browser.find_element(By.CSS_SELECTOR, "button.radius").click()
    mesaj = browser.find_element(By.ID, "flash").text
    return mesaj

mesaj=login("test","23145")

if "Your username is invalid!" in mesaj:
    print("Ok, yanlis kullanici adi - site doğru calişiyor")
else:
    print("HATA: yanlis kullanici adi çalismiyor")

mesaj=login("tomsmith","65165")
if "Your password is invalid!" in mesaj:
    print("Ok, yanlis şifre - site doğru calişiyor")
else:
    print("HATA: yanlis şifre - site çalismiyor")

mesaj=login("tomsmith","SuperSecretPassword!")
if "You logged into a secure area!" in mesaj:
    print("Ok, başarılı giriş - site doğru calişiyor")
else:
    print("HATA: Başarısız giriş - site çalismiyor")

link=browser.current_url
if "secure" in link:
    print("Başarılı link secure içeriyor.")
else:
    print("Başarısız link secure içermiyor.")


browser.close()