

# MediaAttachment

Media attachment. The API will automatically resolve the details, oEmbed, and media available if possible and return them in this object 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authorName** | **String** | The resolved author name of the attachment |  [optional] |
|**authorUrl** | **String** | The resolved author url of the attachment |  [optional] |
|**description** | **String** | The resolved description of the attachment |  [optional] |
|**googleDriveFileId** | **String** | The ID of the Google Drive File |  [optional] |
|**html** | **String** | If the attachment type is &#x60;rich&#x60; or &#x60;video&#x60;, the HTML code of the media to display  |  [optional] |
|**htmlHeight** | **String** | If the &#x60;html&#x60; is available, the height of the widget |  [optional] |
|**htmlWidth** | **String** | If the &#x60;html&#x60; is available, the width of the widget |  [optional] |
|**iconUrl** | **String** | The URL of the icon |  [optional] |
|**lockScoreTemplate** | **Boolean** | To be used with a score attached in &#x60;sharingMode&#x60; &#x60;copy&#x60; (score used as template). If true, students won&#39;t be able to change the original notes of the template. |  [optional] |
|**mimeType** | **String** | The mine type of the file |  [optional] |
|**revision** | **String** | An unique revision identifier of a score |  [optional] |
|**score** | **String** | An unique Flat score identifier |  [optional] |
|**sharingMode** | **MediaScoreSharingMode** |  |  [optional] |
|**thumbnailHeight** | **Integer** | If the &#x60;thumbnailUrl&#x60; is available, the width of the thumbnail  |  [optional] |
|**thumbnailUrl** | **String** | If the attachment type is &#x60;rich&#x60;, &#x60;video&#x60;, &#x60;photo&#x60; or &#x60;link&#x60;, a displayable thumbnail for this attachment  |  [optional] |
|**thumbnailWidth** | **Integer** | If the &#x60;thumbnailUrl&#x60; is available, the width of the thumbnail  |  [optional] |
|**title** | **String** | The resolved title of the attachment |  [optional] |
|**track** | **String** | A unique track identifier |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the assignment resolved: * &#x60;rich&#x60;, &#x60;photo&#x60;, &#x60;video&#x60; are attachment types that are automatically resolved from a &#x60;link&#x60; attachment. * A &#x60;flat&#x60; attachment is a score document where the unique identifier will be specified in the &#x60;score&#x60; property. Its sharing mode will be provided in the &#x60;sharingMode&#x60; property.  |  [optional] |
|**url** | **String** | The url of the attachment |  [optional] |
|**worksheet** | **String** | An unique worksheet identifier |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| RICH | &quot;rich&quot; |
| PHOTO | &quot;photo&quot; |
| VIDEO | &quot;video&quot; |
| LINK | &quot;link&quot; |
| FLAT | &quot;flat&quot; |
| GOOGLE_DRIVE | &quot;googleDrive&quot; |
| WORKSHEET | &quot;worksheet&quot; |
| PERFORMANCE | &quot;performance&quot; |



