# LinQr.LinearGradient

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**angle** | **Number** | Gradient angle (direction) in degrees. By default, horizontal gradient is applied. To reverse color direction use value of 180. Vertical gradients are indicated by values of 90 and 270. You can choose any angle value within the given range. | [optional] [default to 0]
**stops** | [**[GradientStop]**](GradientStop.md) | Gradient is created by specifying a list of (at least two) points called a &#x60;stop&#x60;. Each of them specifies a &#x60;offset&#x60; (in percent) along gradient fill and the &#x60;color&#x60; that the fill get at the given point. | [optional] 
**type** | **String** |  | [optional] [default to &#39;linear&#39;]



## Enum: TypeEnum


* `linear` (value: `"linear"`)




