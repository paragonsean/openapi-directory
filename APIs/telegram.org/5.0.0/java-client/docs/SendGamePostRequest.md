

# SendGamePostRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowSendingWithoutReply** | **Boolean** | Pass *True*, if the message should be sent even if the specified replied-to message is not found |  [optional] |
|**chatId** | **Integer** | Unique identifier for the target chat |  |
|**disableNotification** | **Boolean** | Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound. |  [optional] |
|**gameShortName** | **String** | Short name of the game, serves as the unique identifier for the game. Set up your games via [Botfather](https://t.me/botfather). |  |
|**replyMarkup** | [**InlineKeyboardMarkup**](InlineKeyboardMarkup.md) |  |  [optional] |
|**replyToMessageId** | **Integer** | If the message is a reply, ID of the original message |  [optional] |



