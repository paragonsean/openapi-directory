# MessagesApi.ViberOneOf3

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientRef** | **String** | Client reference of up to 100 characters. The reference will be present in every message status. | [optional] 
**file** | [**ViberOneOf3AllOfFile**](ViberOneOf3AllOfFile.md) |  | 
**messageType** | **String** | The type of message to send. You must provide &#x60;file&#x60; in this field | 
**channel** | **String** | The channel to send to. You must provide &#x60;viber_service&#x60; in this field | 
**from** | **String** | The ID of the message sender  | 
**to** | **String** | The phone number of the message **recipient** in the [E.164](https://en.wikipedia.org/wiki/E.164) format. Don&#39;t use a leading + or 00 when entering a phone number, start with the country code, for example, 447700900000.  | 
**viberService** | [**ChannelOptionsViberViberService**](ChannelOptionsViberViberService.md) |  | [optional] 



## Enum: MessageTypeEnum


* `file` (value: `"file"`)





## Enum: ChannelEnum


* `viber_service` (value: `"viber_service"`)




