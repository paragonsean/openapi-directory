

# CreateCallRequestBaseToInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dtmfAnswer** | **String** | Provide [DTMF digits](https://developer.nexmo.com/voice/voice-api/guides/dtmf) to send when the call is answered |  [optional] |
|**number** | **String** | The phone number to connect to |  |
|**type** | **String** | The type of connection. Must be &#x60;vbc&#x60; |  |
|**uri** | **String** |  |  [optional] |
|**contentType** | [**ContentTypeEnum**](#ContentTypeEnum) |  |  |
|**headers** | [**EndpointWebsocketHeaders**](EndpointWebsocketHeaders.md) |  |  [optional] |
|**extension** | **String** |  |  |



## Enum: ContentTypeEnum

| Name | Value |
|---- | -----|
| _8000 | &quot;audio/l16;rate&#x3D;8000&quot; |
| _16000 | &quot;audio/l16;rate&#x3D;16000&quot; |



