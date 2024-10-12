# InkRecognizerClient.AnalysisRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicationType** | **String** | This describes the domain of the client application | [optional] 
**inkPointValueAttributes** | [**[InkPointValueAttribute]**](InkPointValueAttribute.md) |  | [optional] 
**inputDeviceKind** | **String** | This identifies the kind of device used as the writing instrument | [optional] 
**language** | **String** | The IETF BCP 47 language code (for ex. en-US, en-GB, hi-IN etc.) of the expected language for the handwritten content in the ink strokes. The response will include results from this language. | 
**strokes** | [**[Stroke]**](Stroke.md) | This is the array of strokes sent for recognition. Best results are produced when the order of strokes added in the array matches the order in which the user created them. Changing the stroke order may produce unexpected results. | 
**unit** | **String** | This is the physical unit of the ink strokes. It is up to the application developer to decide how to convert the device specific units to physical units before calling the service. The conversion factor can be different based on the type of the device used. | [optional] 
**unitMultiple** | **Number** |  This is a scaling factor to be applied to the point coordinates when interpreting them in the physical units specified. | [optional] 



## Enum: ApplicationTypeEnum


* `drawing` (value: `"drawing"`)

* `writing` (value: `"writing"`)

* `mixed` (value: `"mixed"`)





## Enum: InputDeviceKindEnum


* `digitizer` (value: `"digitizer"`)

* `pen` (value: `"pen"`)

* `lightPen` (value: `"lightPen"`)

* `touchScreen` (value: `"touchScreen"`)

* `touchPad` (value: `"touchPad"`)

* `whiteBoard` (value: `"whiteBoard"`)

* `3dDigitizer` (value: `"3dDigitizer"`)

* `stereoPlotter` (value: `"stereoPlotter"`)

* `articulatedArm` (value: `"articulatedArm"`)

* `armature` (value: `"armature"`)





## Enum: UnitEnum


* `mm` (value: `"mm"`)

* `cm` (value: `"cm"`)

* `in` (value: `"in"`)




