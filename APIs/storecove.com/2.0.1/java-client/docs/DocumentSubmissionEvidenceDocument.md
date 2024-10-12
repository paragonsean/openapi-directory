

# DocumentSubmissionEvidenceDocument


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**document** | **String** | The URL where the document can be retrieved. |  [optional] |
|**expiresAt** | **String** | The datetime the URL expires. Format: &#39;YYYY-MM-DD HH:mm:ss.&#39; |  [optional] |
|**mimeType** | [**MimeTypeEnum**](#MimeTypeEnum) | The mime type of the document. |  [optional] |



## Enum: MimeTypeEnum

| Name | Value |
|---- | -----|
| MESSAGE_RFC822 | &quot;message/rfc822&quot; |
| APPLICATION_XML | &quot;application/xml&quot; |
| APPLICATION_JSON | &quot;application/json&quot; |
| APPLICATION_PDF | &quot;application/pdf&quot; |



