import requests
from bs4 import BeautifulSoup
import csv

page = requests.get("http://velocity.uwaterloo.ca/companies/") #Fetches the page URL

soup = BeautifulSoup(page.content,'html.parser') #Parses the HTML Page using HTML Parser and displays the content

data = []

companies_html = soup.findAll('li',class_="js-company") #finding tags with <li> with classes <js-company>

for i in range(0,147,1): #147 companies
    company_info = companies_html[i] #indexing through html
    title_companies = company_info.find(class_="company-title companyTitle").get_text() #extracting title by specifying class and extracting it
    desc_companies = company_info.find("p",class_="").get_text() #extracting description of the companies
    enter_data = [title_companies,desc_companies] #entering data in the list
    data.append(enter_data)
    print ("Title of the Company: ", title_companies)
    print ("Description: ", desc_companies)
    
"""
This loop above indexes through the companies_html page
and extracts the title and the description of the companies.
It then uses the empty list and enters data in a singular 
fashion into the list.
"""

with open('velocity.csv','w') as file:
    writer = csv.writer(file)
    writer.writerows(data)

"""
We use csv module to write the contents of the list into 
a csv.
"""
