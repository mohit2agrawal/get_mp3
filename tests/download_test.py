import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from get_mp3 import download
except ImportError:
    print('No Import')

title 			= 'shortest landing ever, world record'
media 			= 'mp3'
video_id 		= '2q8fBMpJ_k'
expected_url 	= 'http://213.136.69.55/mp3ify/final-download-new.php?' \
		  		  'action=download&videoid='+video_id+'&' \
		  		  'title='+title+'&media='+media

def test_format_url():
	m = download.Mp3ify()
	assert(expected_url == m.format_url(video_id, title, media))

def test_request_service():
	m = download.Mp3ify()
	res = m.request_service(video_id, title, media)
	assert(res)
	assert(res.ok)
	assert(res.content)