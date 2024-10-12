# GoogleChatApi.Attachment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachmentDataRef** | [**AttachmentDataRef**](AttachmentDataRef.md) |  | [optional] 
**contentName** | **String** | Output only. The original file name for the content, not the full path. | [optional] [readonly] 
**contentType** | **String** | Output only. The content type (MIME type) of the file. | [optional] [readonly] 
**downloadUri** | **String** | Output only. The download URL which should be used to allow a human user to download the attachment. Chat apps shouldn&#39;t use this URL to download attachment content. | [optional] [readonly] 
**driveDataRef** | [**DriveDataRef**](DriveDataRef.md) |  | [optional] 
**name** | **String** | Resource name of the attachment, in the form &#x60;spaces/_*_/messages/_*_/attachments/_*&#x60;. | [optional] 
**source** | **String** | Output only. The source of the attachment. | [optional] [readonly] 
**thumbnailUri** | **String** | Output only. The thumbnail URL which should be used to preview the attachment to a human user. Chat apps shouldn&#39;t use this URL to download attachment content. | [optional] [readonly] 



## Enum: SourceEnum


* `SOURCE_UNSPECIFIED` (value: `"SOURCE_UNSPECIFIED"`)

* `DRIVE_FILE` (value: `"DRIVE_FILE"`)

* `UPLOADED_CONTENT` (value: `"UPLOADED_CONTENT"`)




