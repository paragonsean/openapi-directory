

# InputTextMessageContent

Represents the [content](https://core.telegram.org/bots/api/#inputmessagecontent) of a text message to be sent as the result of an inline query.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**disableWebPagePreview** | **Boolean** | *Optional*. Disables link previews for links in the sent message |  [optional] |
|**entities** | [**List&lt;MessageEntity&gt;**](MessageEntity.md) | *Optional*. List of special entities that appear in message text, which can be specified instead of *parse\\_mode* |  [optional] |
|**messageText** | **String** | Text of the message to be sent, 1-4096 characters |  |
|**parseMode** | **String** | *Optional*. Mode for parsing entities in the message text. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details. |  [optional] |



