import requests
from bs4 import BeautifulSoup
import csv

file = open('patient.csv','w')
writer=csv.writer(file)
#Header
#writer.writerow(['Name'.encode('utf-8'),'Dob'.encode('utf-8')])
writer.writerow(['RequestID','Name','Dob','Mobile','Nationality','IDtype','ID','Gender','Resulttime','Hours Since Result','Result'])


for xx in range(329, 10000):
    URL = 'https://testcorona.co/verify/qr/'+str(xx)
   # print(URL)
    page = requests.get(URL)
    
    soup = BeautifulSoup(page.content, 'html.parser')


    job_elems = soup.find('div', class_='col')

    final_list=job_elems.get_text().strip().splitlines()

    #print(final_list)


    tempList=[xx,]

    for i in final_list:
        #  print(i.replace('-', ':').split(':'))
        #print(i[i.find(':')+1:].strip())
        tempList.append(i[i.find(':')+1:].strip())
        

    #print(tempList)
    writer.writerow(tempList)

    #lst=['Name : DINA ATEF ZAKARIA ISMAIL ', 'Date of birth : 2012-11-04 ']


file.close()