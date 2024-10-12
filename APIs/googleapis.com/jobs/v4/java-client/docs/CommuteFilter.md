

# CommuteFilter

Parameters needed for commute search.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowImpreciseAddresses** | **Boolean** | If &#x60;true&#x60;, jobs without street level addresses may also be returned. For city level addresses, the city center is used. For state and coarser level addresses, text matching is used. If this field is set to &#x60;false&#x60; or isn&#39;t specified, only jobs that include street level addresses will be returned by commute search. |  [optional] |
|**commuteMethod** | [**CommuteMethodEnum**](#CommuteMethodEnum) | Required. The method of transportation to calculate the commute time for. |  [optional] |
|**departureTime** | [**TimeOfDay**](TimeOfDay.md) |  |  [optional] |
|**roadTraffic** | [**RoadTrafficEnum**](#RoadTrafficEnum) | Specifies the traffic density to use when calculating commute time. |  [optional] |
|**startCoordinates** | [**LatLng**](LatLng.md) |  |  [optional] |
|**travelDuration** | **String** | Required. The maximum travel time in seconds. The maximum allowed value is &#x60;3600s&#x60; (one hour). Format is &#x60;123s&#x60;. |  [optional] |



## Enum: CommuteMethodEnum

| Name | Value |
|---- | -----|
| COMMUTE_METHOD_UNSPECIFIED | &quot;COMMUTE_METHOD_UNSPECIFIED&quot; |
| DRIVING | &quot;DRIVING&quot; |
| TRANSIT | &quot;TRANSIT&quot; |
| WALKING | &quot;WALKING&quot; |
| CYCLING | &quot;CYCLING&quot; |
| TRANSIT_ACCESSIBLE | &quot;TRANSIT_ACCESSIBLE&quot; |



## Enum: RoadTrafficEnum

| Name | Value |
|---- | -----|
| ROAD_TRAFFIC_UNSPECIFIED | &quot;ROAD_TRAFFIC_UNSPECIFIED&quot; |
| TRAFFIC_FREE | &quot;TRAFFIC_FREE&quot; |
| BUSY_HOUR | &quot;BUSY_HOUR&quot; |



