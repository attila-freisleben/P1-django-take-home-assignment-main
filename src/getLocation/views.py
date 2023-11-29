from django.http import JsonResponse
from getLocation.getData import fetchLocation

# Create your views here.

def index(request):
    print(request)
    response, statusCode = fetchLocation(request.GET.get('Lat'), request.GET.get('Lon'),  request.GET.get('FacilityType'), request.GET.get('Top'))
    return JsonResponse(data=response, safe=False, status=statusCode)
