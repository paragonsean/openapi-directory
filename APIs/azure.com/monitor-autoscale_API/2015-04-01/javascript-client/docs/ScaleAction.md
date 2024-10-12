# MonitorManagementClient.ScaleAction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cooldown** | **String** | the amount of time to wait since the last scaling action before this action occurs. It must be between 1 week and 1 minute in ISO 8601 format. | 
**direction** | **String** | the scale direction. Whether the scaling action increases or decreases the number of instances. | 
**type** | **String** | the type of action that should occur when the scale rule fires. | 
**value** | **String** | the number of instances that are involved in the scaling action. This value must be 1 or greater. The default value is 1. | [optional] [default to &#39;1&#39;]



## Enum: DirectionEnum


* `None` (value: `"None"`)

* `Increase` (value: `"Increase"`)

* `Decrease` (value: `"Decrease"`)





## Enum: TypeEnum


* `ChangeCount` (value: `"ChangeCount"`)

* `PercentChangeCount` (value: `"PercentChangeCount"`)

* `ExactCount` (value: `"ExactCount"`)




