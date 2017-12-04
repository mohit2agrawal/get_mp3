#-*- coding: utf-8 -*-

import requests as req
# - Especificação Mp3ify -
# Constantes:
# protocol 	= http
# method 	= GET
# host 		= 213.136.69.55
# path 		= /mp3ify/final-download-new.php?

# Entradas com valor padrão:
# action	= ??? Default = download 
# media		= Formato do arquivo, default = mp3

# Entradas variáveis: 
# video_id 	= Predicado video youtube, 
#			  ex: ua2k52n_Bvw (Required)
# 			  https://www.youtube.com/watch?v=ua2k52n_Bvw
# title		= Nome do vídeo.
class Mp3ify(object):
	URL = 'http://213.136.69.55/mp3ify/final-download-new.php?' \
		  'action=download'

	def format_url(self, video_id: str, title: str, media: str) -> str:
		print (self.URL+ '&videoid='+ video_id+ '&title='+title+ '&media='+ media)
		return (self.URL+ '&videoid='+ video_id+ '&title='+title+ '&media='+ media)


	def save_file(self, content: str, path: str, media: str):
		if path:
			with open(path+ '.'+ media, 'wb') as file:
				file.write(content)


	#def __show_dl_progress(self, response, file_name):
		#print ("Downloading %s" % file_name)
        #response = requests.get(link, stream=True)
        #total_length = response.headers.get('content-length')

        #if total_length is None: # no content length header
            #f.write(response.content)
        #else:
            #dl = 0
            #total_length = int(total_length)
            #for data in response.iter_content(chunk_size=4096):
                #dl += len(data)
                #f.write(data)
                #done = int(50 * dl / total_length)
                #sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )    
                #sys.stdout.flush()

	def request_service(self, video_id: str, title: str, media: str):
		res = req.get(self.format_url(video_id, title, media))
		return res

	def get_file_from_yt(self, video_id: str, title: str, media: str, path: str = None) -> bytes:
		if not path:
			res = req.get(self.format_url(video_id, title, media))
			if res.ok and res.text != 'Error 404':
				self.save_file(res.content, title, media)
			else:
				print('Error: Response is not a mp3 file. Status: %s Response text: %s' %(res.status, res.text))


# Saídas:
# barra de progresso
# status ao final do download
# 

