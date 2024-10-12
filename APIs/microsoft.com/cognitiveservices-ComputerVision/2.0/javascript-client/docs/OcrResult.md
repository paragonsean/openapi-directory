# ComputerVisionClient.OcrResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | **String** | The BCP-47 language code of the text in the image. | [optional] 
**orientation** | **String** | Orientation of the text recognized in the image. The value (up, down, left, or right) refers to the direction that the top of the recognized text is facing, after the image has been rotated around its center according to the detected text angle (see textAngle property). | [optional] 
**regions** | [**[OcrRegion]**](OcrRegion.md) | An array of objects, where each object represents a region of recognized text. | [optional] 
**textAngle** | **Number** | The angle, in degrees, of the detected text with respect to the closest horizontal or vertical direction. After rotating the input image clockwise by this angle, the recognized text lines become horizontal or vertical. In combination with the orientation property it can be used to overlay recognition results correctly on the original image, by rotating either the original image or recognition results by a suitable angle around the center of the original image. If the angle cannot be confidently detected, this property is not present. If the image contains text at different angles, only part of the text will be recognized correctly. | [optional] 


