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
ANames=[]
AOld_Prices=[]
ANew_Prices=[]
olist=[]
nlist=[]

#name

prodname=soup.find_all('a', class_="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal")
print("Amazon Exlusive search results:", searchprod,"->")
print()
#print(prodname.text, "(Amazon Exclusive)")
for i in prodname:
    ANames.append(i.text)
print(ANames[2:5])

#price

oprice=soup.find_all('span', class_="a-price a-text-price")
nprice=soup.find_all('span', class_="a-price-whole")
def rep(x,y): #incase of values repeating twice 
	mid=int(len(x)/2)
	b=x[0:mid]
	y.append(b)

    
for i in oprice:
    AOld_Prices.append(i.text)
    
for a in AOld_Prices[2:5]:
	rep(a,olist)
print(olist)
    
for i in nprice:
    ANew_Prices.append(i.text)
ANew_Prices= ["₹"+ e for e in ANew_Prices]
print(ANew_Prices[2:5])

#FLIPKART

if " " in searchprod:
    searchprod.replace(" ", "%20")   #url-correcter

#get html
h={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
#To bypass bot-check

url='https://www.flipkart.com/search?q='+searchprod+'&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
r= requests.get(url, headers=h) 

#parse html
soup=BeautifulSoup(r.content, 'html.parser')

#pre-dec variables
Names=[]
Old_Prices=[]
New_Prices=[]

#1st way of listing 

#name
prodname=soup.find_all('div', attrs={'class' :"_4rR01T"} )
# if bool(prodname)==True:`
if prodname:
        print("\nFlipkart Exclusive search results:", searchprod,"->")
        print()

        for i in prodname:
            Names.append(i.text)
        print(Names[:3])
        #price
        oprice=soup.find_all('div', class_="_3I9_wc _27UcVY")
        nprice=soup.find_all('div', class_="_30jeq3 _1_WHN1")

        for i in oprice:
            Old_Prices.append(i.text)
        print(Old_Prices[:3])

        for i in nprice:
            New_Prices.append(i.text)
        print(New_Prices[:3])


        
        

import pandas as pd
da=pd.DataFrame({'Product Name':ANames[2:5],'Old Price':AOld_Prices[2:5],'New Price':ANew_Prices[2:5]})
df=pd.DataFrame({'Product Name':Names[2:5],'Old Price':Old_Prices[2:5],'New Price':New_Prices[2:5]})
da.head(4)
df.head(4)

htmla = da.to_html()
htmlf = df.to_html()

#write html to file
#text_file = open("index.html", "w")
with open('pricestable.html',"w", encoding="utf-8") as text_file:
    text_file.write(htmla)
    text_file.write(htmlf)
print("Done.")