

# ActivityObjectAttachmentsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**content** | **String** | If the attachment is an article, this property contains a snippet of text from the article. It can also include descriptions for other types. |  [optional] |
|**displayName** | **String** | The title of the attachment, such as a photo caption or an article title. |  [optional] |
|**embed** | [**ActivityObjectAttachmentsInnerEmbed**](ActivityObjectAttachmentsInnerEmbed.md) |  |  [optional] |
|**fullImage** | [**ActivityObjectAttachmentsInnerFullImage**](ActivityObjectAttachmentsInnerFullImage.md) |  |  [optional] |
|**id** | **String** | The ID of the attachment. |  [optional] |
|**image** | [**ActivityObjectAttachmentsInnerImage**](ActivityObjectAttachmentsInnerImage.md) |  |  [optional] |
|**objectType** | **String** | The type of media object. Possible values include, but are not limited to, the following values:   - \&quot;photo\&quot; - A photo.  - \&quot;album\&quot; - A photo album.  - \&quot;video\&quot; - A video.  - \&quot;article\&quot; - An article, specified by a link. |  [optional] |
|**thumbnails** | [**List&lt;ActivityObjectAttachmentsInnerThumbnailsInner&gt;**](ActivityObjectAttachmentsInnerThumbnailsInner.md) | If the attachment is an album, this property is a list of potential additional thumbnails from the album. |  [optional] |
|**url** | **String** | The link to the attachment, which should be of type text/html. |  [optional] |



