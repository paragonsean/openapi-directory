# MessagesApi.MessengerOneOf3

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientRef** | **String** | Client reference of up to 100 characters. The reference will be present in every message status. | [optional] 
**messageType** | **String** | The type of message to send. You must provide &#x60;video&#x60; in this field | 
**video** | [**MessengerOneOf3AllOfVideo**](MessengerOneOf3AllOfVideo.md) |  | 
**channel** | **String** | The channel to send to. You must provide &#x60;messenger&#x60; in this field | 
**from** | **String** | The ID of the message sender  | 
**messenger** | [**ChannelOptionsMessengerMessenger**](ChannelOptionsMessengerMessenger.md) |  | [optional] 
**to** | **String** | The ID of the message recipient  | 



## Enum: MessageTypeEnum


* `video` (value: `"video"`)





## Enum: ChannelEnum


* `messenger` (value: `"messenger"`)




