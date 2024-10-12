# TelegramBotApi.CallbackQuery

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chatInstance** | **String** | Global identifier, uniquely corresponding to the chat to which the message with the callback button was sent. Useful for high scores in [games](https://core.telegram.org/bots/api/#games). | 
**data** | **String** | *Optional*. Data associated with the callback button. Be aware that a bad client can send arbitrary data in this field. | [optional] 
**from** | [**User**](User.md) |  | 
**gameShortName** | **String** | *Optional*. Short name of a [Game](https://core.telegram.org/bots/api/#games) to be returned, serves as the unique identifier for the game | [optional] 
**id** | **String** | Unique identifier for this query | 
**inlineMessageId** | **String** | *Optional*. Identifier of the message sent via the bot in inline mode, that originated the query. | [optional] 
**message** | [**Message**](Message.md) |  | [optional] 


