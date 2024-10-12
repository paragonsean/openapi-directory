# MessagesApi.SendMessageRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientRef** | **String** | Client reference of up to 100 characters. The reference will be present in every message status. | [optional] 
**messageType** | **String** | The type of message to send. You must provide &#x60;file&#x60; in this field | 
**text** | **Object** | The text of message to send; limited to 1000 characters, including unicode.  | 
**channel** | **String** | The channel to send to. You must provide &#x60;viber_service&#x60; in this field | 
**from** | **String** | The ID of the message sender  | 
**to** | **String** | The phone number of the message **recipient** in the [E.164](https://en.wikipedia.org/wiki/E.164) format. Don&#39;t use a leading + or 00 when entering a phone number, start with the country code, for example, 447700900000.  | 
**image** | [**ViberOneOf1AllOfImage**](ViberOneOf1AllOfImage.md) |  | 
**vcard** | [**MMSOneOf1AllOfVcard**](MMSOneOf1AllOfVcard.md) |  | 
**audio** | [**MessengerOneOf2AllOfAudio**](MessengerOneOf2AllOfAudio.md) |  | 
**video** | [**ViberOneOf2AllOfVideo**](ViberOneOf2AllOfVideo.md) |  | 
**location** | [**Location1Location**](Location1Location.md) |  | 
**file** | [**ViberOneOf3AllOfFile**](ViberOneOf3AllOfFile.md) |  | 
**template** | [**Template1Template**](Template1Template.md) |  | 
**whatsapp** | [**WhatsAppOneOf6AllOfWhatsapp**](WhatsAppOneOf6AllOfWhatsapp.md) |  | 
**custom** | **{String: Object}** | A custom payload, which is passed directly to WhatsApp for certain features such as templates and interactive messages. The schema of a custom object can vary widely. [Read more about Custom Objects](https://developer.vonage.com/messages/concepts/custom-objects). | [optional] 
**messenger** | [**ChannelOptionsMessengerMessenger**](ChannelOptionsMessengerMessenger.md) |  | [optional] 
**viberService** | [**ChannelOptionsViberViberService**](ChannelOptionsViberViberService.md) |  | [optional] 



## Enum: MessageTypeEnum


* `file` (value: `"file"`)





## Enum: ChannelEnum


* `viber_service` (value: `"viber_service"`)




