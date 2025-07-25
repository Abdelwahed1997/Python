from Person import Person 

class Employee(Person):

    def __init__(self, name, money, healthRate, mood, id, car, salary, distanceToWork, email):
        super().__init__(name, money, mood, healthRate)
        self.id = id
        self.car = car
        self.salary = salary
        self.distanceToWork = distanceToWork
        self.email = email

    def work(self, hours):
        if hours == 8:
            self.mood = "happy"
        elif hours < 8:
            self.mood = "lazy"
        else:
            self.mood = "tired"

    def drive(self, distance):
        self.car.run(distance, self.car.velocity)

    def refuel(self, gasAmount):
        self.car.fuelRate += gasAmount

    def send_mail(self, to, subject, body):
        print(f"Sending mail to: {to}")
        print(f"Subject: {subject}")
        print(f"Body: {body}")