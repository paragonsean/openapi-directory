# FormRecognizerClient.FieldValue

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**boundingBox** | **[Number]** | Quadrangle bounding box, with coordinates specified relative to the top-left of the original image. The eight numbers represent the four points, clockwise from the top-left corner relative to the text orientation. For image, the (x, y) coordinates are measured in pixels. For PDF, the (x, y) coordinates are measured in inches. | [optional] 
**confidence** | **Number** | Confidence value. | [optional] 
**elements** | **[String]** | When includeTextDetails is set to true, a list of references to the text elements constituting this field. | [optional] 
**page** | **Number** | The 1-based page number in the input document. | [optional] 
**text** | **String** | Text content of the extracted field. | [optional] 
**type** | [**FieldValueType**](FieldValueType.md) |  | 
**valueArray** | [**[FieldValue]**](FieldValue.md) | Array of field values. | [optional] 
**valueDate** | **Date** | Date value. | [optional] 
**valueInteger** | **Number** | Integer value. | [optional] 
**valueNumber** | **Number** | Floating point value. | [optional] 
**valueObject** | [**{String: FieldValue}**](FieldValue.md) | Dictionary of named field values. | [optional] 
**valuePhoneNumber** | **String** | Phone number value. | [optional] 
**valueString** | **String** | String value. | [optional] 
**valueTime** | **Date** | Time value. | [optional] 


