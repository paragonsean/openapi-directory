# SchoolDiggerApiV20.APIBoundary12

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hasBoundary** | **Boolean** | States whether there is a boundary available | [optional] 
**polylineCollection** | [**[APIPolyline]**](APIPolyline.md) | Collection of one or more polylines that can be used to create the boundary on a map. NOTE: this value is JSON encoded. Specifically, backslashes will be returned escaped (two backslashes). Make sure to decode the polyline before you use it | [optional] 
**polylines** | **String** | Collection of latitude/longitude vertices to form a polygon representing the boundary | [optional] 


