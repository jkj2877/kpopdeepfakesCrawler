import requests
from bs4 import BeautifulSoup

headers = {
    "Cookie": "kd_front_var=1; kd_session=147e60d28dd51593a35ff74cb5b987d0348d3f10d3881959c12c15d1dc21610f; vidkey=17066",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
	"Referer": "https://kpopdeepfakes.net/deepfakes/request-seohyun/request-seolhyun/"
}

def get_files_url(url):
	response = requests.get(url, headers=headers).text
	soup = BeautifulSoup(response, 'lxml')
	url_m3u8 = soup.find_all("source", type="application/x-mpegURL")[0]['src']
	url_split = url_m3u8.split("/")[-1]
	url_key = url_m3u8.replace(url_split, "php.key")
	return url_m3u8, url_key


def get_merge_files(url_m3u8, url_key):
	response1 = requests.get(url_m3u8, headers=headers)
	response2 = requests.get(url_key, headers=headers)

	if response1.status_code == 200 and response2.status_code == 200:
		with open("index.m3u8", "wb") as f:
			f.write(response1.content)
		with open("key.php", "wb") as f:
			f.write(response2.content)
	else:
		print("download failed, parameter 'headers' may have an error.")

def main():
	url = "https://kpopdeepfakes.net/deepfakes/request-seohyun/request-seolhyun/"
	url_m3u8, url_key = get_files_url(url)
	get_merge_files(url_m3u8, url_key)


if __name__=="__main__":
	main()