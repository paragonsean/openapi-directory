# AzureSqlDatabase.TopQueries

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregationFunction** | **String** | The function that is used to aggregate each query&#39;s metrics. | [optional] [readonly] 
**executionType** | **String** | The execution type that is used to filter the query instances that are returned. | [optional] [readonly] 
**intervalType** | **String** | The duration of the interval (ISO8601 duration format). | [optional] [readonly] 
**numberOfTopQueries** | **Number** | The number of requested queries. | [optional] [readonly] 
**observationEndTime** | **Date** | The end time for queries that are returned (ISO8601 format) | [optional] [readonly] 
**observationStartTime** | **Date** | The start time for queries that are returned (ISO8601 format) | [optional] [readonly] 
**observedMetric** | **String** | The type of metric to use for ordering the top metrics. | [optional] [readonly] 
**queries** | [**[QueryStatistic]**](QueryStatistic.md) | The list of queries. | [optional] [readonly] 



## Enum: AggregationFunctionEnum


* `min` (value: `"min"`)

* `max` (value: `"max"`)

* `avg` (value: `"avg"`)

* `sum` (value: `"sum"`)





## Enum: ExecutionTypeEnum


* `any` (value: `"any"`)

* `regular` (value: `"regular"`)

* `irregular` (value: `"irregular"`)

* `aborted` (value: `"aborted"`)

* `exception` (value: `"exception"`)





## Enum: ObservedMetricEnum


* `cpu` (value: `"cpu"`)

* `io` (value: `"io"`)

* `logio` (value: `"logio"`)

* `duration` (value: `"duration"`)

* `executionCount` (value: `"executionCount"`)




