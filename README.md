**Simple GET endpoint for fetching nearby food trucks.**

`/getNearbyTrucks`


*Params*

 `Lat`: Latitude;
 `Lon`: Longitude coordinates to check

*Optional params*

`FacilityType` : ['Push Cart','Truck',''] as of now, consult [source data](https://raw.githubusercontent.com/RAKT-Innovations/P1-django-take-home-assignment/main/food-truck-data.csv) for possible values.
Default: Truck

`Top` : number of items to return, default 5


http://127.0.0.1:8000/getNearbyTrucks?Lat=37.61844615690132&Lon=-122.3986412420388


**Future improvement**

Specify walk/bike/car mode and calculate path distance instead of geo distance, that would translate better to real life.

**Install & run**

> pip install -r requirements.txt
> cd src
> python manage.py runserver
