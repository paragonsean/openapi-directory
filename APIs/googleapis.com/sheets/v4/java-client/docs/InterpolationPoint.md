

# InterpolationPoint

A single interpolation point on a gradient conditional format. These pin the gradient color scale according to the color, type and value chosen.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**color** | [**Color**](Color.md) |  |  [optional] |
|**colorStyle** | [**ColorStyle**](ColorStyle.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | How the value should be interpreted. |  [optional] |
|**value** | **String** | The value this interpolation point uses. May be a formula. Unused if type is MIN or MAX. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| INTERPOLATION_POINT_TYPE_UNSPECIFIED | &quot;INTERPOLATION_POINT_TYPE_UNSPECIFIED&quot; |
| MIN | &quot;MIN&quot; |
| MAX | &quot;MAX&quot; |
| NUMBER | &quot;NUMBER&quot; |
| PERCENT | &quot;PERCENT&quot; |
| PERCENTILE | &quot;PERCENTILE&quot; |



