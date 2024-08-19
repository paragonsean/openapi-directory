# FormRecognizerClient.KeyValueElement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**boundingBox** | **[Number]** | Quadrangle bounding box, with coordinates specified relative to the top-left of the original image. The eight numbers represent the four points, clockwise from the top-left corner relative to the text orientation. For image, the (x, y) coordinates are measured in pixels. For PDF, the (x, y) coordinates are measured in inches. | [optional] 
**elements** | **[String]** | When includeTextDetails is set to true, a list of references to the text elements constituting this key or value. | [optional] 
**text** | **String** | The text content of the key or value. | 


