

# LiveEventInput

The Live Event input.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessToken** | **String** | The access token. |  [optional] |
|**endpoints** | [**List&lt;LiveEventEndpoint&gt;**](LiveEventEndpoint.md) | The input endpoints for the Live Event. |  [optional] |
|**keyFrameIntervalDuration** | **String** | ISO 8601 timespan duration of the key frame interval duration. |  [optional] |
|**streamingProtocol** | [**StreamingProtocolEnum**](#StreamingProtocolEnum) | The streaming protocol for the Live Event. |  |



## Enum: StreamingProtocolEnum

| Name | Value |
|---- | -----|
| FRAGMENTED_MP4 | &quot;FragmentedMP4&quot; |
| RTMP | &quot;RTMP&quot; |



