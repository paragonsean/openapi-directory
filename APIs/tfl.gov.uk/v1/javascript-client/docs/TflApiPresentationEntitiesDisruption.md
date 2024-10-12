# TransportForLondonUnifiedApi.TflApiPresentationEntitiesDisruption

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalInfo** | **String** | Gets or sets the additionaInfo of this disruption. | [optional] 
**affectedRoutes** | [**[TflApiPresentationEntitiesDisruptedRoute]**](TflApiPresentationEntitiesDisruptedRoute.md) | Gets or sets the routes affected by this disruption | [optional] 
**affectedStops** | [**[TflApiPresentationEntitiesStopPoint]**](TflApiPresentationEntitiesStopPoint.md) | Gets or sets the stops affected by this disruption | [optional] 
**category** | **String** | Gets or sets the category of this dispruption. | [optional] 
**categoryDescription** | **String** | Gets or sets the description of the category. | [optional] 
**closureText** | **String** | Text describing the closure type | [optional] 
**created** | **Date** | Gets or sets the date/time when this disruption was created. | [optional] 
**description** | **String** | Gets or sets the description of this disruption. | [optional] 
**lastUpdate** | **Date** | Gets or sets the date/time when this disruption was last updated. | [optional] 
**summary** | **String** | Gets or sets the summary of this disruption. | [optional] 
**type** | **String** | Gets or sets the disruption type of this dispruption. | [optional] 



## Enum: CategoryEnum


* `Undefined` (value: `"Undefined"`)

* `RealTime` (value: `"RealTime"`)

* `PlannedWork` (value: `"PlannedWork"`)

* `Information` (value: `"Information"`)

* `Event` (value: `"Event"`)

* `Crowding` (value: `"Crowding"`)

* `StatusAlert` (value: `"StatusAlert"`)




