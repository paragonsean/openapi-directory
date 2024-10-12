

# ChosenInlineResult

Represents a [result](https://core.telegram.org/bots/api/#inlinequeryresult) of an inline query that was chosen by the user and sent to their chat partner.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**from** | [**User**](User.md) |  |  |
|**inlineMessageId** | **String** | *Optional*. Identifier of the sent inline message. Available only if there is an [inline keyboard](https://core.telegram.org/bots/api/#inlinekeyboardmarkup) attached to the message. Will be also received in [callback queries](https://core.telegram.org/bots/api/#callbackquery) and can be used to [edit](https://core.telegram.org/bots/api/#updating-messages) the message. |  [optional] |
|**location** | [**Location**](Location.md) |  |  [optional] |
|**query** | **String** | The query that was used to obtain the result |  |
|**resultId** | **String** | The unique identifier for the result that was chosen |  |



