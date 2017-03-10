
class Car(object):

    def __init__(self, price, speed, fuel, mileage, tax=.12):
        self.price = price
        self.speed = speed
        self.fuel= fuel
        self.mileage = mileage
        self.tax = tax
        if self.price > 10001:
            self.tax = .15
        self.display_all()

    def display_all(self):
        print 'Price: ' + str(self.price)
        print 'Speed: ' + str(self.speed)
        print 'Fuel: ' + str(self.fuel)
        print 'Mileage: ' + str(self.mileage)
        print 'Tax: ' + str(self.tax)
        print ' '


# newCar = Car(9000, 150, 50, 2454, car.tax)
# print newCar.price, newCar.speed. newCar.fuel, newCar.milage, newCar.tax
newCar1 = Car(12000, 140, 50, 34555)
newCar2 = Car(9000, 120, 60, 83485)
newCar3 = Car(15000, 110, 40, 99345)
newCar4 = Car(8000, 150, 80, 76544)
newCar5 = Car(8700, 180, 60, 84680)
newCar6 = Car(9800, 120, 50, 25466)
