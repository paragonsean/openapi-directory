# ComputerVisionClient.TextRecognitionResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clockwiseOrientation** | **Number** | The orientation of the image in degrees in the clockwise direction. Range between [0, 360). | [optional] 
**height** | **Number** | The height of the image in pixels or the PDF in inches. | [optional] 
**lines** | [**[Line]**](Line.md) | A list of recognized text lines. | 
**page** | **Number** | The 1-based page number of the recognition result. | [optional] 
**unit** | **String** | The unit used in the Width, Height and BoundingBox. For images, the unit is &#39;pixel&#39;. For PDF, the unit is &#39;inch&#39;. | [optional] 
**width** | **Number** | The width of the image in pixels or the PDF in inches. | [optional] 



## Enum: UnitEnum


* `pixel` (value: `"pixel"`)

* `inch` (value: `"inch"`)




