# TelegramBotApi.InlineQueryResultAudio

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audioDuration** | **Number** | *Optional*. Audio duration in seconds | [optional] 
**audioUrl** | **String** | A valid URL for the audio file | 
**caption** | **String** | *Optional*. Caption, 0-1024 characters after entities parsing | [optional] 
**captionEntities** | [**[MessageEntity]**](MessageEntity.md) | *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse\\_mode* | [optional] 
**id** | **String** | Unique identifier for this result, 1-64 bytes | 
**inputMessageContent** | [**InputMessageContent**](InputMessageContent.md) |  | [optional] 
**parseMode** | **String** | *Optional*. Mode for parsing entities in the audio caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details. | [optional] 
**performer** | **String** | *Optional*. Performer | [optional] 
**replyMarkup** | [**InlineKeyboardMarkup**](InlineKeyboardMarkup.md) |  | [optional] 
**title** | **String** | Title | 
**type** | **String** | Type of the result, must be *audio* | 


