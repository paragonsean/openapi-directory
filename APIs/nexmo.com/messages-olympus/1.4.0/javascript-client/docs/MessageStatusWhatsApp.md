# MessagesApi.MessageStatusWhatsApp

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientRef** | **String** | Client reference of up to 100 characters. The reference will be present in every message status. | [optional] 
**error** | [**MessageStatusBaseError**](MessageStatusBaseError.md) |  | [optional] 
**from** | **String** | The phone number of the message **sender** in the [E.164](https://en.wikipedia.org/wiki/E.164) format. Don&#39;t use a leading + or 00 when entering a phone number, start with the country code, for example, 447700900000. For SMS in certain localities alpha-numeric sender id&#39;s will work as well, see [Global Messaging](https://developer.nexmo.com/messaging/sms/guides/country-specific-features#country-specific-features) for more details  | 
**messageUuid** | **String** | The UUID of the message | 
**status** | **String** |  | 
**timestamp** | **String** | The datetime of when the event occurred, in &#x60;ISO 8601&#x60; format. | 
**to** | **String** | The phone number of the message **recipient** in the [E.164](https://en.wikipedia.org/wiki/E.164) format. Don&#39;t use a leading + or 00 when entering a phone number, start with the country code, for example, 447700900000.  | 
**usage** | [**WhatsApp1Usage**](WhatsApp1Usage.md) |  | [optional] 
**channel** | **String** | The channel sending to. | 
**whatsapp** | [**WhatsApp1Whatsapp**](WhatsApp1Whatsapp.md) |  | [optional] 



## Enum: StatusEnum


* `submitted` (value: `"submitted"`)

* `delivered` (value: `"delivered"`)

* `rejected` (value: `"rejected"`)

* `undeliverable` (value: `"undeliverable"`)

* `read` (value: `"read"`)





## Enum: ChannelEnum


* `whatsapp` (value: `"whatsapp"`)




