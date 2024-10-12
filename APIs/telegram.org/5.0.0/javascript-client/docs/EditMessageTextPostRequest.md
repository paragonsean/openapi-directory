# TelegramBotApi.EditMessageTextPostRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chatId** | [**EditMessageCaptionPostRequestChatId**](EditMessageCaptionPostRequestChatId.md) |  | [optional] 
**disableWebPagePreview** | **Boolean** | Disables link previews for links in this message | [optional] 
**entities** | [**[MessageEntity]**](MessageEntity.md) | List of special entities that appear in message text, which can be specified instead of *parse\\_mode* | [optional] 
**inlineMessageId** | **String** | Required if *chat\\_id* and *message\\_id* are not specified. Identifier of the inline message | [optional] 
**messageId** | **Number** | Required if *inline\\_message\\_id* is not specified. Identifier of the message to edit | [optional] 
**parseMode** | **String** | Mode for parsing entities in the message text. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details. | [optional] 
**replyMarkup** | [**InlineKeyboardMarkup**](InlineKeyboardMarkup.md) |  | [optional] 
**text** | **String** | New text of the message, 1-4096 characters after entities parsing | 


