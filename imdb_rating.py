from bs4 import BeautifulSoup
import requests
import os
import sys

def getRatingAndNoOfUsers(mov_name,mov_url):
	url = 'http://www.imdb.com' + mov_url
	r = requests.get(url)
	soup = BeautifulSoup(r.text,'html.parser')
	try:
		rating = soup.find("div",{"class":"titlePageSprite star-box-giga-star"}).text
		item = soup.find("div",{"class","star-box-details"}).find_all('a')
		no_of_users_rated = item[0].contents[1].text
		print "#####", mov_name,"#####", "#####",rating ,"#####","#####", no_of_users_rated,"#####"
	except:
		print "#####",mov_name,"#####", "***** Not rated *****"

movielist = []

def getMovieNames(path):
	dirs = os.listdir(path)
	uwords = ['240p','360p','480p','720p','1080p','rip','x264','h264','bluray','dvd','xvid','cd','dual','audio','hindi','eng','mb','limited']  #words not of use in movie name
	#fileext = ['.mp4','.avi','.mkv']
	fnames = []
	for fname in dirs:
		temp = fname
		fname = fname.lower()
		if ".srt" in fname: #check for subtitles
			continue
		cpath = os.path.join(path, temp)
		if os.path.isdir(cpath):  #check for a directory
			fnames.append(fname)
			#print fname
		else:
			fnames.append(fname[:-4]) #removing extension
			#print fname[:-4]  
	#print fnames
	for fname in fnames:
		for uword in uwords:
			idx = fname.find(uword)
			#print fname,uword,idx
			if idx == -1:
				continue
			else:
				idx = idx - 1
				while idx>=0:
					if fname[idx]>='a' and fname[idx]<='z':
						idx = idx - 1
					# elif  fname[idx]=='[' or fname[idx]=='.' or fname[idx]=='_' or fname[idx]=='-':
					# 	idx = idx - 1
					# 	break
					else:
						break
				fname = fname[:idx+1]
			
		idx1 = fname.find('[')
		if idx1 != -1: 
			idx2 = fname.find(']',idx1)
			strg = fname[idx1+1:idx2]
			strg = strg.strip()
			#print "########################",strg
			if not strg.isdigit():
				fname = fname[:idx1] + fname[idx2+1:]

		idx1 = fname.find('(')
		if idx1 != -1: 
			idx2 = fname.find(')',idx1)
			strg = fname[idx1+1:idx2]
			strg = strg.strip()
			#print "################",strg
			if not strg.isdigit():
				fname = fname[:idx1] + fname[idx2+1:]
		fname = fname.replace('.',' ')
		movielist.append(fname)
	#print movielist

def _init_():
	path = '/Users/gansagar/Desktop/backup/movies/'
	getMovieNames(path)
	sys.stdout = open(path+'movies rating.txt', "w")
	print "############# Movie #############","############# Rating #############" , "############# No of Users Rated #############"
	for movie_name in movielist:
		base_url = 'http://www.imdb.com/find?q='
		url = base_url + movie_name + '&s=all'
		#print url
		r = requests.get(url)

		soup = BeautifulSoup(r.text,'html.parser')

		#print movie_name
		try:
			mov_list = soup.find_all("table",{"class":"findList"})

			# print mov_list
			details = mov_list[0].find_all("td",{"class":"result_text"})
			#print details ,'\n'

			link = details[0].contents[1].get('href')
			mov_name = details[0].text
			# print mov_name.encode('utf-8'),link,'\n'
			getRatingAndNoOfUsers(mov_name.encode('utf-8'),link)
		except:
			print "#####",movie_name,"#####","!!!!**********!!!"
			pass


def test():
	movie_name = 'spy'
	base_url = 'http://www.imdb.com/find?q='
	url = base_url + movie_name + '&s=all'
	print url
	r = requests.get(url)

	soup = BeautifulSoup(r.text,'html.parser')

	print movie_name
	mov_list = soup.find_all("table",{"class":"findList"})

	print mov_list
	details = mov_list[0].find_all("td",{"class":"result_text"})
	print details ,'\n'

	link = details[0].contents[1].get('href')
	mov_name = details[0].text
	print mov_name.encode('utf-8'),link,'\n'
	getRatingAndNoOfUsers(mov_name.encode('utf-8'),link)

#test()
_init_()
