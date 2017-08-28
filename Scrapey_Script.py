import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

smoke = requests.get('http://victoryautowreckers.com/newarrivals.aspx').text

crystal = bs(smoke, 'lxml')

with open('c://users//matt//desktop//pythonprojects//ebay//web_list.txt', 'w') as jesus:
	gerrymander = ''
	for i in range(1, len(crystal.table.table.find_all('tr'))):
		for l in range(2,7):
			if i == len(crystal.table.table.find_all('tr')) -1:
				if l == 6:
					gerrymander += str(crystal.table.table.find_all('tr')[i].find_all('td')[l].text).replace(' ','$')
				else:
					gerrymander += str(crystal.table.table.find_all('tr')[i].find_all('td')[l].text).replace(' ','$') + ' '
			else:
				if l == 6:
					gerrymander += str(crystal.table.table.find_all('tr')[i].find_all('td')[l].text).replace(' ','$') + '*'
				else:
					gerrymander += str(crystal.table.table.find_all('tr')[i].find_all('td')[l].text).replace(' ','$') + ' '
	charliemander = gerrymander.split('*')
	def crystaline(methamphetamine):
		tuplist = []
		for i in range(len(methamphetamine)):
			singlst = methamphetamine[i].split()
			singting = methamphetamine[i].split()[2].replace('$',' ')
			singlst[2] = singting
			nwdx = tuple(singlst)
			tuplist.append(nwdx)
		return tuplist
	everyday = crystaline(charliemander)	 
	junkdata = pd.DataFrame.from_records(data=everyday, columns=['Year','Make','Model','Row','Yard Date'])
	junkdata['Yard Date'] = pd.to_datetime(junkdata['Yard Date'])
	junkdata['Year'] = junkdata['Year'].astype(dtype=int)
	new_data = pd.DataFrame(junkdata[((junkdata['Yard Date'] == pd.datetime.today().date()) | (junkdata['Yard Date'] == pd.datetime.today().date() - pd.Timedelta(1, unit='d')) | (junkdata['Yard Date'] == pd.datetime.today().date() - pd.Timedelta(2, unit='d'))) & (junkdata['Year'] >= 1998)], index=None)
	#new_data = pd.DataFrame(junkdata[((junkdata['Yard Date'] == pd.to_datetime('2017-08-16')) | (junkdata['Yard Date'] == pd.to_datetime('2017-08-15'))) & (junkdata['Year'] >= 1998)], index=None)
	year = new_data.Year.astype(dtype=str).str[2:4]
	model = new_data.Model.str.lower()
	to_txt = pd.DataFrame({1:year, 2:model}, index=None)	
	new_data.to_csv('c://users//matt//desktop//pythonprojects//ebay//web_list.txt', sep=' ', index=False, header=False, mode='w')
	to_txt.to_csv('c://users//matt//desktop//pythonprojects//ebay//search_words.txt', sep=' ', index=False, header=False, mode='w')
