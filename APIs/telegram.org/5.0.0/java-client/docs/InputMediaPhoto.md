

# InputMediaPhoto

Represents a photo to be sent.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**caption** | **String** | *Optional*. Caption of the photo to be sent, 0-1024 characters after entities parsing |  [optional] |
|**captionEntities** | [**List&lt;MessageEntity&gt;**](MessageEntity.md) | *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse\\_mode* |  [optional] |
|**media** | **String** | File to send. Pass a file\\_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://&lt;file\\_attach\\_name&gt;” to upload a new one using multipart/form-data under &lt;file\\_attach\\_name&gt; name. [More info on Sending Files »](https://core.telegram.org/bots/api/#sending-files) |  |
|**parseMode** | **String** | *Optional*. Mode for parsing entities in the photo caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details. |  [optional] |
|**type** | **String** | Type of the result, must be *photo* |  |



