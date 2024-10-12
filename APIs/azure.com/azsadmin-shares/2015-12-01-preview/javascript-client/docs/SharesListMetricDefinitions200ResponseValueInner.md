# StorageManagementClient.SharesListMetricDefinitions200ResponseValueInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metricAvailabilities** | [**[SharesListMetricDefinitions200ResponseValueInnerMetricAvailabilitiesInner]**](SharesListMetricDefinitions200ResponseValueInnerMetricAvailabilitiesInner.md) | Metric availabilities. | [optional] [readonly] 
**name** | [**SharesListMetricDefinitions200ResponseValueInnerName**](SharesListMetricDefinitions200ResponseValueInnerName.md) |  | [optional] 
**primaryAggregationType** | **String** | Aggregate type. | [optional] [readonly] 
**unit** | **String** | Metric unit. | [optional] 



## Enum: PrimaryAggregationTypeEnum


* `None` (value: `"None"`)

* `Average` (value: `"Average"`)

* `Total` (value: `"Total"`)

* `Minimum` (value: `"Minimum"`)

* `Maximum` (value: `"Maximum"`)

* `Last` (value: `"Last"`)





## Enum: UnitEnum


* `Count` (value: `"Count"`)

* `Bytes` (value: `"Bytes"`)

* `Seconds` (value: `"Seconds"`)

* `CountPerSecond` (value: `"CountPerSecond"`)

* `BytesPerSecond` (value: `"BytesPerSecond"`)




