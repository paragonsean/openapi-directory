

# ChannelFrom


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | **String** | The type of connection. Must be &#x60;vbc&#x60; |  |
|**user** | **String** | The username to connect to |  |
|**number** | **String** | The phone number to connect to |  |
|**uri** | **String** |  |  [optional] |
|**contentType** | [**ContentTypeEnum**](#ContentTypeEnum) |  |  |
|**headers** | [**ChannelFromOneOf3Headers**](ChannelFromOneOf3Headers.md) |  |  [optional] |
|**extension** | **String** |  |  |



## Enum: ContentTypeEnum

| Name | Value |
|---- | -----|
| _8000 | &quot;audio/l16;rate&#x3D;8000&quot; |
| _16000 | &quot;audio/l16;rate&#x3D;16000&quot; |



