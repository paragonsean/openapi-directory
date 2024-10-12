# StorSimpleManagementClient.Metrics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dimensions** | [**[MetricDimension]**](MetricDimension.md) | The Metric dimension which indicates the source of the metric | 
**endTime** | **Date** | The metric end time | 
**name** | [**MetricName**](MetricName.md) |  | 
**primaryAggregation** | **String** | The metric aggregation type | 
**resourceId** | **String** | The id of metric source | 
**startTime** | **Date** | The metric start time | 
**timeGrain** | **String** | The time grain, time grain indicates frequency of the metric data | 
**type** | **String** | The Type of the metric data | 
**unit** | **String** | The unit of the metric data | 
**values** | [**[MetricData]**](MetricData.md) | The metric data | 



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




