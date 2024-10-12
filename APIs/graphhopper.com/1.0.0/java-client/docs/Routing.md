

# Routing

This contains all routing specific configurations.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**calcPoints** | **Boolean** | It lets you specify whether the API should provide you with route geometries for vehicle routes or not. Thus, you do not need to do extra routing to get the polyline for each route. |  [optional] |
|**considerTraffic** | **Boolean** | indicates whether historical traffic information should be considered |  [optional] |
|**curbsideStrictness** | [**CurbsideStrictnessEnum**](#CurbsideStrictnessEnum) | In some cases curbside constraints cannot be fulfilled. For example in one-way streets you cannot arrive at a building that is on the left side of the street such that the building is to the right of you (unless you drove the one-way street the wrong/illegal way). You can set the &#x60;curbside_strictness&#x60; to &#x60;soft&#x60; to ignore the curbside constraint in such cases or set it to &#x60;strict&#x60; to get an error response instead. You can also set it to &#x60;ignore&#x60; to ignore all curbside constraints (this is useful to compare the results with and without constraints without modifying every single address). |  [optional] |
|**failFast** | **Boolean** | indicates whether matrix calculation should fail fast when points cannot be connected |  [optional] |
|**networkDataProvider** | [**NetworkDataProviderEnum**](#NetworkDataProviderEnum) | specifies the data provider, read more about it [here](#section/Map-Data-and-Routing-Profiles). |  [optional] |
|**returnSnappedWaypoints** | **Boolean** | Indicates whether a solution includes snapped waypoints. In contrary to the address coordinate a snapped waypoint is the access point to the (road) network. |  [optional] |
|**snapPreventions** | [**List&lt;SnapPreventionsEnum&gt;**](#List&lt;SnapPreventionsEnum&gt;) | Prevents snapping locations to road links of specified road types, e.g. to motorway. |  [optional] |



## Enum: CurbsideStrictnessEnum

| Name | Value |
|---- | -----|
| IGNORE | &quot;ignore&quot; |
| SOFT | &quot;soft&quot; |
| STRICT | &quot;strict&quot; |



## Enum: NetworkDataProviderEnum

| Name | Value |
|---- | -----|
| OPENSTREETMAP | &quot;openstreetmap&quot; |
| TOMTOM | &quot;tomtom&quot; |



## Enum: List&lt;SnapPreventionsEnum&gt;

| Name | Value |
|---- | -----|
| MOTORWAY | &quot;motorway&quot; |
| TRUNK | &quot;trunk&quot; |
| BRIDGE | &quot;bridge&quot; |
| FORD | &quot;ford&quot; |
| TUNNEL | &quot;tunnel&quot; |
| FERRY | &quot;ferry&quot; |



