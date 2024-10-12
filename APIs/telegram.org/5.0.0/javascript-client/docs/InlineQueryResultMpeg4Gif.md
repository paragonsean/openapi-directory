# TelegramBotApi.InlineQueryResultMpeg4Gif

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**caption** | **String** | *Optional*. Caption of the MPEG-4 file to be sent, 0-1024 characters after entities parsing | [optional] 
**captionEntities** | [**[MessageEntity]**](MessageEntity.md) | *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse\\_mode* | [optional] 
**id** | **String** | Unique identifier for this result, 1-64 bytes | 
**inputMessageContent** | [**InputMessageContent**](InputMessageContent.md) |  | [optional] 
**mpeg4Duration** | **Number** | *Optional*. Video duration | [optional] 
**mpeg4Height** | **Number** | *Optional*. Video height | [optional] 
**mpeg4Url** | **String** | A valid URL for the MP4 file. File size must not exceed 1MB | 
**mpeg4Width** | **Number** | *Optional*. Video width | [optional] 
**parseMode** | **String** | *Optional*. Mode for parsing entities in the caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details. | [optional] 
**replyMarkup** | [**InlineKeyboardMarkup**](InlineKeyboardMarkup.md) |  | [optional] 
**thumbMimeType** | **String** | *Optional*. MIME type of the thumbnail, must be one of “image/jpeg”, “image/gif”, or “video/mp4”. Defaults to “image/jpeg” | [optional] [default to &#39;image/jpeg&#39;]
**thumbUrl** | **String** | URL of the static (JPEG or GIF) or animated (MPEG4) thumbnail for the result | 
**title** | **String** | *Optional*. Title for the result | [optional] 
**type** | **String** | Type of the result, must be *mpeg4\\_gif* | 



## Enum: ThumbMimeTypeEnum


* `image/jpeg` (value: `"image/jpeg"`)

* `image/gif` (value: `"image/gif"`)

* `video/mp4` (value: `"video/mp4"`)




