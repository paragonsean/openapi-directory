

# CdnSettings

Brief description of the live stream cdn settings.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**format** | **String** | The format of the video stream that you are sending to Youtube.  |  [optional] |
|**frameRate** | [**FrameRateEnum**](#FrameRateEnum) | The frame rate of the inbound video data. |  [optional] |
|**ingestionInfo** | [**IngestionInfo**](IngestionInfo.md) |  |  [optional] |
|**ingestionType** | [**IngestionTypeEnum**](#IngestionTypeEnum) |  The method or protocol used to transmit the video stream. |  [optional] |
|**resolution** | [**ResolutionEnum**](#ResolutionEnum) | The resolution of the inbound video data. |  [optional] |



## Enum: FrameRateEnum

| Name | Value |
|---- | -----|
| _30FPS | &quot;30fps&quot; |
| _60FPS | &quot;60fps&quot; |
| VARIABLE | &quot;variable&quot; |



## Enum: IngestionTypeEnum

| Name | Value |
|---- | -----|
| RTMP | &quot;rtmp&quot; |
| DASH | &quot;dash&quot; |
| WEBRTC | &quot;webrtc&quot; |
| HLS | &quot;hls&quot; |



## Enum: ResolutionEnum

| Name | Value |
|---- | -----|
| _240P | &quot;240p&quot; |
| _360P | &quot;360p&quot; |
| _480P | &quot;480p&quot; |
| _720P | &quot;720p&quot; |
| _1080P | &quot;1080p&quot; |
| _1440P | &quot;1440p&quot; |
| _2160P | &quot;2160p&quot; |
| VARIABLE | &quot;variable&quot; |



