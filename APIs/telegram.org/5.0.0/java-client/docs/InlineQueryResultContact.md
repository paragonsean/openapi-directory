

# InlineQueryResultContact

Represents a contact with a phone number. By default, this contact will be sent by the user. Alternatively, you can use *input\\_message\\_content* to send a message with the specified content instead of the contact.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**firstName** | **String** | Contact&#39;s first name |  |
|**id** | **String** | Unique identifier for this result, 1-64 Bytes |  |
|**inputMessageContent** | [**InputMessageContent**](InputMessageContent.md) |  |  [optional] |
|**lastName** | **String** | *Optional*. Contact&#39;s last name |  [optional] |
|**phoneNumber** | **String** | Contact&#39;s phone number |  |
|**replyMarkup** | [**InlineKeyboardMarkup**](InlineKeyboardMarkup.md) |  |  [optional] |
|**thumbHeight** | **Integer** | *Optional*. Thumbnail height |  [optional] |
|**thumbUrl** | **String** | *Optional*. Url of the thumbnail for the result |  [optional] |
|**thumbWidth** | **Integer** | *Optional*. Thumbnail width |  [optional] |
|**type** | **String** | Type of the result, must be *contact* |  |
|**vcard** | **String** | *Optional*. Additional data about the contact in the form of a [vCard](https://en.wikipedia.org/wiki/VCard), 0-2048 bytes |  [optional] |



