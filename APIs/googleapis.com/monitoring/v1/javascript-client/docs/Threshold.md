# CloudMonitoringApi.Threshold

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **String** | The state color for this threshold. Color is not allowed in a XyChart. | [optional] 
**direction** | **String** | The direction for the current threshold. Direction is not allowed in a XyChart. | [optional] 
**label** | **String** | A label for the threshold. | [optional] 
**targetAxis** | **String** | The target axis to use for plotting the threshold. Target axis is not allowed in a Scorecard. | [optional] 
**value** | **Number** | The value of the threshold. The value should be defined in the native scale of the metric. | [optional] 



## Enum: ColorEnum


* `COLOR_UNSPECIFIED` (value: `"COLOR_UNSPECIFIED"`)

* `YELLOW` (value: `"YELLOW"`)

* `RED` (value: `"RED"`)





## Enum: DirectionEnum


* `DIRECTION_UNSPECIFIED` (value: `"DIRECTION_UNSPECIFIED"`)

* `ABOVE` (value: `"ABOVE"`)

* `BELOW` (value: `"BELOW"`)





## Enum: TargetAxisEnum


* `TARGET_AXIS_UNSPECIFIED` (value: `"TARGET_AXIS_UNSPECIFIED"`)

* `Y1` (value: `"Y1"`)

* `Y2` (value: `"Y2"`)




