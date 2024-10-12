# VoiceApi.CreateCallRequestBaseToInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dtmfAnswer** | **String** | Provide [DTMF digits](https://developer.nexmo.com/voice/voice-api/guides/dtmf) to send when the call is answered | [optional] 
**number** | **String** | The phone number to connect to | 
**type** | **String** | The type of connection. Must be &#x60;vbc&#x60; | 
**uri** | **String** |  | [optional] 
**contentType** | **String** |  | 
**headers** | [**EndpointWebsocketHeaders**](EndpointWebsocketHeaders.md) |  | [optional] 
**extension** | **String** |  | 



## Enum: ContentTypeEnum


* `8000` (value: `"audio/l16;rate=8000"`)

* `16000` (value: `"audio/l16;rate=16000"`)




