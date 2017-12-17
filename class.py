# Lets start with class

class HumanBeing():
    name   = 'ashish'
    gender = 'male'

instance = HumanBeing()

print(instance.name)












name = 'ash'
gender = 'male'
class HumanBeing1():
    def __init__(self, name, gender):
        
        self.name   = name
        self.gender = gender    


instance = HumanBeing1(name,gender)
print(instance.name)    
    