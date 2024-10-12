

# LiveEventInput

The Live Event input.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessControl** | [**LiveEventInputAccessControl**](LiveEventInputAccessControl.md) |  |  [optional] |
|**accessToken** | **String** | A unique identifier for a stream.  This can be specified at creation time but cannot be updated.  If omitted, the service will generate a unique value. |  [optional] |
|**endpoints** | [**List&lt;LiveEventEndpoint&gt;**](LiveEventEndpoint.md) | The input endpoints for the Live Event. |  [optional] |
|**keyFrameIntervalDuration** | **String** | ISO 8601 timespan duration of the key frame interval duration. |  [optional] |
|**streamingProtocol** | [**StreamingProtocolEnum**](#StreamingProtocolEnum) | The streaming protocol for the Live Event.  This is specified at creation time and cannot be updated. |  |



## Enum: StreamingProtocolEnum

| Name | Value |
|---- | -----|
| FRAGMENTED_MP4 | &quot;FragmentedMP4&quot; |
| RTMP | &quot;RTMP&quot; |



