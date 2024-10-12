# StorecoveApi.Attachment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | A description for the file attachment. | [optional] 
**document** | **String** | The base64 encoded version of the document attachment. | 
**documentId** | **String** | An id for the file attachment. | [optional] 
**filename** | **String** | The name of the file attachment. | [optional] 
**mimeType** | **String** | The document attachment mime type. Currently only application/pdf is allowed. | 
**primaryImage** | **Boolean** | Whether or not this document is a visual representation of the invoice data. Note that although this property is not yet deprecated, using value &#39;true&#39; is discouraged, since the invoice data itself is leading, not the image, and including an image may lead to confusion. Peppol no longer allows including primary images. | [optional] [default to false]



## Enum: MimeTypeEnum


* `application/pdf` (value: `"application/pdf"`)




