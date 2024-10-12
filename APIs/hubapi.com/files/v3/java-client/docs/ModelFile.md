

# ModelFile

File

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**access** | [**AccessEnum**](#AccessEnum) | File access. Can be PUBLIC_INDEXABLE, PUBLIC_NOT_INDEXABLE, PRIVATE. |  |
|**archived** | **Boolean** | If the file is deleted. |  |
|**archivedAt** | **OffsetDateTime** | Deletion time of the file object. |  [optional] |
|**createdAt** | **OffsetDateTime** | Creation time of the file object. |  |
|**defaultHostingUrl** | **String** | Default hosting URL of the file. This will use one of HubSpot&#39;s provided URLs to serve the file. |  [optional] |
|**encoding** | **String** | Encoding of the file. |  [optional] |
|**expiresAt** | **Long** |  |  [optional] |
|**extension** | **String** | Extension of the file. ex: .jpg, .png, .gif, .pdf, etc. |  [optional] |
|**height** | **Integer** | For image and video files, the height of the content. |  [optional] |
|**id** | **String** | File ID. |  |
|**isUsableInContent** | **Boolean** | Previously \&quot;archied\&quot;. Indicates if the file should be used when creating new content like web pages. |  [optional] |
|**name** | **String** | Name of the file. |  [optional] |
|**parentFolderId** | **String** | ID of the folder the file is in. |  [optional] |
|**path** | **String** | Path of the file in the file manager. |  [optional] |
|**size** | **Long** | Size of the file in bytes. |  [optional] |
|**type** | **String** | Type of the file. Can be IMG, DOCUMENT, AUDIO, MOVIE, or OTHER. |  [optional] |
|**updatedAt** | **OffsetDateTime** | Timestamp of the latest update to the file. |  |
|**url** | **String** | URL of the given file. This URL can change depending on the domain settings of the account. Will use the select file hosting domain. |  [optional] |
|**width** | **Integer** | For image and video files, the width of the content. |  [optional] |



## Enum: AccessEnum

| Name | Value |
|---- | -----|
| PUBLIC_INDEXABLE | &quot;PUBLIC_INDEXABLE&quot; |
| PUBLIC_NOT_INDEXABLE | &quot;PUBLIC_NOT_INDEXABLE&quot; |
| HIDDEN_INDEXABLE | &quot;HIDDEN_INDEXABLE&quot; |
| HIDDEN_NOT_INDEXABLE | &quot;HIDDEN_NOT_INDEXABLE&quot; |
| HIDDEN_PRIVATE | &quot;HIDDEN_PRIVATE&quot; |
| PRIVATE | &quot;PRIVATE&quot; |



