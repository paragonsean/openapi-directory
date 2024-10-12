# StorSimple8000SeriesManagementClient.MetricDefinition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **String** | The category of the metric. | [optional] 
**dimensions** | [**[MetricDimension]**](MetricDimension.md) | The available metric dimensions. | [optional] 
**metricAvailabilities** | [**[MetricAvailablity]**](MetricAvailablity.md) | The available metric granularities. | [optional] 
**name** | [**MetricName**](MetricName.md) |  | [optional] 
**primaryAggregationType** | **String** | The metric aggregation type. | [optional] 
**resourceId** | **String** | The metric source ID. | [optional] 
**type** | **String** | The metric definition type. | [optional] 
**unit** | **String** | The metric unit. | [optional] 



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




