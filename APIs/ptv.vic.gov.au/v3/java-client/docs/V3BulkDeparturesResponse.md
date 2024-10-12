

# V3BulkDeparturesResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**directions** | [**List&lt;V3Direction&gt;**](V3Direction.md) | Directions of travel of route |  [optional] |
|**disruptions** | [**Map&lt;String, V3Disruption&gt;**](V3Disruption.md) | Disruption information applicable to relevant routes or stops |  [optional] |
|**responses** | [**List&lt;V3BulkDeparturesUpdateResponse&gt;**](V3BulkDeparturesUpdateResponse.md) | Contains departures for the requested stop and route(s). It includes details as to the route_direction and whether it is still valid. |  [optional] |
|**routes** | **List&lt;Object&gt;** | Train lines, tram routes, bus routes, regional coach routes, Night Bus routes |  [optional] |
|**runs** | [**List&lt;V3Run&gt;**](V3Run.md) | Individual trips/services of a route |  [optional] |
|**status** | [**V3Status**](V3Status.md) |  |  [optional] |
|**stops** | [**Map&lt;String, V3BulkDeparturesStopResponse&gt;**](V3BulkDeparturesStopResponse.md) | A train station, tram stop, bus stop, regional coach stop or Night Bus stop |  [optional] |



