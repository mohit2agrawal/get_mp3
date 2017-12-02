# Le o arquivo com as músicas
# otém os links
# chama o download
# Registra se download com sucesso na lista de links
# Se Tudo ok, remove a lista de links. 
#		Senão: Erro, pega a partir do último link que teve sucesso

import sys
import os
from subprocess import call

from youtube import YoutubeSearch
import download

filename = sys.argv[1] if len(sys.argv) > 1 else 'musics.txt'

if os.path.exists(filename):
	music_list = []
	with open(filename, 'r') as file:
		music_list = file.readlines()

	yt = YoutubeSearch()
	dl = download.Mp3ify()

	for i in range(len(music_list)):
		music = music_list[i].replace('\n', '').replace('\r', '')
		video_id = yt.search_link(music, True)
		if video_id:
			dl.get_file_from_yt(video_id=video_id, title=music, media='mp3')
else:
	print('File: '+ filename + ' not found.')
