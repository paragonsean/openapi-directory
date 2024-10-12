

# InlineQueryResultVideo

Represents a link to a page containing an embedded video player or a video file. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use *input\\_message\\_content* to send a message with the specified content instead of the video.  If an InlineQueryResultVideo message contains an embedded video (e.g., YouTube), you **must** replace its content using *input\\_message\\_content*.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**caption** | **String** | *Optional*. Caption of the video to be sent, 0-1024 characters after entities parsing |  [optional] |
|**captionEntities** | [**List&lt;MessageEntity&gt;**](MessageEntity.md) | *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse\\_mode* |  [optional] |
|**description** | **String** | *Optional*. Short description of the result |  [optional] |
|**id** | **String** | Unique identifier for this result, 1-64 bytes |  |
|**inputMessageContent** | [**InputMessageContent**](InputMessageContent.md) |  |  [optional] |
|**mimeType** | **String** | Mime type of the content of video url, “text/html” or “video/mp4” |  |
|**parseMode** | **String** | *Optional*. Mode for parsing entities in the video caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details. |  [optional] |
|**replyMarkup** | [**InlineKeyboardMarkup**](InlineKeyboardMarkup.md) |  |  [optional] |
|**thumbUrl** | **String** | URL of the thumbnail (jpeg only) for the video |  |
|**title** | **String** | Title for the result |  |
|**type** | **String** | Type of the result, must be *video* |  |
|**videoDuration** | **Integer** | *Optional*. Video duration in seconds |  [optional] |
|**videoHeight** | **Integer** | *Optional*. Video height |  [optional] |
|**videoUrl** | **String** | A valid URL for the embedded video player or video file |  |
|**videoWidth** | **Integer** | *Optional*. Video width |  [optional] |



