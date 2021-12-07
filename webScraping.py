from urllib.request import Request
from urllib.request import urlopen
from urllib.parse import urlencode
from html.parser import HTMLParser
import mysql.connector


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


html = get(url="https://www.vrbo.com/vacation-rentals/family/canada/british-columbia",
           payload={},
           headers={
               "User-Agent":	"Mozilla/5.0 (X11 Ubuntu Linux x86_64 rv: 94.0) Gecko/20100101 Firefox/94.0",
           }
           )
# print(res)


class WebParser(HTMLParser):
    # search query
    query = []

    # search result match
    match = {}

    # results list
    results = []

    # handle opening tag
    def handle_starttag(self, tag, attr):
        self.match['name'] = tag
        self.match['attr'] = attr

    # handle data within a tag
    def handle_data(self, data):
        # init query tag
        tag = self.query[0]

        # init attr query
        attr = self.query[1]

        # init query output
        text = self.query[-1]

        try:
            # found tag name
            if self.match['name'] == tag:
                # attributes are not specified in query
                if not len(attr):
                    # on tag text node query
                    if text == 'text':
                        self.results.append(data)

                    # on tag attrbute data query
                    else:
                        # loop over attributes list
                        for item in self.match['attr']:
                            # init attr key and value
                            key = item[0]
                            val = item[1]

                            # query output is within attr's key
                            if text == key:
                                self.results.append(val)

                # attributes are specified in query
                else:
                    # loop over attributes list
                    for item in self.match['attr']:
                        # init available attr key and value
                        key = item[0]
                        val = item[1]

                        # init query attr key and value
                        q_key = attr[0]
                        q_val = attr[1]

                        # match key and value pairs
                        if q_key == key and q_val == val:
                            # on tag text node query
                            if text == 'text':
                                self.results.append(data)

                            # on tag attrbute data query
                            else:
                                # loop over attributes list
                                for item in self.match['attr']:
                                    # init attr key and value
                                    key = item[0]
                                    val = item[1]

                                    # query output is within attr's key
                                    if text == key:
                                        self.results.append(val)

        except:
            pass

    # handle closing tag
    def handle_endtag(self, tag):
        # reset result match after matching closing tag
        self.match = {}

# parse content


def find(content, query):
    # create parser instance
    parser = WebParser()

    # init query
    parser.query = query

    # find matching results
    parser.feed(str(content))

    # close parser
    parser.close()

    # return results
    return parser.results


# data extraction logic
HotelName = find(content=html, query=[
    'div', ('class', 'CommonRatioCard__description'), 'text'])
WebParser.results = []
Facilites = find(content=html, query=[
    'div', ('class', 'CommonRatioCard__subcaption'), 'text'])
WebParser.results = []
Price = find(content=html, query=[
    'span', ('class', 'CommonRatioCard__price__amount'), 'text'])
WebParser.results = []
Image = find(content=html, query=[
    'span', ('class', 'ListingsRatioCard__img'), 'text'])
WebParser.results = []
# CardCarousel__placeholderImage
# ListingsRatioCard__img

# loop over all items
print("Titles: \n")
for index in range(0, len(HotelName)):
    # write line
    print(HotelName[index], "\n")
#print("\n", len(HotelName), "\n")
print("Facilities: \n")
for index in range(0, len(Facilites)):
    # write line
    print(Facilites[index], "\n")
#print("\n", len(Facilites), "\n")
print("Price: \n")
for index in range(0, len(Price)):
    # write line
    print(Price[index], "\n")
#print("\n", len(Price), "\n")
print("Image: \n")
for index in range(0, len(Image)):
    # write line
    print(Image[index], "\n")

# db connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database='test',
)
if mydb.is_connected():
    print("connected successfully!")
