

# V3StopOnRoute


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**disruptionIds** | **List&lt;Long&gt;** | Disruption information identifier(s) |  [optional] |
|**routeType** | **Integer** | Transport mode identifier |  [optional] |
|**stopId** | **Integer** | Stop identifier |  [optional] |
|**stopLandmark** | **String** | Landmark in proximity of stop |  [optional] |
|**stopLatitude** | **Float** | Geographic coordinate of latitude at stop |  [optional] |
|**stopLongitude** | **Float** | Geographic coordinate of longitude at stop |  [optional] |
|**stopName** | **String** | Name of stop |  [optional] |
|**stopSequence** | **Integer** | Sequence of the stop on the route/run; return 0 when route_id or run_id not specified. Order ascendingly by this field (when non zero) to get physical order (earliest first) of stops on the route_id/run_id. |  [optional] |
|**stopSuburb** | **String** | suburb of stop |  [optional] |
|**stopTicket** | [**V3StopTicket**](V3StopTicket.md) |  |  [optional] |



