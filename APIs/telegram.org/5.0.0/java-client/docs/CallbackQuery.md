

# CallbackQuery

This object represents an incoming callback query from a callback button in an [inline keyboard](/bots#inline-keyboards-and-on-the-fly-updating). If the button that originated the query was attached to a message sent by the bot, the field *message* will be present. If the button was attached to a message sent via the bot (in [inline mode](https://core.telegram.org/bots/api/#inline-mode)), the field *inline\\_message\\_id* will be present. Exactly one of the fields *data* or *game\\_short\\_name* will be present.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**chatInstance** | **String** | Global identifier, uniquely corresponding to the chat to which the message with the callback button was sent. Useful for high scores in [games](https://core.telegram.org/bots/api/#games). |  |
|**data** | **String** | *Optional*. Data associated with the callback button. Be aware that a bad client can send arbitrary data in this field. |  [optional] |
|**from** | [**User**](User.md) |  |  |
|**gameShortName** | **String** | *Optional*. Short name of a [Game](https://core.telegram.org/bots/api/#games) to be returned, serves as the unique identifier for the game |  [optional] |
|**id** | **String** | Unique identifier for this query |  |
|**inlineMessageId** | **String** | *Optional*. Identifier of the message sent via the bot in inline mode, that originated the query. |  [optional] |
|**message** | [**Message**](Message.md) |  |  [optional] |



