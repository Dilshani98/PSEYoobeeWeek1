
#define the variables with values

Name = "John Doe" #String Value
Age = 28 #Int Value
Skills = ["Python", "SQL", "Power BI"] #set
Education = ("BSc Computer Science", 2020) 
ContactDetails = {"email": "Dilshani Senanayake", "phone": "0203445656563"} #dict
Certifications = [
    ("Azure", "AWS", "Azure"), #this shouldn't be set
    {"Azure", "AWS"}
]

Data = [Name, Age, Skills, Education, ContactDetails, Certifications]

print(*Data, sep='\n')