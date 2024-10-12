

# FoTransformRequestDto

The XSL-FO transform document and xml data document as a Base64 encoded string with a set of resources provided with a name and the data of the resource as a Base64 encoded string.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**foDocumentBase64String** | **String** | This is the complete XSL-FO document provided using Base64 encoding. |  [optional] |
|**metadata** | [**PdfMetadataDto**](PdfMetadataDto.md) |  |  [optional] |
|**resources** | **Map&lt;String, String&gt;** | This is a set of key-value pairs of digital resources like images that is referenced in the XSL-FO document. It uses the filename as key and the data is provided as a Base64 encoded string. |  [optional] |
|**xmlDataDocumentBase64String** | **String** | This is xml data document on which the XSL-FO transform document is applied. Provided using Base64 encoding. |  [optional] |



