# TelegramBotApi.InlineQueryResultVideo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**caption** | **String** | *Optional*. Caption of the video to be sent, 0-1024 characters after entities parsing | [optional] 
**captionEntities** | [**[MessageEntity]**](MessageEntity.md) | *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse\\_mode* | [optional] 
**description** | **String** | *Optional*. Short description of the result | [optional] 
**id** | **String** | Unique identifier for this result, 1-64 bytes | 
**inputMessageContent** | [**InputMessageContent**](InputMessageContent.md) |  | [optional] 
**mimeType** | **String** | Mime type of the content of video url, “text/html” or “video/mp4” | 
**parseMode** | **String** | *Optional*. Mode for parsing entities in the video caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details. | [optional] 
**replyMarkup** | [**InlineKeyboardMarkup**](InlineKeyboardMarkup.md) |  | [optional] 
**thumbUrl** | **String** | URL of the thumbnail (jpeg only) for the video | 
**title** | **String** | Title for the result | 
**type** | **String** | Type of the result, must be *video* | 
**videoDuration** | **Number** | *Optional*. Video duration in seconds | [optional] 
**videoHeight** | **Number** | *Optional*. Video height | [optional] 
**videoUrl** | **String** | A valid URL for the embedded video player or video file | 
**videoWidth** | **Number** | *Optional*. Video width | [optional] 


