from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen

url = 'https://scrapebook22.appspot.com/'
csv_file = open("email_list.csv", "w")

response = urlopen(url).read()
soup = BeautifulSoup(response)

for link in soup.findAll('a'):
    if link.string == "See full profile":
        person_url = "https://scrapebook22.appspot.com" + link["href"]
        person_html = urlopen(person_url).read()
        person_soup = BeautifulSoup(person_html)
        email = person_soup.find("span", attrs={"class": "email"}).string
        city = person_soup.find("span", attrs={"data-city": True}).string
        name = person_soup.find("div", attrs={"class": "col-md-8"}).h1.string

        csv_file.write(email + "," + city + "," + name + "\n")
csv_file.close()
