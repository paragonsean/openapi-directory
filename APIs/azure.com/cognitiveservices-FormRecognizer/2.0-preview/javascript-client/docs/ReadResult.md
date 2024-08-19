# FormRecognizerClient.ReadResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**angle** | **Number** | The general orientation of the text in clockwise direction, measured in degrees between (-180, 180]. | 
**height** | **Number** | The height of the image/PDF in pixels/inches, respectively. | 
**language** | [**Language**](Language.md) |  | [optional] 
**lines** | [**[TextLine]**](TextLine.md) | When includeTextDetails is set to true, a list of recognized text lines. The maximum number of lines returned is 300 per page. The lines are sorted top to bottom, left to right, although in certain cases proximity is treated with higher priority. As the sorting order depends on the detected text, it may change across images and OCR version updates. Thus, business logic should be built upon the actual line location instead of order. | [optional] 
**page** | **Number** | The 1-based page number in the input document. | 
**unit** | **String** | The unit used by the width, height and boundingBox properties. For images, the unit is \&quot;pixel\&quot;. For PDF, the unit is \&quot;inch\&quot;. | 
**width** | **Number** | The width of the image/PDF in pixels/inches, respectively. | 



## Enum: UnitEnum


* `pixel` (value: `"pixel"`)

* `inch` (value: `"inch"`)




