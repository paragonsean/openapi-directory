# TelegramBotApi.InlineQueryResultDocument

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**caption** | **String** | *Optional*. Caption of the document to be sent, 0-1024 characters after entities parsing | [optional] 
**captionEntities** | [**[MessageEntity]**](MessageEntity.md) | *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse\\_mode* | [optional] 
**description** | **String** | *Optional*. Short description of the result | [optional] 
**documentUrl** | **String** | A valid URL for the file | 
**id** | **String** | Unique identifier for this result, 1-64 bytes | 
**inputMessageContent** | [**InputMessageContent**](InputMessageContent.md) |  | [optional] 
**mimeType** | **String** | Mime type of the content of the file, either “application/pdf” or “application/zip” | 
**parseMode** | **String** | *Optional*. Mode for parsing entities in the document caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details. | [optional] 
**replyMarkup** | [**InlineKeyboardMarkup**](InlineKeyboardMarkup.md) |  | [optional] 
**thumbHeight** | **Number** | *Optional*. Thumbnail height | [optional] 
**thumbUrl** | **String** | *Optional*. URL of the thumbnail (jpeg only) for the file | [optional] 
**thumbWidth** | **Number** | *Optional*. Thumbnail width | [optional] 
**title** | **String** | Title for the result | 
**type** | **String** | Type of the result, must be *document* | 



## Enum: MimeTypeEnum


* `pdf` (value: `"application/pdf"`)

* `zip` (value: `"application/zip"`)




