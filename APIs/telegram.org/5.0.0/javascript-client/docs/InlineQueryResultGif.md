# TelegramBotApi.InlineQueryResultGif

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**caption** | **String** | *Optional*. Caption of the GIF file to be sent, 0-1024 characters after entities parsing | [optional] 
**captionEntities** | [**[MessageEntity]**](MessageEntity.md) | *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse\\_mode* | [optional] 
**gifDuration** | **Number** | *Optional*. Duration of the GIF | [optional] 
**gifHeight** | **Number** | *Optional*. Height of the GIF | [optional] 
**gifUrl** | **String** | A valid URL for the GIF file. File size must not exceed 1MB | 
**gifWidth** | **Number** | *Optional*. Width of the GIF | [optional] 
**id** | **String** | Unique identifier for this result, 1-64 bytes | 
**inputMessageContent** | [**InputMessageContent**](InputMessageContent.md) |  | [optional] 
**parseMode** | **String** | *Optional*. Mode for parsing entities in the caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details. | [optional] 
**replyMarkup** | [**InlineKeyboardMarkup**](InlineKeyboardMarkup.md) |  | [optional] 
**thumbMimeType** | **String** | *Optional*. MIME type of the thumbnail, must be one of “image/jpeg”, “image/gif”, or “video/mp4”. Defaults to “image/jpeg” | [optional] [default to &#39;image/jpeg&#39;]
**thumbUrl** | **String** | URL of the static (JPEG or GIF) or animated (MPEG4) thumbnail for the result | 
**title** | **String** | *Optional*. Title for the result | [optional] 
**type** | **String** | Type of the result, must be *gif* | 



## Enum: ThumbMimeTypeEnum


* `image/jpeg` (value: `"image/jpeg"`)

* `image/gif` (value: `"image/gif"`)

* `video/mp4` (value: `"video/mp4"`)




