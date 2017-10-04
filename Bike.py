class Bike(object):
    def __init__(this, price, max_speed):
        this.price = price
        this.max_speed = max_speed
        this.miles = 0
    def displayInfo(this):
        print "Price: $" + str(this.price)
        print "Max speed: " + str(this.max_speed) + "mph"
        print "This bike has been ridden for " + str(abs(this.miles)) + " miles"
    def ride(this):
        print "Riding the bike..."
        this.miles += 10
    def reverse(this):
        print "Reversing..."
        this.miles -= 5

sports = Bike(1500, 25)
mountain = Bike(1250, 15)
rec = Bike(500, 15)
sports.displayInfo()
print
sports.ride()
sports.displayInfo()
print
sports.reverse()
mountain.ride()
mountain.ride()
mountain.displayInfo()
print
sports.displayInfo()