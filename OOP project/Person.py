class Person:
    def __init__(self,name,money,mood,healthRate):
        self.name = name
        self.money = money
        self.mood = mood
        self.healthRate = healthRate

    def sleep (self, hours):
        if hours == 7:
            self.mood = "Happy"
        elif hours < 7:
            self.mood = "Tired"
        elif hours > 7:
            self.mood = "Lazy"    


    def eat (self,meals):
        if meals == 3:
            self.healthRate = 100
        elif meals == 2:
            self.healthRate = 75
        elif meals == 1:
            self.healthRate = 50
            return self.healthRate        

    def buy (self,items):
        money = self.money  - items*10
        return money