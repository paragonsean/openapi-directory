

# KeyboardButton

This object represents one button of the reply keyboard. For simple text buttons *String* can be used instead of this object to specify text of the button. Optional fields *request\\_contact*, *request\\_location*, and *request\\_poll* are mutually exclusive.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**requestContact** | **Boolean** | *Optional*. If *True*, the user&#39;s phone number will be sent as a contact when the button is pressed. Available in private chats only |  [optional] |
|**requestLocation** | **Boolean** | *Optional*. If *True*, the user&#39;s current location will be sent when the button is pressed. Available in private chats only |  [optional] |
|**requestPoll** | [**KeyboardButtonPollType**](KeyboardButtonPollType.md) |  |  [optional] |
|**text** | **String** | Text of the button. If none of the optional fields are used, it will be sent as a message when the button is pressed |  |



