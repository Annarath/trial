from bs4 import BeautifulSoup

#read file and read content of that specific file
with open('home.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    print(soup.prettify()) #print html code in a more organised way

    #now grab specific info that wa want e.g. want to grab every html tags that are created as h5 tag
    tags = soup.find('h5') #this only grab the first element of what we want to grab but if want to grab all h5 tags inside the "content", change .find to .find_all('h5)
    print(tags)

    courses_html_tags = soup.find_all('h5') 
    for course in courses_html_tags:
        print(course.text)

#see inspect of the particular webpage to access the html code

#e.g. grab price for the course which is under tag "div"
course_cards = soup.find_all('div', class_='card') #need _ after class as class is one of the built-in keyword where we create classes
for course in course_cards:
    course_name = course.h5.text
    course_price = course.a.text.split()[-1] #a tag stall the info abt price of the course that we want to fine
    print(course_name)
    print(course_price)
    #or
    print(f'{course_name} costs {course_price}')

#now scrape from real website e.g. job info using request library
from bs4 import BeautifulSoup
import requests #it requests library request info from specific website
html_text = requests.get('https://www.glassdoor.com/Explore/top-data-science-companies-london_IO.4,16_IL.27,33_IC2671300.htm').text
print(html_text)
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find('span', class_ = 'common__commonStyles__greenText common__commonStyles__strong pr-xsm')
print(jobs)