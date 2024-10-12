# StorSimple8000SeriesManagementClient.Metrics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dimensions** | [**[MetricDimension]**](MetricDimension.md) | The metric dimensions. | [optional] 
**endTime** | **Date** | The end time of the metric data. | [optional] 
**name** | [**MetricName**](MetricName.md) |  | [optional] 
**primaryAggregation** | **String** | The metric aggregation type. | [optional] 
**resourceId** | **String** | The ID of metric source. | [optional] 
**startTime** | **Date** | The start time of the metric data. | [optional] 
**timeGrain** | **String** | The time granularity of the metric data. | [optional] 
**type** | **String** | The type of the metric data. | [optional] 
**unit** | **String** | The unit of the metric data. | [optional] 
**values** | [**[MetricData]**](MetricData.md) | The list of the metric data. | [optional] 



## Enum: PrimaryAggregationEnum


* `Average` (value: `"Average"`)

* `Last` (value: `"Last"`)

* `Maximum` (value: `"Maximum"`)

* `Minimum` (value: `"Minimum"`)

* `None` (value: `"None"`)

* `Total` (value: `"Total"`)





## Enum: UnitEnum


* `Bytes` (value: `"Bytes"`)

* `BytesPerSecond` (value: `"BytesPerSecond"`)

* `Count` (value: `"Count"`)

* `CountPerSecond` (value: `"CountPerSecond"`)

* `Percent` (value: `"Percent"`)

* `Seconds` (value: `"Seconds"`)




