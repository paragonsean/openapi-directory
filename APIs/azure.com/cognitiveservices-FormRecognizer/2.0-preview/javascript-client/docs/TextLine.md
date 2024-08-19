# FormRecognizerClient.TextLine

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**boundingBox** | **[Number]** | Quadrangle bounding box, with coordinates specified relative to the top-left of the original image. The eight numbers represent the four points, clockwise from the top-left corner relative to the text orientation. For image, the (x, y) coordinates are measured in pixels. For PDF, the (x, y) coordinates are measured in inches. | 
**language** | [**Language**](Language.md) |  | [optional] 
**text** | **String** | The text content of the line. | 
**words** | [**[TextWord]**](TextWord.md) | List of words in the text line. | 


