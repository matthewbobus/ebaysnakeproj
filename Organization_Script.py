import pandas as pd
from pandas import ExcelWriter

df = pd.read_csv('csv_to_xlsx/catID6030.csv', encoding = 'iso-8859-1')
with open('Model_Names.txt', 'r') as model_list:
	fileLines = model_list.readlines()
	brkdwn = []
	for model in fileLines:
		mod1 = model.strip()
		mod2 = mod1.split(' ')
		for i in range(len(mod2)):
			mod2[i] = mod2[i].replace('/',' ')
		brkdwn.append(mod2)
		for i in range(len(brkdwn)):
			if len(brkdwn[i]) == 1:
				hits = df[df['title'].str.contains(brkdwn[i][0], case=False)]
			elif len(brkdwn[i]) == 2:
				hits = df[df['title'].str.contains(brkdwn[i][0], case=False) & df['title'].str.contains(brkdwn[i][1], case=False)]
			elif len(brkdwn[i]) == 3:
				hits = df[df['title'].str.contains(brkdwn[i][0], case=False) & df['title'].str.contains(brkdwn[i][1], case=False) & df['title'].str.contains(brkdwn[i][2], case=False)]
			else:
				print('WTF?!')
#			writer = ExcelWriter('c://users//matt//desktop//pythonprojects//ebay//human_readable_results//' + model.strip().replace('/','') + '.xlsx', engine='xlsxwriter', options={'strings_to_urls': False})
#			hits.to_excel(writer)
#			writer.save()
			hits.to_csv('c://users//matt//desktop//pythonprojects//ebay//csv_to_xlsx//' + model.strip().replace('/','') + '.csv', index=False)