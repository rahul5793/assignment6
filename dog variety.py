#Assignment 2
             
# 1. Create a class named ‘Dog’. It should have a constructor which accepts its name, age and coat color. You must perform the following operations:



#Solution :- 

class Dog:
    def _init_(self,name,age,coat_color):
        self.name = name    
        self.age  = age
        self.coat_color = coat_color

    
    def description(self):
        return f"Name : {self.name} \n Age : {self.age}"

    def get_info(self):
        return f"Coat Color : {self.coat_color}"

    

class jackrusselterrior(Dog):
    def _init_(self,name,age,coat_color,gender,birth_place):
        super()._init_(name,age,coat_color)
        self.gender = gender
        self.birth_place = birth_place

        
    def _str_(self):
            return f"\njackrusselterrior_name  :  {self.name}, \njackrusselterrior_age : {self.age}, \njackrusselterrior_coat_color : {self.coat_color}, \njackrusselterrior_gender : {self.gender}, \njackrusselterrior_birth_place : {self.birth_place}"

class Bulldog(Dog):
    def _init_(self,name,age,coat_color,prize,quality):
        super()._init_(name,age,coat_color)
        self.prize = prize
        self.quality = quality

    def _str_(self):
            return f"\nBulldog_name :  {self.name}, \nBulldog_age : {self.age}, \nBulldog_coat_color : {self.coat_color}, \nBulldog_prize  : {self.prize}, \nBulldog_Quality : {self.quality}"
        


jackrusselterrior_name = input("Enter a jackrusselterrior_name :- ")
jackrusselterrior_age = int(input("Enter the age :- "))
jackrusselterrior_coat_color = input("Enter a coat_color :- ")
jackrusselterrior_gender = input("Enter gender :- ")
jackrusselterrior_birth_place = input("Enter birth_place:- ")
Bulldog_name = input("Enter a Bulldog_name :- ")
Bulldog_age =  int(input("Enter the age :- "))
Bulldog_coat_color = input("Enter a coat_color :- ")
Bulldog_prize = input("Enter prize :- ")
Bulldog_Quality = input("Enter Quality:- ")




jackrusselterrior_obj = jackrusselterrior(jackrusselterrior_name,jackrusselterrior_age,jackrusselterrior_coat_color,jackrusselterrior_gender,jackrusselterrior_birth_place)
print(jackrusselterrior_obj)

print()
print()

Bulldog_obj = Bulldog(Bulldog_name,Bulldog_age,Bulldog_coat_color,Bulldog_prize,Bulldog_Quality)
print(Bulldog_obj)