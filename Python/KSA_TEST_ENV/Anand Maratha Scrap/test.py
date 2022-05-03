
import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd


URL = 'https://www.anandmaratha.com/details.php?mgid=120002'
print(URL)

page = requests.get(URL)

#print(page)
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup)

#job_elems = soup.find('div', class_='col-lg-9 col-md-9 col-sm-9 col-xs-12')
#job_elems = soup.find_all('h5', class_='col-md-6')
job_elems = (soup.find_all('img',  class_='img-responsive'))
#print(job_elems.find(''))

for z in job_elems:
    #print(z)
    #print(type(z))
    #print(z.attrs)
    print(z.attrs['src'])
    print('----')
#print(job_elems[64:job_elems.find('</font>')])

