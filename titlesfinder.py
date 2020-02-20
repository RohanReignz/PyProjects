import requests
from bs4 import BeautifulSoup
author = str(input("Enter writer's name: "))
author_r = author.replace(' ','-')
choice = str(input("Save it in a text file? "))
isYes = False
if choice == "yes" or choice == "YES" or choice == "Y" or choice =="y":
	file=open("BooksList.txt", "w")
	isYes = True
else:
	pass

URL = "https://www.bookseriesinorder.com/"+author_r
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html.parser')
titles = soup.find_all('td')
li= []
for i in range(0,len(titles)):
	if (titles[i].text) != ' Hardcover\xa0\xa0Paperback\xa0\xa0Kindle ':
		try:
			li.append(titles[i].text)
		except Exception as e:
			pass
		
for j in range(0,len(li), 2):
	try:
		print(li[j] + li[j+1])
		if isYes:
			file.write(li[j] + li[j+1]+'\n')
	except Exception as e:
		pass

input()

	