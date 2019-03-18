import requests
from bs4 import BeautifulSoup


def get_cookies(url, headers):
	cookies_list = []
	response = requests.get(url, headers=headers)
	for key, value in response.cookies.items():
		cookies_list.append(key + "=" + value)
	cookies = cookies_list[0] + "; " + cookies_list[1]
	headers["Cookie"] = cookies
	headers["Referer"] = url
	return headers

def get_files_url(url, headers):
	response = requests.get(url, headers=headers).text
	soup = BeautifulSoup(response, 'lxml')
	url_m3u8 = soup.find_all("source", type="application/x-mpegURL")[0]['src']
	url_split = url_m3u8.split("/")[-1]
	url_key = url_m3u8.replace(url_split, "key.php")
	print(url_m3u8, "\n", url_key)
	return url_m3u8, url_key


def get_merge_files(url_m3u8, url_key, headers):
	response1 = requests.get(url_m3u8, headers=headers)
	response2 = requests.get(url_key, headers=headers)

	if response1.status_code == 200 and response2.status_code == 200:
		with open("index.m3u8", "wb") as f:
			f.write(response1.content)
		with open("key.php", "wb") as f:
			f.write(response2.content)
	else:
		print(response1.status_code, response2.status_code, "download failed, parameter 'headers' may have an error.")

def main():
	headers = {
		"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"
	}
	url = "https://kpopdeepfakes.net/deepfakes/hyejeong-sex-in-hotel/"
	headers = get_cookies(url,headers)
	print(headers)
	url_m3u8, url_key = get_files_url(url,headers)
	get_merge_files(url_m3u8, url_key, headers)


if __name__=="__main__":
	main()