# ComputerVisionClient.Word

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**boundingBox** | **[Number]** | Quadrangle bounding box, with coordinates in original image. The eight numbers represent the four points (x-coordinate, y-coordinate from the left-top corner of the image) of the detected rectangle from the left-top corner in the clockwise direction. For images, coordinates are in pixels. For PDF, coordinates are in inches. | 
**confidence** | **String** | Qualitative confidence measure. | [optional] 
**text** | **String** | The text content of the word. | 



## Enum: ConfidenceEnum


* `High` (value: `"High"`)

* `Low` (value: `"Low"`)




