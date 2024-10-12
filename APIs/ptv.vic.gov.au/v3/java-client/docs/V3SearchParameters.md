

# V3SearchParameters


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**includeAddresses** | **Boolean** | Placeholder for future development; currently unavailable |  [optional] |
|**includeOutlets** | **Boolean** | Indicates if outlets will be returned in response (default &#x3D; true) |  [optional] |
|**latitude** | **Float** | Filter by geographic coordinate of latitude |  [optional] |
|**longitude** | **Float** | Filter by geographic coordinate of longitude |  [optional] |
|**matchRouteBySuburb** | **Boolean** | Indicates whether to find routes by suburbs in the search term (default &#x3D; true) |  [optional] |
|**matchStopByGtfsStopId** | **Boolean** | Indicates whether to search for stops according to a metlink stop ID (default &#x3D; false) |  [optional] |
|**matchStopBySuburb** | **Boolean** | Indicates whether to find stops by suburbs in the search term (default &#x3D; true) |  [optional] |
|**maxDistance** | **Float** | Filter by maximum distance (in metres) from location specified via latitude and longitude parameters |  [optional] |
|**routeTypes** | [**List&lt;RouteTypesEnum&gt;**](#List&lt;RouteTypesEnum&gt;) | Filter by route_type; values returned via RouteTypes API (note: stops and routes are ordered by route_types specified) |  [optional] |



## Enum: List&lt;RouteTypesEnum&gt;

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |
| NUMBER_3 | 3 |
| NUMBER_4 | 4 |



