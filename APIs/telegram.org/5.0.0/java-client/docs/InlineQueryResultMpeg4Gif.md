

# InlineQueryResultMpeg4Gif

Represents a link to a video animation (H.264/MPEG-4 AVC video without sound). By default, this animated MPEG-4 file will be sent by the user with optional caption. Alternatively, you can use *input\\_message\\_content* to send a message with the specified content instead of the animation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**caption** | **String** | *Optional*. Caption of the MPEG-4 file to be sent, 0-1024 characters after entities parsing |  [optional] |
|**captionEntities** | [**List&lt;MessageEntity&gt;**](MessageEntity.md) | *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse\\_mode* |  [optional] |
|**id** | **String** | Unique identifier for this result, 1-64 bytes |  |
|**inputMessageContent** | [**InputMessageContent**](InputMessageContent.md) |  |  [optional] |
|**mpeg4Duration** | **Integer** | *Optional*. Video duration |  [optional] |
|**mpeg4Height** | **Integer** | *Optional*. Video height |  [optional] |
|**mpeg4Url** | **String** | A valid URL for the MP4 file. File size must not exceed 1MB |  |
|**mpeg4Width** | **Integer** | *Optional*. Video width |  [optional] |
|**parseMode** | **String** | *Optional*. Mode for parsing entities in the caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details. |  [optional] |
|**replyMarkup** | [**InlineKeyboardMarkup**](InlineKeyboardMarkup.md) |  |  [optional] |
|**thumbMimeType** | [**ThumbMimeTypeEnum**](#ThumbMimeTypeEnum) | *Optional*. MIME type of the thumbnail, must be one of “image/jpeg”, “image/gif”, or “video/mp4”. Defaults to “image/jpeg” |  [optional] |
|**thumbUrl** | **String** | URL of the static (JPEG or GIF) or animated (MPEG4) thumbnail for the result |  |
|**title** | **String** | *Optional*. Title for the result |  [optional] |
|**type** | **String** | Type of the result, must be *mpeg4\\_gif* |  |



## Enum: ThumbMimeTypeEnum

| Name | Value |
|---- | -----|
| IMAGE_JPEG | &quot;image/jpeg&quot; |
| IMAGE_GIF | &quot;image/gif&quot; |
| VIDEO_MP4 | &quot;video/mp4&quot; |



