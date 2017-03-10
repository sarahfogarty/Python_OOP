
class Bike(object):

    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles

    def displayInfo(self):
        print '{}, {}, {}'.format(self.price, self.max_speed, self.miles)


# newBike= Bike(5, 6, 7)
# print newBike.price
# print newBike.max_speed
# print newBike.miles

    def Ride(self):
        print 'Riding - ' + (self.miles+10)

# newBike= Bike(5, 6, 7)
# print 'Riding: New mileage  =  ' + str((newBike.miles+10))

    def reverse(self):
        print 'Reversing - ' + (self.miles-5)

# newBike= Bike(5, 6, 7)
# print 'Reversing: New mileage =  ' + str((newBike.miles-5))

    def reverse(self):
        if self.miles > 5:
            print 'Reversing: New mileage =  ' + str((self.miles-5))
        else:
            print 'ERROR'
#
# newBike= Bike(5, 6, 4)
# if newBike.miles > 5:
#     print 'Reversing: New mileage =  ' + str((newBike.miles-5))
# else:
#     print 'ERROR'
