

# InboundMessageMMS


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**channel** | [**ChannelEnum**](#ChannelEnum) | The channel the message came in on |  |
|**from** | **String** | The phone number of the message **sender** in the [E.164](https://en.wikipedia.org/wiki/E.164) format. Don&#39;t use a leading + or 00 when entering a phone number, start with the country code, for example, 447700900000. For SMS in certain localities alpha-numeric sender id&#39;s will work as well, see [Global Messaging](https://developer.nexmo.com/messaging/sms/guides/country-specific-features#country-specific-features) for more details  |  |
|**messageUuid** | **String** | The UUID of the message |  |
|**timestamp** | **String** | The datetime of when the event occurred, in &#x60;ISO 8601&#x60; format. |  |
|**to** | **String** | The phone number of the message **recipient** in the [E.164](https://en.wikipedia.org/wiki/E.164) format. Don&#39;t use a leading + or 00 when entering a phone number, start with the country code, for example, 447700900000.  |  |



## Enum: ChannelEnum

| Name | Value |
|---- | -----|
| MMS | &quot;mms&quot; |



