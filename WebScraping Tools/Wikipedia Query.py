import requests
from bs4 import BeautifulSoup
import os

while True:
	query = str(input("Search word: "))
	if query == 'xx':
		break
	elif query == 'cls':
		os.system('CLS')
		continue
	URL = "https://en.wikipedia.org/wiki/"+query
	r = requests.get(URL)
	soup = BeautifulSoup(r.content, 'html.parser')

	para = soup.find_all('p')
	i=0
	for i in range(len(para)):
		if para[i].text and para[i].text.strip():
			print('\nDEFINITION OF '+query.upper()+'\n\n')
			print(para[i].text+'\n')
			break
		else:
			continue
			
	
	