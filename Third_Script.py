import os, pandas as pd
from numpy import nan as NaN
from datetime import datetime
from pandas import ExcelWriter


for file in os.listdir('c://users//matt//desktop//pythonprojects//ebay//csv_to_xlsx'):
	df = pd.read_csv('c://users//matt//desktop//pythonprojects//ebay//csv_to_xlsx//' + file, encoding='iso-8859-1')
	df.drop_duplicates(df.columns.difference(['sellerID']), inplace=True)
	if os.path.isfile('c://users//matt//desktop//pythonprojects//ebay//results' + file):
		df.to_csv('c://users//matt//desktop//pythonprojects//ebay//results//' + file, mode='a', index=False, header=False, encoding='iso-8859-1')
	else:
		df.to_csv('c://users//matt//desktop//pythonprojects//ebay//results//' + file, index=False, encoding='iso-8859-1')
	print(file[:-4])
	df = pd.read_csv('c://users//matt//desktop//pythonprojects//ebay//results//' + file, encoding='iso-8859-1')
	df['end'] = pd.to_datetime(df['end'])
	df['start'] = pd.to_datetime(df['start'])
	df['hours'] = ((df['end'] - df['start']).dt.total_seconds())/3600
	twodays = df[df['hours'] < 360]
#	sevendays = df[(df['hours'] > 48) & (df['hours'] < 168)]
	sevendays = df[df['hours'] < 168]
	two_cat = twodays['cat name'].value_counts().reset_index(name='count')
	sev_cat = sevendays['cat name'].value_counts().reset_index(name='count')
	two_cat.rename(columns={'index':'cat name'}, inplace=True)
	sev_cat.rename(columns={'index':'cat name'}, inplace=True)
	two_cat['avg price'] = 0
	for i in range(len(two_cat['cat name'])):
		two_cat['avg price'][i] = twodays[twodays['cat name'] == str(two_cat['cat name'].tolist()[i])]['price'].mean()
	sev_cat['avg price'] = 0
	for i in range(len(sev_cat['cat name'])):
		sev_cat['avg price'][i] = sevendays[sevendays['cat name'] == str(sev_cat['cat name'].tolist()[i])]['price'].mean()
	def by_cat(Series, DataFrame):
		blank = pd.Series([NaN,NaN,NaN,NaN,NaN,NaN], index=['title', 'cat name', 'cat id', 'price', 'sellerID', 'url'])
		listlenofcategories = list(range(len(Series['cat name'])))
		catorglist = []
		for x in listlenofcategories:
			catorglist.append(str(x)) 
			catorglist[x] = DataFrame[DataFrame['cat name'] == str(Series['cat name'].tolist()[x])][['title', 'cat name', 'cat id', 'price', 'sellerID', 'url']]
		catorglist = catorglist[0:len(Series[Series['count'] >= Series['count'].quantile(q=0.87)]['cat name'])]
		for i in range(len(catorglist)):
			catorglist[i] = catorglist[i].append(blank, ignore_index=True)
		return (catorglist)
	def dflistapnd(dflist):
		if len(dflist) == 1:
			longdf = dflist[0]
		elif len(dflist) == 0:
			longdf = ''
		else:
			longdf = dflist.pop(0).append(dflist, ignore_index=False)
		return longdf
	twodaelist = by_cat(two_cat, twodays)
	sevdaelist = by_cat(sev_cat, sevendays)
	def series_destroy(ser):
		listcat = []
		for i in range(len(ser) - 1):
			for thing in ser[i].lower().split():
				listcat.append(thing)
		return (listcat)		
	def wizwordry(listy):
		shisty = []
		blanky = pd.Series([NaN,NaN], index=['word', 'count'])
		for item in listy:
			first = pd.DataFrame(series_destroy(item['title']))
			sec = first[0].value_counts().reset_index(name='count')
			sec.rename(columns={'index':'word'}, inplace=True)
			third = sec[sec['count'] >= sec['count'].quantile(q=0.92)]
			third = third.append(blanky, ignore_index=True)
			shisty.append(third)
		if len(shisty) == 1:
			wristy = shisty[0]
		elif len(shisty) == 0:
			wristy = ''
		else:
			wristy = shisty.pop(0).append(shisty, ignore_index=True)
		return(wristy)		
	tdwordctallcats = wizwordry(twodaelist)
	sdwordctallcats = wizwordry(sevdaelist)
	tcat_df = dflistapnd(twodaelist)
	scat_df = dflistapnd(sevdaelist)
	writer = ExcelWriter('c://users//matt//desktop//pythonprojects//ebay//human_readable_results//' + file[:-4] + '.xlsx') 
#	'{}.xlsx'.format(datetime.now().strftime('-%m-%d-%y')))
	twodays.to_excel(writer, sheet_name='15 Days Sold-Raw Results')
	two_cat.to_excel(writer, sheet_name='15 Days-Category Counts')
	tcat_df.to_excel(writer, sheet_name='15 Days-Top Category Results')
	tdwordctallcats.to_excel(writer, sheet_name='15 Days-Word Counts')
	sevendays.to_excel(writer, sheet_name='Seven Days Sold-Raw Results')
	sev_cat.to_excel(writer, sheet_name='Seven Days-Category Counts')
	scat_df.to_excel(writer, sheet_name='Seven Days-Top Category Results')
	sdwordctallcats.to_excel(writer, sheet_name='Seven Days-Word Counts')
	writer.save()
	os.remove('c://users//matt//desktop//pythonprojects//ebay//csv_to_xlsx//' + file)