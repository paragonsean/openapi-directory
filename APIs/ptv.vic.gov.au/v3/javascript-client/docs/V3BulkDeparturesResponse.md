# PtvTimetableApiVersion3.V3BulkDeparturesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**directions** | [**[V3Direction]**](V3Direction.md) | Directions of travel of route | [optional] 
**disruptions** | [**{String: V3Disruption}**](V3Disruption.md) | Disruption information applicable to relevant routes or stops | [optional] 
**responses** | [**[V3BulkDeparturesUpdateResponse]**](V3BulkDeparturesUpdateResponse.md) | Contains departures for the requested stop and route(s). It includes details as to the route_direction and whether it is still valid. | [optional] 
**routes** | **[Object]** | Train lines, tram routes, bus routes, regional coach routes, Night Bus routes | [optional] 
**runs** | [**[V3Run]**](V3Run.md) | Individual trips/services of a route | [optional] 
**status** | [**V3Status**](V3Status.md) |  | [optional] 
**stops** | [**{String: V3BulkDeparturesStopResponse}**](V3BulkDeparturesStopResponse.md) | A train station, tram stop, bus stop, regional coach stop or Night Bus stop | [optional] 


