import requests
from bs4 import BeautifulSoup
import pandas
import csv

page = requests.get("http://velocity.uwaterloo.ca/companies/") #fetching page

page #checking response

soup = BeautifulSoup(page.content,'html.parser')

data = [] #defining empty list to add data about companies
#Parser
for i in range(0,147,1): #147 companies
    company_info = companies_html[i] #indexing through html
    title_companies = company_info.find(class_="company-title companyTitle").get_text() #extracting title by specifying class and extracting it
    desc_companies = company_info.find("p",class_="").get_text() #extracting description of the companies
    enter_data = [title_companies,desc_companies] #entering data in the list
    data.append(enter_data)
    print ("Title of the Company: ", title_companies)
    print ("Description: ", desc_companies)

#This loop enters data into the list for us to export to csv

with open('velocity.csv','w') as file:
    writer = csv.writer(file)
    writer.writerows(data)
    
#writes the data into a .csv file
