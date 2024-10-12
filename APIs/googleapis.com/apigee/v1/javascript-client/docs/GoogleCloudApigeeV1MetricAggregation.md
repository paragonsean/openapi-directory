# ApigeeApi.GoogleCloudApigeeV1MetricAggregation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregation** | **String** | Aggregation function associated with the metric. | [optional] 
**name** | **String** | Name of the metric | [optional] 
**order** | **String** | Ordering for this aggregation in the result. For time series this is ignored since the ordering of points depends only on the timestamp, not the values. | [optional] 



## Enum: AggregationEnum


* `AGGREGATION_FUNCTION_UNSPECIFIED` (value: `"AGGREGATION_FUNCTION_UNSPECIFIED"`)

* `AVG` (value: `"AVG"`)

* `SUM` (value: `"SUM"`)

* `MIN` (value: `"MIN"`)

* `MAX` (value: `"MAX"`)

* `COUNT_DISTINCT` (value: `"COUNT_DISTINCT"`)





## Enum: OrderEnum


* `ORDER_UNSPECIFIED` (value: `"ORDER_UNSPECIFIED"`)

* `ASCENDING` (value: `"ASCENDING"`)

* `DESCENDING` (value: `"DESCENDING"`)




