from email.policy import default
import requests
from bs4 import BeautifulSoup
import xlsxwriter
import time
import threading

ErroredURL=[]
finalList=[]
baseURL='https://www.anandmaratha.com'


def append_list(from_number, to_number):
    ErrorCount=0
    for x in range(from_number,to_number):
        if ErrorCount > 20:#if error count is >20 then EXIT.
            break
        print(x)
        URL = 'https://www.anandmaratha.com/details.php?mgid='+str(x)
        #print(URL)




        page = requests.get(URL)

        #print(page)
        soup = BeautifulSoup(page.content, 'html.parser')
        #print(soup)


        #find profile name
        Profile_name = str(soup.find('p'))
        Profile_name=Profile_name[64:Profile_name.find('</font>')]
        #print(Profile_name[64:job_elems.find('</font>')])
        
        #print(Profile_name[:1])
        if Profile_name[:1] != 'M':
            print('***Not Valid**** '+URL)
            ErroredURL.append(x)
            ErrorCount=ErrorCount+1 #counting errord records. If this is more than 20 EXIT.
            continue
        
        #print(Profile_name)
        ErrorCount=0

        #get image url  of profile
        job_elems = (soup.find_all('img',  class_='img-responsive'))
        i=1
        img1url=''
        img2url=''
        img3url=''
        for z in job_elems:#iterrate through all images
            #print(z)
            #print(type(z))
            #print(z.attrs)
            #print(z.attrs['src'])
            if i==1:
                img1url=baseURL+z.attrs['src']
            elif i==2:
                img2url=baseURL+z.attrs['src']
            elif i==3:
                img3url=baseURL+z.attrs['src']
            else:
                break
            i=i+1
            #print('----')

        #job_elems = soup.find_all('h5', class_='col-md-6')
        job_elems = soup.find_all('h5')

        soup2=BeautifulSoup(str(job_elems),features="html.parser")
        #print(job_elems)
        h5List=list(soup2.find_all('h5'))

        #print(list(soup2.find_all('h5')))

        count =0
        tempList=[]
        tempList.append(URL)
        tempList.append(img1url)
        tempList.append(img2url)
        tempList.append(img3url)
        tempList.append(Profile_name)
        for xx in h5List:
            each_line=str(xx)
            transformed_line=each_line[each_line.find(':')+2:each_line.find('</h5>')].strip()

            tempList.append(transformed_line)
            
            #print(count)

            #tempList.append(tempList)
        #print('Loop Inner end')
        #print(tempList)
        

        #getting candidates DOB and Gender 
        #print('DOB:'+tempList[5])
        GENDER_CANDIDATE=tempList[6]
        #print('GENDER:'+GENDER_CANDIDATE)

        #converting string date to date obj
        DOB_CANDIDATE=time.strptime(tempList[5],"%d/%m/%Y")
        DOB_reference=time.strptime('01/01/1995','%d/%m/%Y') #chnage here if need to change reference DOB

        #print(DOB_CANDIDATE)
        #print(DOB_reference)

        #checking candidates dob is after 1995 or not and FEMALE if not exit.
        if DOB_CANDIDATE >= DOB_reference and GENDER_CANDIDATE== 'FEMALE':
            print('Candidate is born after 1995 and female')
            pass
        else:
            print('Candidate is born before 1995 or Male')
            continue

        finalList.append(tempList)
        tempList=[] #reset the templist here

    #print('Loop outer end')
    #print(finalList)


append_list(130350,130370)
print(finalList)

