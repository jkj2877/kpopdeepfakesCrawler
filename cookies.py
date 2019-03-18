import requests

headers = {
    	"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"
}
url = "https://kpopdeepfakes.net/deepfakes/seolhyun-bouncing-around/"

cookies_list = []
response = requests.get(url, headers=headers)
for key, value in response.cookies.items():
    cookies_list.append(key + "=" + value)
cookies = cookies_list[0] + ", " + cookies_list[1]
headers["Cookie"] = cookies
print(headers)