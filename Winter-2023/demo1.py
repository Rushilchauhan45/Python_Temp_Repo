#Describe different methods to make dictionary variable. (concept + short code)[3]

#Dictionary means the Key-value pair Data in python....

#Method 1: Using Curly Braces {}

student = {
    "name" : "Shyam" , 
    "age" : 18 , 
    "College" : "GECGN" , 
    "City" : "Gandhinagar",
    "Marks" : 90 
    }

#Method 2 : Using dict() function/Constructor

student1 = dict(name = "Ram" , 
                age = 19 ,
                College = "GECGN" ,
                City = "Gandhinagar",
                Marks = 85
                )

#Method 3 : Using With Tuple And List

student2 = dict([ 
  ("name","ghanshayam"),
  ("age",20),
  ("College","GECGN"),
  ("City","Gandhinagar"),
  ("Marks",88)
])

