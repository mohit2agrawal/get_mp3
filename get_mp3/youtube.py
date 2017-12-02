#-*- coding: utf-8 -*-

import requests as req
from bs4 import BeautifulSoup


class YoutubeSearch(object):
	""" This class is responsible for all interactions with Youtube site. 
		All relevant properties will be here. """

	BASE_URL = 'https://www.youtube.com/'
	SEARCH_URL = BASE_URL+ 'results?search_query='

	def __init__(self):
		pass

	def __search(self, music_name: str) -> str: 
		search_query = music_name.replace(' ','-')
		page = req.get(self.SEARCH_URL+ search_query).content
		return page

	def search_link(self, search_content: str = None, only_video_id: bool = False) -> str:
		""" Returns the link of Youtube video by music name passed as search content. """
		if not search_content:
			return None

		page = self.__search(search_content)
		soup = BeautifulSoup(page, 'html.parser')

		t = soup.find('h3', class_='yt-lockup-title')
		link = t.a['href']

		if only_video_id:
			return link.split('=')[1]

		return(self.BASE_URL + link[1:])

if __name__ == '__main__':
	from youtube import YoutubeSearch

	y = YoutubeSearch()
	print(y.search_link("", True))
	