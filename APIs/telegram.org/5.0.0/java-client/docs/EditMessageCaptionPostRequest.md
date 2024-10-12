

# EditMessageCaptionPostRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**caption** | **String** | New caption of the message, 0-1024 characters after entities parsing |  [optional] |
|**captionEntities** | [**List&lt;MessageEntity&gt;**](MessageEntity.md) | List of special entities that appear in the caption, which can be specified instead of *parse\\_mode* |  [optional] |
|**chatId** | [**EditMessageCaptionPostRequestChatId**](EditMessageCaptionPostRequestChatId.md) |  |  [optional] |
|**inlineMessageId** | **String** | Required if *chat\\_id* and *message\\_id* are not specified. Identifier of the inline message |  [optional] |
|**messageId** | **Integer** | Required if *inline\\_message\\_id* is not specified. Identifier of the message to edit |  [optional] |
|**parseMode** | **String** | Mode for parsing entities in the message caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details. |  [optional] |
|**replyMarkup** | [**InlineKeyboardMarkup**](InlineKeyboardMarkup.md) |  |  [optional] |



