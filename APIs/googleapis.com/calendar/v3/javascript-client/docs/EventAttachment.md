# CalendarApi.EventAttachment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fileId** | **String** | ID of the attached file. Read-only. For Google Drive files, this is the ID of the corresponding Files resource entry in the Drive API. | [optional] 
**fileUrl** | **String** | URL link to the attachment. For adding Google Drive file attachments use the same format as in alternateLink property of the Files resource in the Drive API. Required when adding an attachment. | [optional] 
**iconLink** | **String** | URL link to the attachment&#39;s icon. This field can only be modified for custom third-party attachments. | [optional] 
**mimeType** | **String** | Internet media type (MIME type) of the attachment. | [optional] 
**title** | **String** | Attachment title. | [optional] 


