# TelegramBotApi.SendMessagePostRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowSendingWithoutReply** | **Boolean** | Pass *True*, if the message should be sent even if the specified replied-to message is not found | [optional] 
**chatId** | [**CopyMessagePostRequestChatId**](CopyMessagePostRequestChatId.md) |  | 
**disableNotification** | **Boolean** | Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound. | [optional] 
**disableWebPagePreview** | **Boolean** | Disables link previews for links in this message | [optional] 
**entities** | [**[MessageEntity]**](MessageEntity.md) | List of special entities that appear in message text, which can be specified instead of *parse\\_mode* | [optional] 
**parseMode** | **String** | Mode for parsing entities in the message text. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details. | [optional] 
**replyMarkup** | [**CopyMessagePostRequestReplyMarkup**](CopyMessagePostRequestReplyMarkup.md) |  | [optional] 
**replyToMessageId** | **Number** | If the message is a reply, ID of the original message | [optional] 
**text** | **String** | Text of the message to be sent, 1-4096 characters after entities parsing | 


