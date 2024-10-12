

# InlineQueryResultDocument

Represents a link to a file. By default, this file will be sent by the user with an optional caption. Alternatively, you can use *input\\_message\\_content* to send a message with the specified content instead of the file. Currently, only **.PDF** and **.ZIP** files can be sent using this method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**caption** | **String** | *Optional*. Caption of the document to be sent, 0-1024 characters after entities parsing |  [optional] |
|**captionEntities** | [**List&lt;MessageEntity&gt;**](MessageEntity.md) | *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse\\_mode* |  [optional] |
|**description** | **String** | *Optional*. Short description of the result |  [optional] |
|**documentUrl** | **String** | A valid URL for the file |  |
|**id** | **String** | Unique identifier for this result, 1-64 bytes |  |
|**inputMessageContent** | [**InputMessageContent**](InputMessageContent.md) |  |  [optional] |
|**mimeType** | [**MimeTypeEnum**](#MimeTypeEnum) | Mime type of the content of the file, either “application/pdf” or “application/zip” |  |
|**parseMode** | **String** | *Optional*. Mode for parsing entities in the document caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details. |  [optional] |
|**replyMarkup** | [**InlineKeyboardMarkup**](InlineKeyboardMarkup.md) |  |  [optional] |
|**thumbHeight** | **Integer** | *Optional*. Thumbnail height |  [optional] |
|**thumbUrl** | **String** | *Optional*. URL of the thumbnail (jpeg only) for the file |  [optional] |
|**thumbWidth** | **Integer** | *Optional*. Thumbnail width |  [optional] |
|**title** | **String** | Title for the result |  |
|**type** | **String** | Type of the result, must be *document* |  |



## Enum: MimeTypeEnum

| Name | Value |
|---- | -----|
| PDF | &quot;application/pdf&quot; |
| ZIP | &quot;application/zip&quot; |



