

# ModelFile


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**links** | [**List&lt;FileLinksInner&gt;**](FileLinksInner.md) | The links related to resource. |  [optional] [readonly] |
|**createdTime** | **OffsetDateTime** | The upload date/time. |  [optional] [readonly] |
|**description** | **String** | The File description. |  [optional] |
|**extension** | **String** | The File extension. |  [optional] |
|**height** | **Integer** | Image height, applicable to images only. |  [optional] [readonly] |
|**id** | **String** | The resource ID. Defaults to UUID v4. |  [optional] [readonly] |
|**isPublic** | **Boolean** | Is the file available publicly (without authentication). If true, the permalink in the _links section contains the public URL. |  [optional] |
|**mime** | [**MimeEnum**](#MimeEnum) | The mime type. |  [optional] [readonly] |
|**name** | **String** | Original File name. |  [optional] |
|**sha1** | **String** | Hash sum of the file. |  [optional] [readonly] |
|**size** | **Integer** | The File size in bytes. |  [optional] [readonly] |
|**tags** | **List&lt;String&gt;** | The tags list. |  [optional] |
|**updatedTime** | **OffsetDateTime** | The latest update date/time. |  [optional] [readonly] |
|**width** | **Integer** | Image width, applicable to images only. |  [optional] [readonly] |



## Enum: MimeEnum

| Name | Value |
|---- | -----|
| IMAGE_PNG | &quot;image/png&quot; |
| IMAGE_JPEG | &quot;image/jpeg&quot; |
| IMAGE_GIF | &quot;image/gif&quot; |
| APPLICATION_PDF | &quot;application/pdf&quot; |
| AUDIO_MPEG | &quot;audio/mpeg&quot; |



