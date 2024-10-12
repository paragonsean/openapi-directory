# MessagesApi.MMSOneOf

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientRef** | **String** | Client reference of up to 100 characters. The reference will be present in every message status. | [optional] 
**image** | [**MMSOneOfAllOfImage**](MMSOneOfAllOfImage.md) |  | 
**messageType** | **String** | The type of message to send. You must provide &#x60;image&#x60; in this field | 
**channel** | **String** | The channel to send to. You must provide &#x60;mms&#x60; in this field | 
**from** | **String** | The phone number of the message **sender** in the [E.164](https://en.wikipedia.org/wiki/E.164) format. Don&#39;t use a leading + or 00 when entering a phone number, start with the country code, for example, 447700900000. For SMS in certain localities alpha-numeric sender id&#39;s will work as well, see [Global Messaging](https://developer.nexmo.com/messaging/sms/guides/country-specific-features#country-specific-features) for more details  | 
**to** | **String** | The phone number of the message **recipient** in the [E.164](https://en.wikipedia.org/wiki/E.164) format. Don&#39;t use a leading + or 00 when entering a phone number, start with the country code, for example, 447700900000.  | 



## Enum: MessageTypeEnum


* `image` (value: `"image"`)





## Enum: ChannelEnum


* `mms` (value: `"mms"`)




