# PtvTimetableApiVersion3.V3ResultStop

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**routeType** | **Number** | Transport mode identifier | [optional] 
**routes** | [**[V3ResultRoute]**](V3ResultRoute.md) | List of routes travelling through the stop | [optional] 
**stopDistance** | **Number** | Distance of stop from input location (in metres); returns 0 if no location is input | [optional] 
**stopId** | **Number** | Stop identifier | [optional] 
**stopLandmark** | **String** | Landmark in proximity of stop | [optional] 
**stopLatitude** | **Number** | Geographic coordinate of latitude at stop | [optional] 
**stopLongitude** | **Number** | Geographic coordinate of longitude at stop | [optional] 
**stopName** | **String** | Name of stop | [optional] 
**stopSequence** | **Number** | Sequence of the stop on the route/run; return 0 when route_id or run_id not specified. Order ascendingly by this field (when non zero) to get physical order (earliest first) of stops on the route_id/run_id. | [optional] 
**stopSuburb** | **String** | suburb of stop | [optional] 


