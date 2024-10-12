

# Threshold

Defines a threshold for categorizing time series values.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**color** | [**ColorEnum**](#ColorEnum) | The state color for this threshold. Color is not allowed in a XyChart. |  [optional] |
|**direction** | [**DirectionEnum**](#DirectionEnum) | The direction for the current threshold. Direction is not allowed in a XyChart. |  [optional] |
|**label** | **String** | A label for the threshold. |  [optional] |
|**targetAxis** | [**TargetAxisEnum**](#TargetAxisEnum) | The target axis to use for plotting the threshold. Target axis is not allowed in a Scorecard. |  [optional] |
|**value** | **Double** | The value of the threshold. The value should be defined in the native scale of the metric. |  [optional] |



## Enum: ColorEnum

| Name | Value |
|---- | -----|
| COLOR_UNSPECIFIED | &quot;COLOR_UNSPECIFIED&quot; |
| YELLOW | &quot;YELLOW&quot; |
| RED | &quot;RED&quot; |



## Enum: DirectionEnum

| Name | Value |
|---- | -----|
| DIRECTION_UNSPECIFIED | &quot;DIRECTION_UNSPECIFIED&quot; |
| ABOVE | &quot;ABOVE&quot; |
| BELOW | &quot;BELOW&quot; |



## Enum: TargetAxisEnum

| Name | Value |
|---- | -----|
| TARGET_AXIS_UNSPECIFIED | &quot;TARGET_AXIS_UNSPECIFIED&quot; |
| Y1 | &quot;Y1&quot; |
| Y2 | &quot;Y2&quot; |



