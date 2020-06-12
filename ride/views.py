from django.shortcuts import render, get_object_or_404
from .models import CabAvailableModel
from .models import Ride
from django.utils import timezone
# Create your views here.

'''
This class will give all available cab details given that location
@:param -> location
@:return -> cab detail object

'''


class CabAvailability:

    def __init__(self, location):
        self.location = location

    def available_cab(self):
        obj = CabAvailableModel.objects.get(location=self.location)
        if obj == None:
            return None
        return obj


def free_cab(self, cab_obj):
    # free the cab and add the cab at end location
    pass


'''
@:param -> request made for a ride
@:return -> allocate ride or not
'''


def ride_view(request):
    start_location = request['start_location']
    end_location = request['end_location']
    start_time = request['start_time']

    #find the cab which is near to the start location
    cab_obj = CabAvailability(start_location)
    if not cab_obj:
        return render(request, "no cab availabe right now", {})

    #if cab is available then  create a ride object
    dict_key = {}
    ride_obj = Ride.objects.create(dict_key)
    ride_obj.save()
    info = {}
    return render(request, "your cab is on the way", info)


def ride_complete_view(request, pk):
    if request.is_completed:
        obj = get_object_or_404(Ride, pk=pk)
        obj.end_time = timezone.now()
        obj.save()
        free_cab()
        # redirect to the home page











