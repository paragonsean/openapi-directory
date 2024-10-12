

# SMS


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientRef** | **String** | Client reference of up to 100 characters. The reference will be present in every message status. |  [optional] |
|**messageType** | [**MessageTypeEnum**](#MessageTypeEnum) | The type of message to send. You must provide &#x60;text&#x60; in this field |  |
|**text** | **Object** | The text of message to send; limited to 1000 characters. The Messages API automatically detects unicode characters when sending SMS and sends the message as a unicode SMS. For more information on how concatenation and encoding please visit: [developer.nexmo.com/messaging/sms/guides/concatenation-and-encoding](https://developer.nexmo.com/messaging/sms/guides/concatenation-and-encoding).  |  |
|**channel** | [**ChannelEnum**](#ChannelEnum) | The channel to send to. You must provide &#x60;sms&#x60; in this field |  |
|**from** | **String** | The phone number of the message **sender** in the [E.164](https://en.wikipedia.org/wiki/E.164) format. Don&#39;t use a leading + or 00 when entering a phone number, start with the country code, for example, 447700900000. For SMS in certain localities alpha-numeric sender id&#39;s will work as well, see [Global Messaging](https://developer.nexmo.com/messaging/sms/guides/country-specific-features#country-specific-features) for more details  |  |
|**to** | **String** | The phone number of the message **recipient** in the [E.164](https://en.wikipedia.org/wiki/E.164) format. Don&#39;t use a leading + or 00 when entering a phone number, start with the country code, for example, 447700900000.  |  |



## Enum: MessageTypeEnum

| Name | Value |
|---- | -----|
| TEXT | &quot;text&quot; |



## Enum: ChannelEnum

| Name | Value |
|---- | -----|
| SMS | &quot;sms&quot; |



