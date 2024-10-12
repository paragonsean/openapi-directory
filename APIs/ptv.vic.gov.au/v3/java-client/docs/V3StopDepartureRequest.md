

# V3StopDepartureRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**gtfs** | **Boolean** | Indicates that stop_id parameter will accept \&quot;GTFS stop_id\&quot; data and route_directions[x].route_id parameters will accept route_gtfs_id data |  [optional] |
|**maxResults** | **Integer** | Maximum number of results returned |  [optional] |
|**routeDirections** | [**List&lt;V3StopDepartureRequestRouteDirection&gt;**](V3StopDepartureRequestRouteDirection.md) | The route directions to find departures for at this stop. |  |
|**routeType** | [**RouteTypeEnum**](#RouteTypeEnum) | Number identifying transport mode; values returned via RouteTypes API |  [optional] |
|**stopId** | **Integer** | Identifier of stop; values returned by Stops API |  [optional] |



## Enum: RouteTypeEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |
| NUMBER_3 | 3 |
| NUMBER_4 | 4 |



