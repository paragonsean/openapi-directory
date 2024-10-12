# TransportForLondonUnifiedApi.TflApiPresentationEntitiesCycleSuperhighway

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geography** | [**SystemDataSpatialDbGeography**](SystemDataSpatialDbGeography.md) |  | [optional] 
**id** | **String** | The Id | [optional] 
**label** | **String** | The long label to show on maps when zoomed in | [optional] 
**labelShort** | **String** | The short label to show on maps | [optional] 
**modified** | **Date** | When the data was last updated | [optional] 
**routeType** | **String** | Type of cycle route e.g CycleSuperhighways, Quietways, MiniHollands etc | [optional] 
**segmented** | **Boolean** | True if the route is split into segments | [optional] 
**status** | **String** | Cycle route status i.e Proposed, Existing etc | [optional] 



## Enum: RouteTypeEnum


* `Unknown` (value: `"Unknown"`)

* `All` (value: `"All"`)

* `Cycle Superhighways` (value: `"Cycle Superhighways"`)

* `Quietways` (value: `"Quietways"`)

* `Cycleways` (value: `"Cycleways"`)

* `Mini-Hollands` (value: `"Mini-Hollands"`)

* `Central London Grid` (value: `"Central London Grid"`)

* `Streetspace Route` (value: `"Streetspace Route"`)





## Enum: StatusEnum


* `Unknown` (value: `"Unknown"`)

* `All` (value: `"All"`)

* `Open` (value: `"Open"`)

* `In Progress` (value: `"In Progress"`)

* `Planned` (value: `"Planned"`)

* `Planned - Subject to feasibility and consultation.` (value: `"Planned - Subject to feasibility and consultation."`)

* `Not Open` (value: `"Not Open"`)




