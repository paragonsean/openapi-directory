# MessagesApi.ChannelOptionsSms

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | **String** | The channel to send to. You must provide &#x60;sms&#x60; in this field | [optional] 
**from** | **String** | The phone number of the message **sender** in the [E.164](https://en.wikipedia.org/wiki/E.164) format. Don&#39;t use a leading + or 00 when entering a phone number, start with the country code, for example, 447700900000. For SMS in certain localities alpha-numeric sender id&#39;s will work as well, see [Global Messaging](https://developer.nexmo.com/messaging/sms/guides/country-specific-features#country-specific-features) for more details  | [optional] 
**to** | **String** | The phone number of the message **recipient** in the [E.164](https://en.wikipedia.org/wiki/E.164) format. Don&#39;t use a leading + or 00 when entering a phone number, start with the country code, for example, 447700900000.  | [optional] 



## Enum: ChannelEnum


* `sms` (value: `"sms"`)




