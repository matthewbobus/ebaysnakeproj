import requests, os, pandas as pd
from bs4 import BeautifulSoup as soup
from datetime import datetime

with open ("C://Users//Matt//Desktop//PythonProjects//Ebay//category_IDs_new.txt", "r") as catnums:
	Id_text = catnums.readlines()

with open ("C://users//matt//desktop//pythonprojects//ebay//search_words.txt", "r") as martin:
	ting = martin.readlines()
	if ting == []:
		ting.append("")

url = "http://svcs.ebay.com/services/search/FindingService/v1"					
querystring = {
"categoryId":Id_text[0].strip(),
"keywords": ting[0].strip().replace('\"',''),
#"itemFilter(0).name":"ListingType",
#"itemFilter(0).value(0)":"Auction",
#"itemFilter(0).value(1)":"FixedPrice",
#"itemFilter(0).value(2)": "AuctionWithBIN",
"outputSelector":"SellerInfo",
"itemFilter(0).name":"SoldItemsOnly",
"itemFilter(0).value":"true",
"itemFilter(1).name":"Condition",
"itemFilter(1).value(0)":"New",
"itemFilter(1).value(1)":"1000",
#"itemFilter(2).name":"MinPrice",
#"itemFilter(2).value":"50",
"paginationInput.pageNumber":1
}
headers = {
'x-ebay-soa-security-appname': "MatthewB-Finder-PRD-28e2d25a0-432feaac",
'x-ebay-soa-operation-name': "findCompletedItems",
'cache-control': "no-cache"
}
response = requests.get(url, headers=headers, params=querystring).text
print(requests.get(url, headers=headers, params=querystring).url)
tasty = soup(response, 'xml')
result_count = (tasty.find('totalPages'))
print("pages: " + result_count.text)
print(tasty.find('ack').text)
input('Everything good?...')
		###____###
with open ("C://users//matt//desktop//pythonprojects//ebay//search_words.txt", "r") as martin:
	ting = martin.readlines()
	if ting == []:
		ting.append("")
	with open ("C://Users//Matt//Desktop//PythonProjects//Ebay//category_IDs_new.txt", "r") as catnums:
		Id_text = catnums.readlines()
		for x in range(len(Id_text)):
			for i in range(len(ting)):
				url = "http://svcs.ebay.com/services/search/FindingService/v1"
				querystring = {"categoryId":Id_text[x].strip(),
				"keywords": ting[i].strip().replace('\"',''),
				#"itemFilter(0).name":"ListingType",
				#"itemFilter(0).value(0)":"Auction",
				#"itemFilter(0).value(1)":"FixedPrice",
				#"itemFilter(0).value(2)": "AuctionWithBIN",
				"outputSelector":"SellerInfo",
				"itemFilter(0).name":"SoldItemsOnly",
				"itemFilter(0).value":"true",
				"itemFilter(1).name":"Condition",
				"itemFilter(1).value(0)":"New",
				"itemFilter(1).value(1)":"1000"
				#"itemFilter(2).name":"MinPrice",
				#"itemFilter(2).value":"50"
				}
				headers = {
			    'x-ebay-soa-security-appname': "MatthewB-Finder-PRD-28e2d25a0-432feaac",
			    'x-ebay-soa-operation-name': "findCompletedItems",
			    'cache-control': "no-cache"
			    }
			    ###____###
				response = requests.get(url, headers=headers, params=querystring).text
				tasty = soup(response, 'xml')
				result_count = (tasty.find('totalPages'))
				if int(result_count.text) > 100:
					result_count = 100
				else:
					result_count = int(tasty.find('totalPages').text)
				for page in range(result_count,0,-1):
					url = "http://svcs.ebay.com/services/search/FindingService/v1"
					querystring = {"categoryId":Id_text[x].strip(),
					"keywords": ting[i].strip().replace('\"',''),
					#"itemFilter(0).name":"ListingType",
					#"itemFilter(0).value(0)":"Auction",
					#"itemFilter(0).value(1)":"FixedPrice",
					#"itemFilter(0).value(2)": "AuctionWithBIN",
					"outputSelector":"SellerInfo",
					"itemFilter(0).name":"SoldItemsOnly",
					"itemFilter(0).value":"true",
					"itemFilter(1).name":"Condition",
					"itemFilter(1).value(0)":"New",
					"itemFilter(1).value(1)":"1000",
					#"itemFilter(2).name":"MinPrice",
					#"itemFilter(2).value":"50",
					"paginationInput.pageNumber":page
					}
					headers = {
				    'x-ebay-soa-security-appname': "MatthewB-Finder-PRD-28e2d25a0-432feaac",
				    'x-ebay-soa-operation-name': "findCompletedItems",
				    'cache-control': "no-cache"
				    }
				    ###____###
					response = requests.get(url, headers=headers, params=querystring).text
					tasty = soup(response, 'xml')
					###____###
					titles = ""
					for item_title in tasty.find_all('title'):
						titles += (str(item_title.text).replace(',', '') + ',')
					titles = titles.split(',')
					item_id = ""
					for ids in tasty.find_all('itemId'):
						item_id += (str(ids.text) + ',')
					item_id = item_id.split(',')
					categories = ""
					for category in tasty.find_all('primaryCategory'):
						categories += (str(category.find('categoryName').text).replace(',','') + ',')
					categories = categories.split(',')
					categoryId = ""
					for cat_no in tasty.find_all('primaryCategory'):
						categoryId += (str(cat_no.find('categoryId').text) + ',')
					categoryId = categoryId.split(',')
					prices = ""
					for price in tasty.find_all('currentPrice'):
						prices += (str(price.text).replace(',','') + ',')
					prices = prices.split(',')
					urls = ""
					for url in tasty.find_all('viewItemURL'):
						urls += (str(url.text) + ',')
					urls = urls.split(',')
					sellerID = ""
					for sellerName in tasty.find_all('sellerUserName'):
						sellerID += (str(sellerName.text).replace(',','') + ',')
					sellerID = sellerID.split(',')
					start = ""
					for s_time in tasty.find_all('startTime'):
						raw = str(s_time.text.split('T')[1].replace('.000Z', ''))
						start += (str(s_time.text.split('T')[0]) + ' ' + raw + ',')
					start = start.split(',')
					end = ""
					for e_time in tasty.find_all('endTime'):
						raw = str(e_time.text.split('T')[1].replace('.000Z', ''))
						end += (str(e_time.text.split('T')[0]) + ' ' + raw + ',')
					end = end.split(',')
					csv_d = list(zip(titles,item_id,categories,categoryId,prices,sellerID,start,urls,end))[:-1]
					df = pd.DataFrame(csv_d, columns=['title','ID','cat name','cat id','price','sellerID','start','url','end'])
					if os.path.isfile("c://users//matt//desktop//pythonprojects//ebay//csv_to_xlsx//catID" + querystring['categoryId'] + ting[i].strip().replace('\"','') +".csv"):
						df.to_csv("c://users//matt//desktop//pythonprojects//ebay//csv_to_xlsx//catID" + querystring['categoryId'] + ting[i].strip().replace('\"','') +".csv", mode='a', index=False, header=False)
					else:
						df.to_csv("c://users//matt//desktop//pythonprojects//ebay//csv_to_xlsx//catID" + querystring['categoryId'] + ting[i].strip().replace('\"','') +".csv", index=False)

print("Good Job!")