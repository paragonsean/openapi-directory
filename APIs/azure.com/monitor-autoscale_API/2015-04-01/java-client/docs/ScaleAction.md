

# ScaleAction

The parameters for the scaling action.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cooldown** | **String** | the amount of time to wait since the last scaling action before this action occurs. It must be between 1 week and 1 minute in ISO 8601 format. |  |
|**direction** | [**DirectionEnum**](#DirectionEnum) | the scale direction. Whether the scaling action increases or decreases the number of instances. |  |
|**type** | [**TypeEnum**](#TypeEnum) | the type of action that should occur when the scale rule fires. |  |
|**value** | **String** | the number of instances that are involved in the scaling action. This value must be 1 or greater. The default value is 1. |  [optional] |



## Enum: DirectionEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| INCREASE | &quot;Increase&quot; |
| DECREASE | &quot;Decrease&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CHANGE_COUNT | &quot;ChangeCount&quot; |
| PERCENT_CHANGE_COUNT | &quot;PercentChangeCount&quot; |
| EXACT_COUNT | &quot;ExactCount&quot; |



