

# InlineQueryResultVoice

Represents a link to a voice recording in an .OGG container encoded with OPUS. By default, this voice recording will be sent by the user. Alternatively, you can use *input\\_message\\_content* to send a message with the specified content instead of the the voice message.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**caption** | **String** | *Optional*. Caption, 0-1024 characters after entities parsing |  [optional] |
|**captionEntities** | [**List&lt;MessageEntity&gt;**](MessageEntity.md) | *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse\\_mode* |  [optional] |
|**id** | **String** | Unique identifier for this result, 1-64 bytes |  |
|**inputMessageContent** | [**InputMessageContent**](InputMessageContent.md) |  |  [optional] |
|**parseMode** | **String** | *Optional*. Mode for parsing entities in the voice message caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details. |  [optional] |
|**replyMarkup** | [**InlineKeyboardMarkup**](InlineKeyboardMarkup.md) |  |  [optional] |
|**title** | **String** | Recording title |  |
|**type** | **String** | Type of the result, must be *voice* |  |
|**voiceDuration** | **Integer** | *Optional*. Recording duration in seconds |  [optional] |
|**voiceUrl** | **String** | A valid URL for the voice recording |  |



