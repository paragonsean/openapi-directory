# GmailApi.MessagePart

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | [**MessagePartBody**](MessagePartBody.md) |  | [optional] 
**filename** | **String** | The filename of the attachment. Only present if this message part represents an attachment. | [optional] 
**headers** | [**[MessagePartHeader]**](MessagePartHeader.md) | List of headers on this message part. For the top-level message part, representing the entire message payload, it will contain the standard RFC 2822 email headers such as &#x60;To&#x60;, &#x60;From&#x60;, and &#x60;Subject&#x60;. | [optional] 
**mimeType** | **String** | The MIME type of the message part. | [optional] 
**partId** | **String** | The immutable ID of the message part. | [optional] 
**parts** | [**[MessagePart]**](MessagePart.md) | The child MIME message parts of this part. This only applies to container MIME message parts, for example &#x60;multipart/_*&#x60;. For non- container MIME message part types, such as &#x60;text/plain&#x60;, this field is empty. For more information, see RFC 1521. | [optional] 


