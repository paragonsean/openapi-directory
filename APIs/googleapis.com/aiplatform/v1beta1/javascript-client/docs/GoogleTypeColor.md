# VertexAiApi.GoogleTypeColor

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alpha** | **Number** | The fraction of this color that should be applied to the pixel. That is, the final pixel color is defined by the equation: &#x60;pixel color &#x3D; alpha * (this color) + (1.0 - alpha) * (background color)&#x60; This means that a value of 1.0 corresponds to a solid color, whereas a value of 0.0 corresponds to a completely transparent color. This uses a wrapper message rather than a simple float scalar so that it is possible to distinguish between a default value and the value being unset. If omitted, this color object is rendered as a solid color (as if the alpha value had been explicitly given a value of 1.0). | [optional] 
**blue** | **Number** | The amount of blue in the color as a value in the interval [0, 1]. | [optional] 
**green** | **Number** | The amount of green in the color as a value in the interval [0, 1]. | [optional] 
**red** | **Number** | The amount of red in the color as a value in the interval [0, 1]. | [optional] 


