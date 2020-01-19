from selenium import webdriver
import time
from bs4 import BeautifulSoup
import random
buy = False
error = None

wordlist = {}
MPQ = {10:1, 100:2, 1000:3, 10000:4, 75000:5, 300000:6, 1000000:7, 10000000:8, 100000000:9}
SB = {15:1, 150:2, 1500:3, 15000:4, 115000:5, 450000:6, 1500000:7, 15000000:8, 200000000:9}
M = {50:1, 300:2, 2000:3, 12000:4, 85000:5, 700000:6, 6500000:7, 65000000:8, 1000000000:9}

driver = webdriver.Chrome(executable_path=r'C:\Users\lucas\Documents\chromedriver_win32\chromedriver.exe')

def super_get(url):
    driver.get(url)
    driver.execute_script("window.onbeforeunload = function() {};")


while True:
	try:
		print("hi")
		super_get("https://chatt--spacedino.repl.co/")
		inputt = driver.find_element_by_id("nameArea")
		inputt.send_keys("Lukaja21 Bot")
		inputt.send_keys(u'\ue007')
		time.sleep(3)
		if error != None:
			inputt = driver.find_element_by_id("messageArea")
			inputt.send_keys(error)
			inputt.send_keys(u'\ue007')
			error = None
		while True:
			time.sleep(10)
			html = BeautifulSoup(driver.find_element_by_tag_name('html').get_attribute('innerHTML'), "html.parser")
			if "!gimkit" in html.find_all("span", class_="messageContent")[-1].text:
				gimkitCode = html.find_all("span", class_="messageContent")[-1].text.split()[1]
				inputt = driver.find_element_by_id("messageArea")
				if len(gimkitCode) == 5:
					try:
						gimkitCode = str(int(gimkitCode))
						inputt.send_keys("Going to Gimkit game at code: " + gimkitCode)
						inputt.send_keys(u'\ue007')
					except:
						inputt.send_keys("Not a valid code")
						inputt.send_keys(u'\ue007')
				else:
					inputt.send_keys("Not a valid code")
					inputt.send_keys(u'\ue007')
				break
			elif "!stop" in html.find_all("span", class_="messageContent")[-1].text:
				sys.exit()
		
		super_get("https://gimkit.com/play")
		driver.execute_script(open("hello_world.js").read())
		driver.find_element_by_class_name("sc-cSHVUG").send_keys(gimkitCode)
		driver.find_element_by_class_name("sc-cSHVUG").send_keys(u'\ue007')
		time.sleep(3)
		driver.find_element_by_class_name("sc-cSHVUG").send_keys("lucas")
		driver.find_element_by_class_name("sc-cSHVUG").send_keys(u'\ue007')
		time.sleep(5)
		
		while True:
			#Question Page
			time.sleep(.5)
			html = BeautifulSoup(driver.find_element_by_tag_name('html').get_attribute('innerHTML'), "html.parser")
			if html.find("div", class_="sc-gzVnrw").text in wordlist:
				thingList = html.find_all("div", class_="sc-csuQGl")
				for thing in thingList:
					if thing.text == wordlist[html.find("div", class_="sc-gzVnrw").text]:
						number = thingList.index(thing)
				driver.find_elements_by_class_name("sc-csuQGl")[number].click()
				#Continue Page
				time.sleep(.5)
				balance = int(html.find("div", class_="sc-daURTG").text.replace("$", "").replace(",", ""))
				if balance + 1 > min(MPQ):
					category = 0
					buyList = MPQ
					buy = True
				elif balance + 1 > min(SB):
					category = 1
					buyList = SB
					buy = True
				elif balance + 1 > min(M):
					category = 2
					buyList = M
					buy = True
				if not buy:
					driver.find_elements_by_class_name("sc-htpNat")[1].click()
				else:
					driver.find_elements_by_class_name("sc-htpNat")[0].click()	
					time.sleep(.5)
					driver.find_elements_by_class_name("sc-cJSrbW")[category].click()
					time.sleep(.5)
					driver.find_elements_by_class_name("sc-eXEjpC")[buyList[min(buyList)]].click()
					driver.find_elements_by_class_name("sc-bwzfXH")[2].click()
					del buyList[min(buyList)]
					driver.find_element_by_class_name("sc-bdVaJa").click()
					buy = False
			else:
				choice = random.randint(0, 3)
				choiceThing = html.find_all("div", class_="sc-csuQGl")[choice].text
				driver.find_elements_by_class_name("sc-csuQGl")[choice].click()
				time.sleep(.5)
				html = BeautifulSoup(driver.find_element_by_tag_name('html').get_attribute('innerHTML'), "html.parser")
				if "Shop" not in html.find("div", class_="sc-htpNat").text:
					#Continue Page
					driver.find_element_by_class_name("sc-htpNat").click()
					#Learn Word Page
					time.sleep(.5)
					html = BeautifulSoup(driver.find_element_by_tag_name('html').get_attribute('innerHTML'), "html.parser")
					wordlist[html.find_all("div", class_="sc-bwzfXH")[0].text] = html.find_all("div", class_="sc-bwzfXH")[2].text
					driver.find_elements_by_class_name("sc-bwzfXH")[3].click()
				else:
					#Continue Page
					wordlist[html.find("div", class_="sc-exAgwC").text] = choice
					time.sleep(.5)
					print("Y")
					html = BeautifulSoup(driver.find_element_by_tag_name('html').get_attribute('innerHTML'), "html.parser")
					driver.find_elements_by_class_name("sc-htpNat")[1].click()
	except Exception as e:
		error = str(e)
		gimkitCode = None