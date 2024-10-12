# CloudTalentSolutionApi.CommuteFilter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowImpreciseAddresses** | **Boolean** | If &#x60;true&#x60;, jobs without street level addresses may also be returned. For city level addresses, the city center is used. For state and coarser level addresses, text matching is used. If this field is set to &#x60;false&#x60; or isn&#39;t specified, only jobs that include street level addresses will be returned by commute search. | [optional] 
**commuteMethod** | **String** | Required. The method of transportation to calculate the commute time for. | [optional] 
**departureTime** | [**TimeOfDay**](TimeOfDay.md) |  | [optional] 
**roadTraffic** | **String** | Specifies the traffic density to use when calculating commute time. | [optional] 
**startCoordinates** | [**LatLng**](LatLng.md) |  | [optional] 
**travelDuration** | **String** | Required. The maximum travel time in seconds. The maximum allowed value is &#x60;3600s&#x60; (one hour). Format is &#x60;123s&#x60;. | [optional] 



## Enum: CommuteMethodEnum


* `COMMUTE_METHOD_UNSPECIFIED` (value: `"COMMUTE_METHOD_UNSPECIFIED"`)

* `DRIVING` (value: `"DRIVING"`)

* `TRANSIT` (value: `"TRANSIT"`)

* `WALKING` (value: `"WALKING"`)

* `CYCLING` (value: `"CYCLING"`)

* `TRANSIT_ACCESSIBLE` (value: `"TRANSIT_ACCESSIBLE"`)





## Enum: RoadTrafficEnum


* `ROAD_TRAFFIC_UNSPECIFIED` (value: `"ROAD_TRAFFIC_UNSPECIFIED"`)

* `TRAFFIC_FREE` (value: `"TRAFFIC_FREE"`)

* `BUSY_HOUR` (value: `"BUSY_HOUR"`)




