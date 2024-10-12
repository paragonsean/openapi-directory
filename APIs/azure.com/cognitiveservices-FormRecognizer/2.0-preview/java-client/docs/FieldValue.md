

# FieldValue

Recognized field value.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**boundingBox** | **List&lt;BigDecimal&gt;** | Quadrangle bounding box, with coordinates specified relative to the top-left of the original image. The eight numbers represent the four points, clockwise from the top-left corner relative to the text orientation. For image, the (x, y) coordinates are measured in pixels. For PDF, the (x, y) coordinates are measured in inches. |  [optional] |
|**confidence** | **BigDecimal** | Confidence value. |  [optional] |
|**elements** | **List&lt;String&gt;** | When includeTextDetails is set to true, a list of references to the text elements constituting this field. |  [optional] |
|**page** | **Integer** | The 1-based page number in the input document. |  [optional] |
|**text** | **String** | Text content of the extracted field. |  [optional] |
|**type** | **FieldValueType** |  |  |
|**valueArray** | [**List&lt;FieldValue&gt;**](FieldValue.md) | Array of field values. |  [optional] |
|**valueDate** | **OffsetDateTime** | Date value. |  [optional] |
|**valueInteger** | **Integer** | Integer value. |  [optional] |
|**valueNumber** | **BigDecimal** | Floating point value. |  [optional] |
|**valueObject** | [**Map&lt;String, FieldValue&gt;**](FieldValue.md) | Dictionary of named field values. |  [optional] |
|**valuePhoneNumber** | **String** | Phone number value. |  [optional] |
|**valueString** | **String** | String value. |  [optional] |
|**valueTime** | **OffsetDateTime** | Time value. |  [optional] |



