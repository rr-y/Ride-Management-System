from django.db import models
from django.utils import timezone
# Create your models here.


class DriverInfo(models.Model):
    '''
        attributes like
        driver name
        drive address

    '''
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Cab(models.Model):
    '''
    attributes
        car number
        car model
        car name
        refrence point -> particular driver
    '''
    car_number = models.CharField(max_length=20)
    car_model = models.CharField(max_length=20)
    car_name = models.CharField(max_length=20)
    driver = models.ForeignKey(DriverInfo.name, on_delete = models.CASCADE)


    def __str__(self):
        return self.car_name +" "+self.car_model


class PassengerInfo(models.Model):
    '''
            attributes like
            passenger name
            passenger address
            and more

    '''
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Ride(models.Model):
    '''
        start location
        end location
        refereces -> driver, passenger
        time
        active -> current ride is active or not
    '''
    start_location = models.CharField(max_length=100)
    end_location = models.CharField(max_length= 100)
    driver_name = models.ForeignKey(DriverInfo.name, on_delete=models.CASCADE)
    passenger_name = models.ForeignKey(PassengerInfo.name, on_delete=models.CASCADE)
    ride_start_time = models.DateTimeField(default=timezone.now())
    active = models.BooleanField(default=True)
    end_time = models.DateTimeField(null=True)

    def mark_completed(self):

        if not self.active:
            self.end_time = timezone.now()
            self.save()

    def __str__(self):
        return self.start_location+" "+self.end_location+ " "+ self.driver_name


class CabAvailableModel(models.Model):
    '''
        location ->
        num of cabs available
    '''

    location = models.CharField(max_length=200)
    num_cab = models.IntegerField()
