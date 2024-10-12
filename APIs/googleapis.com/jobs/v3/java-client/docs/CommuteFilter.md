

# CommuteFilter

Input only. Parameters needed for commute search.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowImpreciseAddresses** | **Boolean** | Optional. If true, jobs without \&quot;precise\&quot; addresses (street level addresses or GPS coordinates) might also be returned. For city and coarser level addresses, text matching is used. If this field is set to false or is not specified, only jobs that include precise addresses are returned by Commute Search. Note: If &#x60;allow_imprecise_addresses&#x60; is set to true, Commute Search is not able to calculate accurate commute times to jobs with city level and coarser address information. Jobs with imprecise addresses will return a &#x60;travel_duration&#x60; time of 0 regardless of distance from the job seeker. |  [optional] |
|**commuteMethod** | [**CommuteMethodEnum**](#CommuteMethodEnum) | Required. The method of transportation for which to calculate the commute time. |  [optional] |
|**departureTime** | [**TimeOfDay**](TimeOfDay.md) |  |  [optional] |
|**roadTraffic** | [**RoadTrafficEnum**](#RoadTrafficEnum) | Optional. Specifies the traffic density to use when calculating commute time. |  [optional] |
|**startCoordinates** | [**LatLng**](LatLng.md) |  |  [optional] |
|**travelDuration** | **String** | Required. The maximum travel time in seconds. The maximum allowed value is &#x60;3600s&#x60; (one hour). Format is &#x60;123s&#x60;. |  [optional] |



## Enum: CommuteMethodEnum

| Name | Value |
|---- | -----|
| COMMUTE_METHOD_UNSPECIFIED | &quot;COMMUTE_METHOD_UNSPECIFIED&quot; |
| DRIVING | &quot;DRIVING&quot; |
| TRANSIT | &quot;TRANSIT&quot; |



## Enum: RoadTrafficEnum

| Name | Value |
|---- | -----|
| ROAD_TRAFFIC_UNSPECIFIED | &quot;ROAD_TRAFFIC_UNSPECIFIED&quot; |
| TRAFFIC_FREE | &quot;TRAFFIC_FREE&quot; |
| BUSY_HOUR | &quot;BUSY_HOUR&quot; |



