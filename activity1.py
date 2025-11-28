#Activity 1: Multi Type Profile

#define the variables with values of different data types

Name = "John Doe" #String
Age = 28 #Integer
Skills = ["Python", "SQL", "Power BI"] #list
Education = ("BSc Computer Science", 2020) #tuple
ContactDetails = {"email": "Dilshani Senanayake", "phone": "0203445656563"} #dictionary
Certifications = {"Azure", "AWS", "Azure"} #set ,duplicates will be removed

Data = [Name, Age, Skills, Education, ContactDetails, Certifications]

print(*Data, sep='\n')