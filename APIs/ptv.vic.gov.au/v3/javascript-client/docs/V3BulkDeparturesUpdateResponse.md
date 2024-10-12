# PtvTimetableApiVersion3.V3BulkDeparturesUpdateResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**departures** | [**[V3Departure]**](V3Departure.md) | Timetabled and real-time service departures | [optional] 
**requestedRouteDirection** | [**V3BulkDeparturesRouteDirectionResponse**](V3BulkDeparturesRouteDirectionResponse.md) |  | [optional] 
**routeDirection** | [**V3BulkDeparturesRouteDirectionResponse**](V3BulkDeparturesRouteDirectionResponse.md) |  | [optional] 
**routeDirectionStatus** | **Number** | The status of the route direction (changed | unchanged).              If changed, requests should change the requested_route_direction for the route_direction supplied. | [optional] 
**routeType** | **Number** | Transport mode identifier | [optional] 
**stopId** | **Number** | Stop identifier | [optional] 



## Enum: RouteDirectionStatusEnum


* `0` (value: `0`)

* `1` (value: `1`)




