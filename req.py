import requests 
print('Url kiriting :')
url= str(input())
print("rasm nomini kiriting :" )
name=str(input())

img=requests.get(url)
img_option=open(name +'.jpg','wb')
img_option.write(img.content)


# import requests 
# from bs4 import BeautifulSoup as BS 


# r= requests.get("https://stopgame.ru/show/114649/crown_trick_review")
# html =BS(r.content, "html.parser")

# for el in html.select(".items > .article-summary"):
#     title= el.select('.caption > a')
#     print( title[0].text)

