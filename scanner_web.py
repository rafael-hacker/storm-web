from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import requests 
import socket
import sys
import os
import subprocess

user = os.getenv("USER")

print(f"hello {user} !")
site = input("which site do you want to scan ? it is not necessary to put https:// ")

nikto = subprocess.run(
    ["nikto", "-h", site, "-maxtime", "29"],
    capture_output=True,
    text=True,
)

nikto_output = nikto.stdout
print(nikto_output)
site2 = "https://" + site

with open("relatory.txt", "a" ) as f:
	f.write(nikto_output)
print("the relatory is save in 'relatory.txt'")

driver = webdriver.Chrome()
driver.get(site2)
sleep(9)

cookies = driver.get_cookies()
sleep(10)

print(f"the cookies found were {len(cookies)}  ")
print(cookies)
driver.quit()

to_chek = subprocess.run(["ping", "-c", "4",  site])
print(f"this site is {to_chek}")


response = requests.get(site2, timeout=14)

obtained_ip = socket.gethostbyname(site)
print(f"the ip and {obtained_ip} ")
with open("relatory2.txt", "w") as f:
	f.write(obtained_ip)


print("put yes or no ")
force_brute = input("Do you want to text default admin login? ").lower()

if force_brute == "yes":
	login = input("pass the url login part of the site: ")
	print("okay running")
	driver2 = webdriver.Firefox()
	driver2.get(login)
	
	login_site = driver2.find_element(By.NAME, "username")
	login_site.send_keys("admin")
	login_site.send_keys(Keys.RETURN)
	sleep(6)
	
	password = driver2.find_element(By.XPATH, "//input[@type='password']")
	password.send_keys("admin")
	password.send_keys(Keys.RETURN)
	sleep(6)
	driver2.quit()
	sleep(17)
else:
	print("okay")

fuzz = input("you want to fuzz the website ? yes or no ").lower()
print("fuzzing for https in BETA please not use port 443 in fuzzing !!")
while True:
	if fuzz == "yes":
		print("okay start fuzz ....")
		port = int(input("which port will use ? 'for https port 443' 'for http port 80' "))
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(2)
		s.connect((obtained_ip, port))
		if port == 80:
			payload_str = 'GET /' + ('#!#$' * 10000) + ' HTTP/1.1\r\n\r\n'
			payload = payload_str.encode()
			s.send(payload)
		if port == 443:
			print("port 443 is under development please select another option")

	elif fuzz == "no":
		print("okay !")
		break
	cont = input("Do you want to continue? yes or no.").lower()
	if cont == "no":
		break
		print("ok the loop has been stopped !")

nmap = input("Do you want to see the services running on the site with nmap? yes or no").lower()
if nmap == "yes":
	nmap_sv = subprocess.run(
    	["nmap", "-sV", site], 
    	capture_output=True,   
    	text=True              
) 

elif nmap == "no":
	print("okay")
else:
	print("error: your option is invalid ")
whois = input("Do you want to run whois to get public data? yes or no ?").lower()
if whois == yes:
	who = subprocess.run(
	"whois, site",
	capture_output=True,
	text=True
)

	result_who = who.stdout
	print(f"the whois return {result_who}")
elif whois == no:
	print("okay")
else:
	print("error: option invalid !")

detect_firewall = input("you want use Wafw00f for detect firewall yes or no ? ").lower()
if detect_firewall == "yes":
	wafw = subprocess.run(

	["wafw00f", site],
	capture_output=True,
	text=True
)
	print(f"the scan was a success and returned {wafw}")
elif detect_firewall == "no":
	print("okay")
else:
	print("error: option invalid")
sql = input("you want to make a basic text to test sql yes or no").lower()
if sql == "yes":
	parameters  = {'id': 5}
	print("running")
	response = requests.get(url_base, params=parametros)
	html_content = response.text 

	len_sql = len(html_content)
	print("the text return {len_sql}")
elif sql == "no":
	print("okay")
else:
	print("error option invalid")

DDoS = input("which site do you want to DDoS? yes or no").lower()

if DDoS == "yes":
	subprocess.run("./sh.sh")

elif nmap2 == "no":
	print("okay")
else:
	print("error: option invalid selecioned please restart the code")

while True:
	nmap2 = input("do you want to use more nmap parameters on the ip yes or no")
	print(f"the ip website is {obtained_ip}")

	if nmap2 == "yes":
		nmap3 = subprocess.run(
        ["./nmap.sh"],
        capture_output=True,
        text=True,
    )

		
		break
	elif nmap2 == "no":
		print("okay")
		break
	else:
		print("error: option ivalid ! ")
