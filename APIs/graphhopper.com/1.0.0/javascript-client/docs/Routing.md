# GraphHopperDirectionsApi.Routing

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calcPoints** | **Boolean** | It lets you specify whether the API should provide you with route geometries for vehicle routes or not. Thus, you do not need to do extra routing to get the polyline for each route. | [optional] [default to false]
**considerTraffic** | **Boolean** | indicates whether historical traffic information should be considered | [optional] [default to false]
**curbsideStrictness** | **String** | In some cases curbside constraints cannot be fulfilled. For example in one-way streets you cannot arrive at a building that is on the left side of the street such that the building is to the right of you (unless you drove the one-way street the wrong/illegal way). You can set the &#x60;curbside_strictness&#x60; to &#x60;soft&#x60; to ignore the curbside constraint in such cases or set it to &#x60;strict&#x60; to get an error response instead. You can also set it to &#x60;ignore&#x60; to ignore all curbside constraints (this is useful to compare the results with and without constraints without modifying every single address). | [optional] [default to &#39;soft&#39;]
**failFast** | **Boolean** | indicates whether matrix calculation should fail fast when points cannot be connected | [optional] [default to true]
**networkDataProvider** | **String** | specifies the data provider, read more about it [here](#section/Map-Data-and-Routing-Profiles). | [optional] [default to &#39;openstreetmap&#39;]
**returnSnappedWaypoints** | **Boolean** | Indicates whether a solution includes snapped waypoints. In contrary to the address coordinate a snapped waypoint is the access point to the (road) network. | [optional] [default to false]
**snapPreventions** | **[String]** | Prevents snapping locations to road links of specified road types, e.g. to motorway. | [optional] 



## Enum: CurbsideStrictnessEnum


* `ignore` (value: `"ignore"`)

* `soft` (value: `"soft"`)

* `strict` (value: `"strict"`)





## Enum: NetworkDataProviderEnum


* `openstreetmap` (value: `"openstreetmap"`)

* `tomtom` (value: `"tomtom"`)





## Enum: [SnapPreventionsEnum]


* `motorway` (value: `"motorway"`)

* `trunk` (value: `"trunk"`)

* `bridge` (value: `"bridge"`)

* `ford` (value: `"ford"`)

* `tunnel` (value: `"tunnel"`)

* `ferry` (value: `"ferry"`)




