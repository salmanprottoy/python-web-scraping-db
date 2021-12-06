from urllib import response
from urllib import request
from urllib.request import Request
from urllib.request import urlopen
from urllib.parse import urlencode
from urllib.error import HTTPError
from urllib.error import URLError


def get(url, payload, headers):
    payload = urlencode(payload)
    url = url + "?" + payload
    try:
        request = Request(url=url, headers=headers, method="GET")
        response = urlopen(request)
        return response.read().decode('utf-8')
    except Exception as e:
        print("Request error:", e)
        return "no content available!"


def post(url, payload, headers):
    payload = urlencode(payload)
    try:
        request = Request(url=url, data=payload.encode(),
                          headers=headers, method='POST')
        response = urlopen(request)
        return response.read().decode('utf-8')
    except Exception as e:
        print("Request error", e)
        return "no content available"


res = get(url="https://www.vrbo.com/vacation-rentals/family/canada/british-columbia",
          payload={},
          headers={
              "User-Agent":	"Mozilla/5.0 (X11 Ubuntu Linux x86_64 rv: 94.0) Gecko/20100101 Firefox/94.0",
          }
          )
print(res)
