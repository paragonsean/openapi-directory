# GmailApi.MessagePartBody

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachmentId** | **String** | When present, contains the ID of an external attachment that can be retrieved in a separate &#x60;messages.attachments.get&#x60; request. When not present, the entire content of the message part body is contained in the data field. | [optional] 
**data** | **Blob** | The body data of a MIME message part as a base64url encoded string. May be empty for MIME container types that have no message body or when the body data is sent as a separate attachment. An attachment ID is present if the body data is contained in a separate attachment. | [optional] 
**size** | **Number** | Number of bytes for the message part data (encoding notwithstanding). | [optional] 


