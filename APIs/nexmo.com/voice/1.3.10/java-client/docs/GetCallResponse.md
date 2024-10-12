

# GetCallResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**links** | [**GetCallResponseLinks**](GetCallResponseLinks.md) |  |  [optional] |
|**conversationUuid** | **UUID** | The unique identifier for the conversation this call leg is part of. |  [optional] |
|**direction** | **Direction** |  |  [optional] |
|**duration** | **String** | The time elapsed for the call to take place in seconds. This is only sent if &#x60;status&#x60; is &#x60;completed&#x60;. |  [optional] |
|**endTime** | **String** | The time the call started in the following format: &#x60;YYYY-MM-DD HH:MM:SS&#x60;. For xample, &#x60;2020-01-01 12:00:00&#x60;. This is only sent if &#x60;status&#x60; is &#x60;completed&#x60;. |  [optional] |
|**from** | [**From**](From.md) |  |  [optional] |
|**network** | **String** | The Mobile Country Code Mobile Network Code ([MCCMNC](https://en.wikipedia.org/wiki/Mobile_country_code)) for the carrier network used to make this call. This is only sent if &#x60;status&#x60; is &#x60;completed&#x60;. |  [optional] |
|**price** | **String** | The total price charged for this call. This is only sent if &#x60;status&#x60; is &#x60;completed&#x60;. |  [optional] |
|**rate** | **String** | The price per minute for this call. This is only sent if &#x60;status&#x60; is &#x60;completed&#x60;. |  [optional] |
|**startTime** | **String** | The time the call started in the following format: &#x60;YYYY-MM-DD HH:MM:SS&#x60;. For example, &#x60;2020-01-01 12:00:00&#x60;. This is only sent if &#x60;status&#x60; is &#x60;completed&#x60;. |  [optional] |
|**status** | **String** | The status of the call. [See possible values](https://developer.nexmo.com/voice/voice-api/guides/call-flow#event-objects) |  [optional] |
|**to** | [**To**](To.md) |  |  [optional] |
|**uuid** | **UUID** | The unique identifier for this call leg. The UUID is created when your call request is accepted by Vonage. You use the UUID in all requests for individual live calls |  [optional] |



