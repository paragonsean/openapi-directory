# MessagesApi.ViberOneOf2

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientRef** | **String** | Client reference of up to 100 characters. The reference will be present in every message status. | [optional] 
**messageType** | **String** | The type of message to send. You must provide &#x60;video&#x60; in this field | 
**video** | [**ViberOneOf2AllOfVideo**](ViberOneOf2AllOfVideo.md) |  | 
**channel** | **String** | The channel to send to. You must provide &#x60;viber_service&#x60; in this field | 
**from** | **String** | The ID of the message sender  | 
**to** | **String** | The phone number of the message **recipient** in the [E.164](https://en.wikipedia.org/wiki/E.164) format. Don&#39;t use a leading + or 00 when entering a phone number, start with the country code, for example, 447700900000.  | 
**viberService** | [**ChannelOptionsViberVideoViberService**](ChannelOptionsViberVideoViberService.md) |  | [optional] 



## Enum: MessageTypeEnum


* `video` (value: `"video"`)





## Enum: ChannelEnum


* `viber_service` (value: `"viber_service"`)




