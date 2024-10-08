import json
import os
import requests
import time
requests.packages.urllib3.disable_warnings()

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}
headers['Cookie'] = 'SESSDATA=1bd55a3f%2C1743849764%2C78b14%2Aa1CjAaMafVM5-ngL4wd1K_RcXeYuwlvLboCmdoV8lRNXcIAnKiwPz4fFmpWsgD1j70W4USVk1uOFZac3BwN1RTbXBoeExDMmUwNUtta3RFVzZNZmc4MUhtM18tWEtoSXRVTG9ZQjhTdGtZU1dOOExaQTJRT1hSVkg0X2R1QkdQcHFvdURlMW1lbG5RIIEC'
def safe_httpget(url):
	r = requests.get (url, headers=headers)
	time.sleep(1)
	return r.text
def parse_bvid(url):
	if 'bilibili.com' in url:
		bvid = url.split('video/')[1].split('?')[0]
		if not bvid.startswith('BV'):
			bvid = url.split('video/')[1].split('/?')[0]
			if not bvid.startswith('BV'):
				print('Invalid URL')
		return bvid
	else:
		return url
def download(bvid):
	url = f'https://api.bilibili.com/x/player/pagelist?bvid={bvid}&jsonp=jsonp'
	r = safe_httpget(url)
	result = json.loads(r)
	print(r)
	data = result['data']
	video_title = data[0]['part']
	cid = data[0]['cid']
	print(cid)
	url = f'https://api.bilibili.com/x/player/wbi/v2?bvid={bvid}&cid={cid}'
	r = safe_httpget(url)
	result = json.loads(r)
	

	subtitle = result['data']['subtitle']
	subtitle_url = 'https:'+subtitle['subtitles'][0]['subtitle_url']
	print(subtitle_url)
	r = safe_httpget(subtitle_url)
	data = json.loads(r)
	bodies = data['body']
	with open(video_title + '_transcript.txt', 'w', encoding='utf-8') as transcript_file:
		for body in bodies:
			transcript_file.write(f"{body['content']}")
	with open(video_title+'.txt', 'w', encoding='utf-8') as f:
		for body in bodies:
			start_time = time.strftime('%H:%M:%S', time.gmtime(body['from']))
			end_time = time.strftime('%H:%M:%S', time.gmtime(body['to']))
			f.write(f"{start_time} --> {end_time}\n{body['content']}\n\n")
	print(f"Downloaded {video_title}.txt")
url = input('Enter the URL of the bilibili video: ')
bvid = parse_bvid(url)
print(bvid)
download(bvid)
