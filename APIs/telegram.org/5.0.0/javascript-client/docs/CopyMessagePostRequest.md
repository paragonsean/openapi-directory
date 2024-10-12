# TelegramBotApi.CopyMessagePostRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowSendingWithoutReply** | **Boolean** | Pass *True*, if the message should be sent even if the specified replied-to message is not found | [optional] 
**caption** | **String** | New caption for media, 0-1024 characters after entities parsing. If not specified, the original caption is kept | [optional] 
**captionEntities** | [**[MessageEntity]**](MessageEntity.md) | List of special entities that appear in the new caption, which can be specified instead of *parse\\_mode* | [optional] 
**chatId** | [**CopyMessagePostRequestChatId**](CopyMessagePostRequestChatId.md) |  | 
**disableNotification** | **Boolean** | Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound. | [optional] 
**fromChatId** | [**CopyMessagePostRequestFromChatId**](CopyMessagePostRequestFromChatId.md) |  | 
**messageId** | **Number** | Message identifier in the chat specified in *from\\_chat\\_id* | 
**parseMode** | **String** | Mode for parsing entities in the new caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details. | [optional] 
**replyMarkup** | [**CopyMessagePostRequestReplyMarkup**](CopyMessagePostRequestReplyMarkup.md) |  | [optional] 
**replyToMessageId** | **Number** | If the message is a reply, ID of the original message | [optional] 


