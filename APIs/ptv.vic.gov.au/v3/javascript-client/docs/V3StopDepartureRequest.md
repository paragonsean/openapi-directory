# PtvTimetableApiVersion3.V3StopDepartureRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gtfs** | **Boolean** | Indicates that stop_id parameter will accept \&quot;GTFS stop_id\&quot; data and route_directions[x].route_id parameters will accept route_gtfs_id data | [optional] 
**maxResults** | **Number** | Maximum number of results returned | [optional] 
**routeDirections** | [**[V3StopDepartureRequestRouteDirection]**](V3StopDepartureRequestRouteDirection.md) | The route directions to find departures for at this stop. | 
**routeType** | **Number** | Number identifying transport mode; values returned via RouteTypes API | [optional] 
**stopId** | **Number** | Identifier of stop; values returned by Stops API | [optional] 



## Enum: RouteTypeEnum


* `0` (value: `0`)

* `1` (value: `1`)

* `2` (value: `2`)

* `3` (value: `3`)

* `4` (value: `4`)




