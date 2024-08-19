# StorSimpleManagementClient.MetricDefinition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dimensions** | [**[MetricDimension]**](MetricDimension.md) | The supported dimensions | 
**metricAvailabilities** | [**[MetricAvailablity]**](MetricAvailablity.md) | The available metric granularities | 
**name** | [**MetricName**](MetricName.md) |  | 
**primaryAggregationType** | **String** | The metric aggregation type | 
**resourceId** | **String** | The metric source id | 
**type** | **String** | The metric definition type | 
**unit** | **String** | The metric unit | 



## Enum: PrimaryAggregationTypeEnum


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