'''
for x in range(130350, 131000): #142615
    if ErrorCount > 20:#if error count is >20 then EXIT.
        break
    print(x)
    URL = 'https://www.anandmaratha.com/details.php?mgid='+str(x)
    #print(URL)




    page = requests.get(URL)

    #print(page)
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)


    #find profile name
    Profile_name = str(soup.find('p'))
    Profile_name=Profile_name[64:Profile_name.find('</font>')]
    #print(Profile_name[64:job_elems.find('</font>')])
    
    #print(Profile_name[:1])
    if Profile_name[:1] != 'M':
        print('***Not Valid**** '+URL)
        ErroredURL.append(x)
        ErrorCount=ErrorCount+1 #counting errord records. If this is more than 20 EXIT.
        continue
    
    #print(Profile_name)
    ErrorCount=0

    #get image url  of profile
    job_elems = (soup.find_all('img',  class_='img-responsive'))
    i=1
    img1url=''
    img2url=''
    img3url=''
    for z in job_elems:#iterrate through all images
        #print(z)
        #print(type(z))
        #print(z.attrs)
        #print(z.attrs['src'])
        if i==1:
            img1url=baseURL+z.attrs['src']
        elif i==2:
            img2url=baseURL+z.attrs['src']
        elif i==3:
            img3url=baseURL+z.attrs['src']
        else:
            break
        i=i+1
        #print('----')

    #job_elems = soup.find_all('h5', class_='col-md-6')
    job_elems = soup.find_all('h5')

    soup2=BeautifulSoup(str(job_elems),features="html.parser")
    #print(job_elems)
    h5List=list(soup2.find_all('h5'))

    #print(list(soup2.find_all('h5')))

    count =0
    tempList=[]
    tempList.append(URL)
    tempList.append(img1url)
    tempList.append(img2url)
    tempList.append(img3url)
    tempList.append(Profile_name)
    for xx in h5List:
        each_line=str(xx)
        transformed_line=each_line[each_line.find(':')+2:each_line.find('</h5>')].strip()

        tempList.append(transformed_line)
        
        #print(count)

        #tempList.append(tempList)
    #print('Loop Inner end')
    #print(tempList)
    

   #getting candidates DOB and Gender 
    #print('DOB:'+tempList[5])
    GENDER_CANDIDATE=tempList[6]
    #print('GENDER:'+GENDER_CANDIDATE)

    #converting string date to date obj
    DOB_CANDIDATE=time.strptime(tempList[5],"%d/%m/%Y")
    DOB_reference=time.strptime('01/01/1995','%d/%m/%Y') #chnage here if need to change reference DOB

    #print(DOB_CANDIDATE)
    #print(DOB_reference)

    #checking candidates dob is after 1995 or not and FEMALE if not exit.
    if DOB_CANDIDATE >= DOB_reference and GENDER_CANDIDATE== 'FEMALE':
         #print('Candidate is born after 1995 and female')
         pass
    else:
        #print('Candidate is born before 1995 or Male')
        continue

    finalList.append(tempList)
    tempList=[] #reset the templist here

#print('Loop outer end')
#print(finalList)



# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('8Apr22_fem_95-2.xlsx')
worksheet = workbook.add_worksheet()

# Some data we want to write to the worksheet.
expenses = (
    ['Rent', 1000],
    ['Gas',   100],
    ['Food',  300],
    ['Gym',    50],
)


# Start from the first cell. Rows and columns are zero indexed.
row = 0
col = 5


#write header  Profile_name
worksheet.write(row, col-5,'URL')
worksheet.write(row, col-4,'Img1')
worksheet.write(row, col-3,'Img2')
worksheet.write(row, col-2,'Img3')
worksheet.write(row, col-1,'Profile_name')
worksheet.write(row, col,'dob')
worksheet.write(row,col+1,'sex')
worksheet.write(row,col+2,'ht')
worksheet.write(row,col+3,'cast')
worksheet.write(row,col+4,'edu')
worksheet.write(row,col+5,'occu')
worksheet.write(row,col+6,'blood')
worksheet.write(row,col+7,'spec')
worksheet.write(row,col+8,'complexion')
worksheet.write(row,col+9,'gotra')
worksheet.write(row,col+10,'birthpalce')
worksheet.write(row,col+11,'mangal')
worksheet.write(row,col+12,'diet')
worksheet.write(row,col+13,'horo')
worksheet.write(row,col+14,'father')
worksheet.write(row,col+15,'mother')
worksheet.write(row,col+16,'brother')
worksheet.write(row,col+17,'sister')
worksheet.write(row,col+18,'mama')
worksheet.write(row,col+19,'relative')
worksheet.write(row,col+20,'parentResideIn')
worksheet.write(row,col+21,'native')
worksheet.write(row,col+22,'wealth')
worksheet.write(row,col+23,'ageDiffernce')
worksheet.write(row,col+24,'expeHT')
worksheet.write(row,col+25,'edu')
worksheet.write(row,col+26,'occ')
worksheet.write(row,col+27,'cast')
worksheet.write(row,col+28,'divor')
worksheet.write(row,col+29,'mangal')
worksheet.write(row,col+30,'prefCity')

#incrementing row after header
row = 1

# Iterate over the data and write it out row by row.
for URL,img1,img2,img3,Profile_name,dob,sex,ht,cast,edu,occu,blood,spec,complexion,gotra,birthpalce,mangal,diet,horo,father,mother,brother,sister,mama,relative,parentResideIn,native,wealth,ageDiffernce,expeHT,edu,occ,cast,divor,mangal,prefCity in (finalList):
    worksheet.write(row, col-5,URL)
    worksheet.write(row, col-4,img1)
    worksheet.write(row, col-3,img2)
    worksheet.write(row, col-2,img3)
    worksheet.write(row, col-1,Profile_name)
    worksheet.write(row, col,dob)
    worksheet.write(row,col+1,sex)
    worksheet.write(row,col+2,ht)
    worksheet.write(row,col+3,cast)
    worksheet.write(row,col+4,edu)
    worksheet.write(row,col+5,occu)
    worksheet.write(row,col+6,blood)
    worksheet.write(row,col+7,spec)
    worksheet.write(row,col+8,complexion)
    worksheet.write(row,col+9,gotra)
    worksheet.write(row,col+10,birthpalce)
    worksheet.write(row,col+11,mangal)
    worksheet.write(row,col+12,diet)
    worksheet.write(row,col+13,horo)
    worksheet.write(row,col+14,father)
    worksheet.write(row,col+15,mother)
    worksheet.write(row,col+16,brother)
    worksheet.write(row,col+17,sister)
    worksheet.write(row,col+18,mama)
    worksheet.write(row,col+19,relative)
    worksheet.write(row,col+20,parentResideIn)
    worksheet.write(row,col+21,native)
    worksheet.write(row,col+22,wealth)
    worksheet.write(row,col+23,ageDiffernce)
    worksheet.write(row,col+24,expeHT)
    worksheet.write(row,col+25,edu)
    worksheet.write(row,col+26,occ)
    worksheet.write(row,col+27,cast)
    worksheet.write(row,col+28,divor)
    worksheet.write(row,col+29,mangal)
    worksheet.write(row,col+30,prefCity)

    row += 1

worksheet.write(row,0,str(ErroredURL))
workbook.close()
print(ErroredURL)

'''
