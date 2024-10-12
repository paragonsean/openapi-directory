# SubscriptionsManagementClient.PlansListMetricDefinitions200ResponseValueInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metricAvailabilities** | [**[PlansListMetricDefinitions200ResponseValueInnerMetricAvailabilitiesInner]**](PlansListMetricDefinitions200ResponseValueInnerMetricAvailabilitiesInner.md) | List of metric definitions. | [optional] 
**name** | **String** | Metric definition name. | [optional] 
**primaryAggregationType** | **String** | The primary aggregation type for resource metric. | [optional] 
**unit** | **String** | The resource metric unit. | [optional] 



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




