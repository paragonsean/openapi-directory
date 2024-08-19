# MonitorClient.MetricDefinition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | the resource identifier of the metric definition. | [optional] 
**metricAvailabilities** | [**[MetricAvailability]**](MetricAvailability.md) | the collection of what aggregation intervals are available to be queried. | [optional] 
**name** | [**LocalizableString**](LocalizableString.md) |  | [optional] 
**primaryAggregationType** | **String** | the primary aggregation type value defining how to use the values for display. | [optional] 
**resourceId** | **String** | the resource identifier of the resource that emitted the metric. | [optional] 
**unit** | [**Unit**](Unit.md) |  | [optional] 



## Enum: PrimaryAggregationTypeEnum


* `None` (value: `"None"`)

* `Average` (value: `"Average"`)

* `Count` (value: `"Count"`)

* `Minimum` (value: `"Minimum"`)

* `Maximum` (value: `"Maximum"`)

* `Total` (value: `"Total"`)




