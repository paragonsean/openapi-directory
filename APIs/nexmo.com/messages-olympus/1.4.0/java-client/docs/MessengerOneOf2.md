

# MessengerOneOf2


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientRef** | **String** | Client reference of up to 100 characters. The reference will be present in every message status. |  [optional] |
|**audio** | [**MessengerOneOf2AllOfAudio**](MessengerOneOf2AllOfAudio.md) |  |  |
|**messageType** | [**MessageTypeEnum**](#MessageTypeEnum) | The type of message to send. You must provide &#x60;audio&#x60; in this field |  |
|**channel** | [**ChannelEnum**](#ChannelEnum) | The channel to send to. You must provide &#x60;messenger&#x60; in this field |  |
|**from** | **String** | The ID of the message sender  |  |
|**messenger** | [**ChannelOptionsMessengerMessenger**](ChannelOptionsMessengerMessenger.md) |  |  [optional] |
|**to** | **String** | The ID of the message recipient  |  |



## Enum: MessageTypeEnum

| Name | Value |
|---- | -----|
| AUDIO | &quot;audio&quot; |



## Enum: ChannelEnum

| Name | Value |
|---- | -----|
| MESSENGER | &quot;messenger&quot; |



