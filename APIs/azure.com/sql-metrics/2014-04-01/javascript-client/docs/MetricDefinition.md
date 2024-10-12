# AzureSqlDatabase.MetricDefinition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metricAvailabilities** | [**[MetricAvailability]**](MetricAvailability.md) | The list of database metric availabilities for the metric. | [optional] [readonly] 
**name** | [**MetricName**](MetricName.md) |  | [optional] 
**primaryAggregationType** | **String** | The primary aggregation type defining how metric values are displayed. | [optional] [readonly] 
**resourceUri** | **String** | The resource uri of the database. | [optional] [readonly] 
**unit** | **String** | The unit of the metric. | [optional] [readonly] 



## Enum: PrimaryAggregationTypeEnum


* `None` (value: `"None"`)

* `Average` (value: `"Average"`)

* `Count` (value: `"Count"`)

* `Minimum` (value: `"Minimum"`)

* `Maximum` (value: `"Maximum"`)

* `Total` (value: `"Total"`)





## Enum: UnitEnum


* `Count` (value: `"Count"`)

* `Bytes` (value: `"Bytes"`)

* `Seconds` (value: `"Seconds"`)

* `Percent` (value: `"Percent"`)

* `CountPerSecond` (value: `"CountPerSecond"`)

* `BytesPerSecond` (value: `"BytesPerSecond"`)




