# PtvTimetableApiVersion3.V3RouteDeparturesSpecificParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dateUtc** | **Date** | Filter by the date and time of the request (ISO 8601 UTC format) (default &#x3D; current date and time) | [optional] 
**expand** | **[String]** | List of objects to be returned in full (i.e. expanded) - options include: All, Stop, Route, Run, Direction, Disruption, VehiclePosition, VehicleDescriptor or None.              Run must be expanded to receive VehiclePosition and VehicleDescriptor information. | [optional] 
**includeCancelled** | **Boolean** | Indicates if cancelled services (if they exist) are returned (default &#x3D; false) - metropolitan train only | [optional] 
**includeGeopath** | **Boolean** | Indicates if the route geopath should be returned | [optional] 
**lookBackwards** | **Boolean** | Indicates if filtering runs (and their departures) to those that arrive at destination before date_utc (default &#x3D; false). Requires max_results &amp;gt; 0. | [optional] 
**maxResults** | **Number** | Maximum number of results returned | [optional] 
**scheduledTimetables** | **Boolean** | When set to true, all timetable information returned by Chronos will be sourced from the scheduled timetables,              while when set to false (default state), the operational timetables will be used where available. | [optional] 
**trainScheduledTimetables** | **Boolean** | DEPRECATED - use &#x60;scheduled_timetables&#x60; instead | [optional] 



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




