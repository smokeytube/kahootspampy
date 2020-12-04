import pyautogui
import time
from selenium import webdriver
from tkinter import *

win = Tk()
win.title("Kahoot Botter")
win.geometry("350x260")
var1 = IntVar()
def ratcheck():
    print (int(var1.get()))
Checkbutton(win, text="School appropriate names", variable=var1, command=ratcheck).place(x=150, y=100)

var2 = IntVar()
def ratcheck2():
    print (int(var2.get()))
Checkbutton(win, text="Friendly Nick Generator", variable=var2, command=ratcheck2).place(x=150, y=140)

heading = Label(win, text="Input into the feilds")
Label(win, text="Made by Zach").place(x=200, y=10)
Label(win, text="Bot your teacher!").place(x=200, y=30)
Label(win, text="Enter game code:").place(x=10, y=10)
code22 = IntVar()
Entry(win, textvariable=code22, width=25, bg="gray").place(x=10, y=30)
def code112():
    print (int(code22.get()))
Button(win, text="Submit", width=5, height=1, bg="gray", command=code112).place(x=10, y=50)
Label(win, text="Enter your chrome version").place(x=10, y=160)
Label(win, text="85, 86, or 87").place(x=10, y=180)
chromever = IntVar()
Entry(win, textvariable=chromever, width=5, bg="gray").place(x=10, y=200)
def chromeversion():
    print (int(chromever.get()))
Button(win, text="Submit", width=5, height=1, bg="gray", command=chromeversion).place(x=10, y=230)
Label(win, text="Bots:").place(x=10, y=90)
botnum = IntVar()
Entry(win, textvariable=botnum, width=2, bg="gray").place(x=50, y=92)
def bot():
    print (int(botnum.get()))
Button(win, text="Submit", width=5, height=1, bg="gray", command=bot).place(x=10, y=120)
Button(win, text="Start", bg="red", command=win.quit).place(x=240, y=220)
win.mainloop()
code22 = int(code22.get())
botnum = int(botnum.get())
chromever = int(chromever.get())
appropriatenames = int(var1.get())
nickgen = int(var2.get())


if chromever == 85:
    chromedriverdir = 'chromedriver85.exe'
if chromever == 86:
    chromedriverdir = 'chromedriver86.exe'
if chromever == 87:
    chromedriverdir = 'chromedriver87.exe'
else:
    print ("Not a valid version. Using chrome 86 as deafault.")
chromedriverdir = 'chromedriver86.exe'
# chromedriverdir = 'C:\webdrivers\chromedriver.exe'
driver = webdriver.Chrome(chromedriverdir)
driver.implicitly_wait(5)
driver.get('https://kahoot.it/')
time.sleep(2)
tab = 1
nume = 9
if nickgen == 1:
    while botnum > 0:
        while tab != nume:
            time.sleep(0.5)
            code_input = driver.find_element_by_xpath('//*[@id="game-input"]')
            code_input.click()
            code_input.send_keys(code22)
            submit_code = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div/main/div/form/button')
            submit_code.click()
            spin = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[2]/div/div[2]/button')
            spin.click()
            go = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[2]/div/div[2]/button[2]')
            go.click()
            time.sleep(0.5)
            driver.execute_script("window.open('https://kahoot.it')")
            driver.switch_to.window(driver.window_handles[tab])
            botnum = botnum - 1
            tab = tab + 1
            driver.delete_cookie
        time.sleep(60)
        nume = nume + 7
else:
    if appropriatenames == 0:
        namelist = open('boynames.txt', encoding="utf8")
    elif appropriatenames == 1:
        namelist = open('namesappropriate.txt', encoding="utf8")
    else:
        namelist = ("How tf did you get here??")
        print (namelist)
        time.sleep(9223372036854775807)
    while botnum > 0:
        while tab != nume:
            name = namelist.readline()
            time.sleep(0.5)
            code_input = driver.find_element_by_xpath('//*[@id="game-input"]')
            code_input.click()
            code_input.send_keys(code22)
            submit_code = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div/main/div/form/button')
            submit_code.click()
            name_input = driver.find_element_by_xpath('//*[@id="nickname"]')
            name_input.click()
            pyautogui.typewrite(name)
            submit_name = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div/main/div/form/button')
            time.sleep(0.5)
            driver.execute_script("window.open('https://kahoot.it')")
            driver.switch_to.window(driver.window_handles[tab])
            botnum = botnum - 1
            tab = tab + 1
            driver.delete_cookie
        time.sleep(60)
        nume = nume + 7