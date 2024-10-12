# StorageManagementClient.BlobServicesListMetrics200ResponseValueInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endTime** | **Date** | Metric end time. | [optional] [readonly] 
**metricUnit** | **String** | Metric unit. | [optional] 
**metricValues** | [**[BlobServicesListMetrics200ResponseValueInnerMetricValuesInner]**](BlobServicesListMetrics200ResponseValueInnerMetricValuesInner.md) | List of metric values. | [optional] [readonly] 
**name** | [**BlobServicesListMetricDefinitions200ResponseValueInnerName**](BlobServicesListMetricDefinitions200ResponseValueInnerName.md) |  | [optional] 
**startTime** | **Date** | Metric start time. | [optional] [readonly] 
**timeGrain** | **String** | Metric time grain. | [optional] [readonly] 



## Enum: MetricUnitEnum


* `Count` (value: `"Count"`)

* `Bytes` (value: `"Bytes"`)

* `Seconds` (value: `"Seconds"`)

* `CountPerSecond` (value: `"CountPerSecond"`)

* `BytesPerSecond` (value: `"BytesPerSecond"`)




