# MonitorManagementClient.DynamicMetricCriteria

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alertSensitivity** | **String** | The extent of deviation required to trigger an alert. This will affect how tight the threshold is to the metric series pattern. | 
**failingPeriods** | [**DynamicThresholdFailingPeriods**](DynamicThresholdFailingPeriods.md) |  | 
**ignoreDataBefore** | **Date** | Use this option to set the date from which to start learning the metric historical data and calculate the dynamic thresholds (in ISO8601 format) | [optional] 
**operator** | **String** | The operator used to compare the metric value against the threshold. | 



## Enum: AlertSensitivityEnum


* `Low` (value: `"Low"`)

* `Medium` (value: `"Medium"`)

* `High` (value: `"High"`)





## Enum: OperatorEnum


* `GreaterThan` (value: `"GreaterThan"`)

* `LessThan` (value: `"LessThan"`)

* `GreaterOrLessThan` (value: `"GreaterOrLessThan"`)




