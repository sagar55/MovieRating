from bs4 import BeautifulSoup
import requests

def getRatingAndNoOfUsers(mov_name,mov_url):
	url = 'http://www.imdb.com' + mov_url
	r = requests.get(url)
	soup = BeautifulSoup(r.text,'html.parser')
	rating = soup.find("div",{"class":"titlePageSprite star-box-giga-star"}).text
	item = soup.find("div",{"class","star-box-details"}).find_all('a')
	no_of_users_rated = item[0].contents[1].text
	print mov_name, rating , no_of_users_rated

def getMovieNames():
	test

base_url = 'http://www.imdb.com/find?q='
movie_name = 'spy'
url = base_url + movie_name + '&s=all'
#print url
r = requests.get(url)

soup = BeautifulSoup(r.text,'html.parser')

mov_list = soup.find_all("table",{"class":"findList"})

# print mov_list
details = mov_list[0].find_all("td",{"class":"result_text"})
#print details ,'\n'

link = details[0].contents[1].get('href')
mov_name = details[0].text
# print mov_name,link,'\n'
getRatingAndNoOfUsers(mov_name,link)






