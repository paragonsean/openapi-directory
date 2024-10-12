

# AffineTransform

AffineTransform uses a 3x3 matrix with an implied last row of [ 0 0 1 ] to transform source coordinates (x,y) into destination coordinates (x', y') according to: x' x = shear_y scale_y translate_y 1 [ 1 ] After transformation, x' = scale_x * x + shear_x * y + translate_x; y' = scale_y * y + shear_y * x + translate_y; This message is therefore composed of these six matrix elements.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**scaleX** | **Double** | The X coordinate scaling element. |  [optional] |
|**scaleY** | **Double** | The Y coordinate scaling element. |  [optional] |
|**shearX** | **Double** | The X coordinate shearing element. |  [optional] |
|**shearY** | **Double** | The Y coordinate shearing element. |  [optional] |
|**translateX** | **Double** | The X coordinate translation element. |  [optional] |
|**translateY** | **Double** | The Y coordinate translation element. |  [optional] |
|**unit** | [**UnitEnum**](#UnitEnum) | The units for translate elements. |  [optional] |



## Enum: UnitEnum

| Name | Value |
|---- | -----|
| UNIT_UNSPECIFIED | &quot;UNIT_UNSPECIFIED&quot; |
| EMU | &quot;EMU&quot; |
| PT | &quot;PT&quot; |



