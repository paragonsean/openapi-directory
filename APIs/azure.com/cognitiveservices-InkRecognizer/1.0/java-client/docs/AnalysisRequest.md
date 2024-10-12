

# AnalysisRequest

This shows the expected contents of a request

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applicationType** | [**ApplicationTypeEnum**](#ApplicationTypeEnum) | This describes the domain of the client application |  [optional] |
|**inkPointValueAttributes** | [**List&lt;InkPointValueAttribute&gt;**](InkPointValueAttribute.md) |  |  [optional] |
|**inputDeviceKind** | [**InputDeviceKindEnum**](#InputDeviceKindEnum) | This identifies the kind of device used as the writing instrument |  [optional] |
|**language** | **String** | The IETF BCP 47 language code (for ex. en-US, en-GB, hi-IN etc.) of the expected language for the handwritten content in the ink strokes. The response will include results from this language. |  |
|**strokes** | [**List&lt;Stroke&gt;**](Stroke.md) | This is the array of strokes sent for recognition. Best results are produced when the order of strokes added in the array matches the order in which the user created them. Changing the stroke order may produce unexpected results. |  |
|**unit** | [**UnitEnum**](#UnitEnum) | This is the physical unit of the ink strokes. It is up to the application developer to decide how to convert the device specific units to physical units before calling the service. The conversion factor can be different based on the type of the device used. |  [optional] |
|**unitMultiple** | **BigDecimal** |  This is a scaling factor to be applied to the point coordinates when interpreting them in the physical units specified. |  [optional] |



## Enum: ApplicationTypeEnum

| Name | Value |
|---- | -----|
| DRAWING | &quot;drawing&quot; |
| WRITING | &quot;writing&quot; |
| MIXED | &quot;mixed&quot; |



## Enum: InputDeviceKindEnum

| Name | Value |
|---- | -----|
| DIGITIZER | &quot;digitizer&quot; |
| PEN | &quot;pen&quot; |
| LIGHT_PEN | &quot;lightPen&quot; |
| TOUCH_SCREEN | &quot;touchScreen&quot; |
| TOUCH_PAD | &quot;touchPad&quot; |
| WHITE_BOARD | &quot;whiteBoard&quot; |
| _3D_DIGITIZER | &quot;3dDigitizer&quot; |
| STEREO_PLOTTER | &quot;stereoPlotter&quot; |
| ARTICULATED_ARM | &quot;articulatedArm&quot; |
| ARMATURE | &quot;armature&quot; |



## Enum: UnitEnum

| Name | Value |
|---- | -----|
| MM | &quot;mm&quot; |
| CM | &quot;cm&quot; |
| IN | &quot;in&quot; |



