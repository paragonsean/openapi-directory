# PtvTimetableApiVersion3.V3BulkDeparturesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dateUtc** | **Date** | Filter by the date and time of the request (ISO 8601 UTC format) (default &#x3D; current date and time) | [optional] 
**expand** | **[String]** | List objects to be returned in full (i.e. expanded) - options include: all, stop, route, run, direction, disruption, none | [optional] 
**includeCancelled** | **Boolean** | Indicates if cancelled services (if they exist) are returned (default &#x3D; false) - metropolitan train only | [optional] 
**includeGeopath** | **Boolean** | Indicates if the route geopath should be returned | [optional] 
**lookBackwards** | **Boolean** | Indicates if filtering runs (and their departures) to those that arrive at destination before date_utc (default &#x3D; false). Requires max_results &amp;gt; 0. | [optional] 
**requests** | [**[V3StopDepartureRequest]**](V3StopDepartureRequest.md) | Collection of departure requests | 



## Enum: [ExpandEnum]


* `All` (value: `"All"`)

* `Stop` (value: `"Stop"`)

* `Route` (value: `"Route"`)

* `Run` (value: `"Run"`)

* `Direction` (value: `"Direction"`)

* `Disruption` (value: `"Disruption"`)

* `VehicleDescriptor` (value: `"VehicleDescriptor"`)

* `VehiclePosition` (value: `"VehiclePosition"`)

* `None` (value: `"None"`)




