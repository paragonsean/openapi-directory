# StorageManagementClient.BlobServicesListMetricDefinitions200ResponseValueInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metricAvailabilities** | [**[BlobServicesListMetricDefinitions200ResponseValueInnerMetricAvailabilitiesInner]**](BlobServicesListMetricDefinitions200ResponseValueInnerMetricAvailabilitiesInner.md) | Metric availabilities. | [optional] [readonly] 
**name** | [**BlobServicesListMetricDefinitions200ResponseValueInnerName**](BlobServicesListMetricDefinitions200ResponseValueInnerName.md) |  | [optional] 
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




