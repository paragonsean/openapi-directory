# PtvTimetableApiVersion3.V3StopDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disruptionIds** | **[Number]** | Disruption information identifier(s) | [optional] 
**routeType** | **Number** | Transport mode identifier | [optional] 
**routes** | **[Object]** | Routes travelling through the stop | [optional] 
**stationDescription** | **String** | The definition applicable to the station_type; returns null for V/Line train | [optional] 
**stationType** | **String** | Type of metropolitan train station (i.e. \&quot;Premium\&quot;, \&quot;Host\&quot; or \&quot;Unstaffed\&quot; station); returns null for V/Line train | [optional] 
**stopAccessibility** | [**V3StopAccessibility**](V3StopAccessibility.md) |  | [optional] 
**stopAmenities** | [**V3StopAmenityDetails**](V3StopAmenityDetails.md) |  | [optional] 
**stopId** | **Number** | Stop identifier | [optional] 
**stopLandmark** | **String** | Landmark in proximity of stop | [optional] 
**stopLocation** | [**V3StopLocation**](V3StopLocation.md) |  | [optional] 
**stopName** | **String** | Name of stop | [optional] 
**stopStaffing** | [**V3StopStaffing**](V3StopStaffing.md) |  | [optional] 


