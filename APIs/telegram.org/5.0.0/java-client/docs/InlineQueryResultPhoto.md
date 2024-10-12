

# InlineQueryResultPhoto

Represents a link to a photo. By default, this photo will be sent by the user with optional caption. Alternatively, you can use *input\\_message\\_content* to send a message with the specified content instead of the photo.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**caption** | **String** | *Optional*. Caption of the photo to be sent, 0-1024 characters after entities parsing |  [optional] |
|**captionEntities** | [**List&lt;MessageEntity&gt;**](MessageEntity.md) | *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse\\_mode* |  [optional] |
|**description** | **String** | *Optional*. Short description of the result |  [optional] |
|**id** | **String** | Unique identifier for this result, 1-64 bytes |  |
|**inputMessageContent** | [**InputMessageContent**](InputMessageContent.md) |  |  [optional] |
|**parseMode** | **String** | *Optional*. Mode for parsing entities in the photo caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details. |  [optional] |
|**photoHeight** | **Integer** | *Optional*. Height of the photo |  [optional] |
|**photoUrl** | **String** | A valid URL of the photo. Photo must be in **jpeg** format. Photo size must not exceed 5MB |  |
|**photoWidth** | **Integer** | *Optional*. Width of the photo |  [optional] |
|**replyMarkup** | [**InlineKeyboardMarkup**](InlineKeyboardMarkup.md) |  |  [optional] |
|**thumbUrl** | **String** | URL of the thumbnail for the photo |  |
|**title** | **String** | *Optional*. Title for the result |  [optional] |
|**type** | **String** | Type of the result, must be *photo* |  |



