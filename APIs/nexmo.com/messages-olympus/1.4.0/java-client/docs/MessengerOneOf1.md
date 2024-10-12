

# MessengerOneOf1


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientRef** | **String** | Client reference of up to 100 characters. The reference will be present in every message status. |  [optional] |
|**image** | [**MessengerOneOf1AllOfImage**](MessengerOneOf1AllOfImage.md) |  |  |
|**messageType** | [**MessageTypeEnum**](#MessageTypeEnum) | The type of message to send. You must provide &#x60;image&#x60; in this field |  |
|**channel** | [**ChannelEnum**](#ChannelEnum) | The channel to send to. You must provide &#x60;messenger&#x60; in this field |  |
|**from** | **String** | The ID of the message sender  |  |
|**messenger** | [**ChannelOptionsMessengerMessenger**](ChannelOptionsMessengerMessenger.md) |  |  [optional] |
|**to** | **String** | The ID of the message recipient  |  |



## Enum: MessageTypeEnum

| Name | Value |
|---- | -----|
| IMAGE | &quot;image&quot; |



## Enum: ChannelEnum

| Name | Value |
|---- | -----|
| MESSENGER | &quot;messenger&quot; |



