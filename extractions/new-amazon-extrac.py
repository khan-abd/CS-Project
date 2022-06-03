#Features of this version:
# -Top 3 search results -Removed sponsored products


from bs4 import BeautifulSoup
import requests

searchprod=input("Enter product to be searched: ")
if " " in searchprod:
    searchprod.replace(" ", "+")   #url-correcter

#get html
h={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
 #To bypass bot-check

url='https://www.amazon.in/s?k='+searchprod+'&crid=8EC88KDQ73CJ&sprefix=iphone+1%2Caps%2C269&ref=nb_sb_noss_2'
r= requests.get(url, headers=h) 

#parse html
soup=BeautifulSoup(r.content, 'html.parser')

#pre-dec variables
Names=[]
Old_Prices=[]
New_Prices=[]
olist=[]
nlist=[]
  

#name

prodname=soup.find_all('a', class_="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal")
print("Search results for", searchprod,"->")
print()
#print(prodname.text, "(Amazon Exclusive)")
for i in prodname:
    Names.append(i.text)
print(Names[2:5])

#price

oprice=soup.find_all('span', class_="a-price a-text-price")
nprice=soup.find_all('span', class_="a-price-whole")
def rep(x,y): #incase of values repeating twice 
	mid=int(len(x)/2)
	b=x[0:mid]
	y.append(b)

    
for i in oprice:
    Old_Prices.append(i.text)
    
for a in Old_Prices[2:5]:
	rep(a,olist)
print(olist)
    
for i in nprice:
    New_Prices.append(i.text)
New_Prices= ["₹"+ e for e in New_Prices]
print(New_Prices[2:5])

