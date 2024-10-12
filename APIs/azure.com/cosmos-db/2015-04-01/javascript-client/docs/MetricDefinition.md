# CosmosDb.MetricDefinition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metricAvailabilities** | [**[MetricAvailability]**](MetricAvailability.md) | The list of metric availabilities for the account. | [optional] [readonly] 
**name** | [**MetricName**](MetricName.md) |  | [optional] 
**primaryAggregationType** | **String** | The primary aggregation type of the metric. | [optional] [readonly] 
**resourceUri** | **String** | The resource uri of the database. | [optional] [readonly] 
**unit** | [**UnitType**](UnitType.md) |  | [optional] 



## Enum: PrimaryAggregationTypeEnum


* `None` (value: `"None"`)

* `Average` (value: `"Average"`)

* `Total` (value: `"Total"`)

* `Minimum` (value: `"Minimum"`)

* `Maximum` (value: `"Maximum"`)

* `Last` (value: `"Last"`)




