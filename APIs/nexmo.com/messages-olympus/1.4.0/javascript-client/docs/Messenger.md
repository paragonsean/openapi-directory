# MessagesApi.Messenger

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientRef** | **String** | Client reference of up to 100 characters. The reference will be present in every message status. | [optional] 
**messageType** | **String** | The type of message to send. You must provide &#x60;file&#x60; in this field | 
**text** | **Object** | The text of message to send; limited to 640 characters, including unicode.  | 
**channel** | **String** | The channel to send to. You must provide &#x60;messenger&#x60; in this field | 
**from** | **String** | The ID of the message sender  | 
**messenger** | [**ChannelOptionsMessengerMessenger**](ChannelOptionsMessengerMessenger.md) |  | [optional] 
**to** | **String** | The ID of the message recipient  | 
**image** | [**MessengerOneOf1AllOfImage**](MessengerOneOf1AllOfImage.md) |  | 
**audio** | [**MessengerOneOf2AllOfAudio**](MessengerOneOf2AllOfAudio.md) |  | 
**video** | [**MessengerOneOf3AllOfVideo**](MessengerOneOf3AllOfVideo.md) |  | 
**file** | [**MessengerOneOf4AllOfFile**](MessengerOneOf4AllOfFile.md) |  | 



## Enum: MessageTypeEnum


* `file` (value: `"file"`)





## Enum: ChannelEnum


* `messenger` (value: `"messenger"`)




