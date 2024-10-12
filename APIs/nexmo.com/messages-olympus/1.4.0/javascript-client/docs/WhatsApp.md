# MessagesApi.WhatsApp

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientRef** | **String** | Client reference of up to 100 characters. The reference will be present in every message status. | [optional] 
**messageType** | **String** | The type of message to send. You must provide &#x60;custom&#x60; in this field | 
**text** | **Object** | The location to be sent in the message.  | 
**channel** | **String** | The channel to send to. You must provide &#x60;whatsapp&#x60; in this field | 
**from** | **String** | The phone number of the message **sender** in the [E.164](https://en.wikipedia.org/wiki/E.164) format. Don&#39;t use a leading + or 00 when entering a phone number, start with the country code, for example, 447700900000. For SMS in certain localities alpha-numeric sender id&#39;s will work as well, see [Global Messaging](https://developer.nexmo.com/messaging/sms/guides/country-specific-features#country-specific-features) for more details  | 
**to** | **String** | The phone number of the message **recipient** in the [E.164](https://en.wikipedia.org/wiki/E.164) format. Don&#39;t use a leading + or 00 when entering a phone number, start with the country code, for example, 447700900000.  | 
**location** | [**Location1Location**](Location1Location.md) |  | 
**image** | [**WhatsAppOneOf2AllOfImage**](WhatsAppOneOf2AllOfImage.md) |  | 
**audio** | [**WhatsAppOneOf3AllOfAudio**](WhatsAppOneOf3AllOfAudio.md) |  | 
**video** | [**WhatsAppOneOf4AllOfVideo**](WhatsAppOneOf4AllOfVideo.md) |  | 
**file** | [**WhatsAppOneOf5AllOfFile**](WhatsAppOneOf5AllOfFile.md) |  | 
**template** | [**Template1Template**](Template1Template.md) |  | 
**whatsapp** | [**WhatsAppOneOf6AllOfWhatsapp**](WhatsAppOneOf6AllOfWhatsapp.md) |  | 
**custom** | **{String: Object}** | A custom payload, which is passed directly to WhatsApp for certain features such as templates and interactive messages. The schema of a custom object can vary widely. [Read more about Custom Objects](https://developer.vonage.com/messages/concepts/custom-objects). | [optional] 



## Enum: MessageTypeEnum


* `custom` (value: `"custom"`)





## Enum: ChannelEnum


* `whatsapp` (value: `"whatsapp"`)




