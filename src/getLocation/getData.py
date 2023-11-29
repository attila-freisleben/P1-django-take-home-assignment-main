import geopy.distance
import pandas as pd
import json
import datetime as dt


def fetchLocation(Lat=None, Lon=None, FacilityType=None, Top=None):
    if Lat is None:
        Lat = '37.78844615690132'
    if Lon is None:
        Lon = '122.3986412420388'
    if FacilityType is None:
        FacilityType = ["Truck"]
    if Top is None:
        Top = 5
    else:
        Top = int(Top)

    try:
        df = pd.read_csv(r"https://raw.githubusercontent.com/RAKT-Innovations/P1-django-take-home-assignment/main/food-truck-data.csv")
        # use Location instead of Lat/long, should yield the same results
        # clean Location field so geopy accepts it, make a copy to coords

        #filter Status
        df = df[df['Status'].isin(['APPROVED', 'ISSUED'])]

        #filter FacilityType
        df = df[df['FacilityType'].isin(FacilityType)]

        clean = str.maketrans(dict.fromkeys('(),'))
        df["coords"] = df['Location'].map(lambda x: x.translate(clean))

        # use geopy to calculate distance
        df['distanceKM'] = df['coords'].map(lambda x: geopy.distance.geodesic(f'{Lat} {Lon}', x).km)

        #filter Top (closest by geocoord) results
        dfs = df.sort_values('distanceKM').head(Top)
        #return as JSON
        results = json.loads(dfs.to_json(orient='records'))

        statusCode = 200
    except Exception as e:
        now = dt.datetime.now()
        #some error info for logging
        print(f'error: {now:%Y-%m-%d %H:%I:%S} ', e)
        #public error message
        results = {"error" : "Something awful happened"}
        statusCode = 500

    return results, statusCode


