

# TflApiPresentationEntitiesCycleSuperhighway



## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**geography** | [**SystemDataSpatialDbGeography**](SystemDataSpatialDbGeography.md) |  |  [optional] |
|**id** | **String** | The Id |  [optional] |
|**label** | **String** | The long label to show on maps when zoomed in |  [optional] |
|**labelShort** | **String** | The short label to show on maps |  [optional] |
|**modified** | **OffsetDateTime** | When the data was last updated |  [optional] |
|**routeType** | [**RouteTypeEnum**](#RouteTypeEnum) | Type of cycle route e.g CycleSuperhighways, Quietways, MiniHollands etc |  [optional] |
|**segmented** | **Boolean** | True if the route is split into segments |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Cycle route status i.e Proposed, Existing etc |  [optional] |



## Enum: RouteTypeEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| ALL | &quot;All&quot; |
| CYCLE_SUPERHIGHWAYS | &quot;Cycle Superhighways&quot; |
| QUIETWAYS | &quot;Quietways&quot; |
| CYCLEWAYS | &quot;Cycleways&quot; |
| MINI_HOLLANDS | &quot;Mini-Hollands&quot; |
| CENTRAL_LONDON_GRID | &quot;Central London Grid&quot; |
| STREETSPACE_ROUTE | &quot;Streetspace Route&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| ALL | &quot;All&quot; |
| OPEN | &quot;Open&quot; |
| IN_PROGRESS | &quot;In Progress&quot; |
| PLANNED | &quot;Planned&quot; |
| PLANNED_SUBJECT_TO_FEASIBILITY_AND_CONSULTATION_ | &quot;Planned - Subject to feasibility and consultation.&quot; |
| NOT_OPEN | &quot;Not Open&quot; |



