import re
from html.parser import HTMLParser
import urllib.request
import mysql.connector
from mysql.connector import Error


location = "https://www.vrbo.com/vacation-rentals/family/canada/british-columbia"
url = urllib.request.urlopen(
    "https://www.vrbo.com/vacation-rentals/family/canada/british-columbia")
html = url.read().decode()
url.close()


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
    'script', (), 'text'])
WebParser.results = []

location = location[52:59]+" "+location[60:68]+", "+location[45:51]

all_facilitites = []
for index in range(0, len(Facilites)):
    all_facilitites.append(Facilites[index].split(" · "))

for index in range(0, len(all_facilitites)):
    if(len(all_facilitites[index]) < 3):
        temp = all_facilitites[index]
        temp.append('None')
        all_facilitites[index] = temp

for index in range(0, len(Image)):
    if(Image[index].startswith('window.__PRELOADED_STATE__ ')):
        Image = Image[index]


list_match_img_url1 = re.findall(
    r'"tripleId":(.*?),"thumbnailUrl":(.*?),', Image)
'''for i in list_match_img[-6:]:
    print(i, "\n")'''
list_match_img_url2 = re.findall(
    r'"tripleId":(.*?),"thumbnailUrl2":(.*?),', Image)
list_match_img_url3 = re.findall(
    r'"tripleId":(.*?),"thumbnailUrl3":(.*?),', Image)


matched_img1 = list_match_img_url1[-6:]
matched_img2 = list_match_img_url2[-6:]
matched_img3 = list_match_img_url3[-6:]

collapse_img = []
for i in range(len(matched_img1)):
    collapse_img.append([matched_img1[i][1],
                         matched_img2[i][1], matched_img3[i][1]])


all_information = []
print("\n\n\n")
for i in range(0, len(HotelName)):
    all_information.append([HotelName[i], location, all_facilitites[i],
                            Price[i], collapse_img[i]])


''' for i in all_information:
    print(i, "\n")
 '''

def insert_into_mysql_database(titile, location, sleeps, bedroom, bathroom, image_1, image_2, image_3, pirce):
    try:
        mydb_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database='test',
        )
        cursor = mydb_connection.cursor()
        query = """INSERT INTO family_friendly_rentals (Title, Location, Sleeps, Bedroom, Bathroom, Image1, Image2, Image3, Price) 
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) """
        record = (titile, location, sleeps, bedroom, bathroom,
                  image_1, image_2, image_3, pirce)
        cursor.execute(query, record)
        mydb_connection.commit()
        print("Inserted Successfully")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if mydb_connection.is_connected():
            cursor.close()
            mydb_connection.close()
            print("MySQL connection is closed")


for info in all_information:
    insert_into_mysql_database(info[0],
                               info[1],
                               info[2][0],
                               info[2][1],
                               info[2][2],
                               info[4][0],
                               info[4][1],
                               info[4][2],
                               info[3])
