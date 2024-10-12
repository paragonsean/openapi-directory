

# ChannelOptionsViber


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**channel** | [**ChannelEnum**](#ChannelEnum) | The channel to send to. You must provide &#x60;viber_service&#x60; in this field |  [optional] |
|**from** | **String** | The ID of the message sender  |  [optional] |
|**to** | **String** | The phone number of the message **recipient** in the [E.164](https://en.wikipedia.org/wiki/E.164) format. Don&#39;t use a leading + or 00 when entering a phone number, start with the country code, for example, 447700900000.  |  [optional] |
|**viberService** | [**ChannelOptionsViberViberService**](ChannelOptionsViberViberService.md) |  |  [optional] |



## Enum: ChannelEnum

| Name | Value |
|---- | -----|
| VIBER_SERVICE | &quot;viber_service&quot; |



