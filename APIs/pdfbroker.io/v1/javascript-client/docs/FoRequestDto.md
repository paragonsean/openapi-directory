# PdfBrokerIoApi.FoRequestDto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**foDocumentBase64String** | **String** | This is the complete XSL-FO document provided using Base64 encoding. | [optional] 
**metadata** | [**PdfMetadataDto**](PdfMetadataDto.md) |  | [optional] 
**resources** | **{String: String}** | This is a set of key-value pairs of digital resources like images that is referenced in the XSL-FO document. It uses the filename as key and the data is provided as a Base64 encoded string. | [optional] 


