

# Video

A PageElement kind representing a video.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | The video source&#39;s unique identifier for this video. |  [optional] |
|**source** | [**SourceEnum**](#SourceEnum) | The video source. |  [optional] |
|**url** | **String** | An URL to a video. The URL is valid as long as the source video exists and sharing settings do not change. |  [optional] |
|**videoProperties** | [**VideoProperties**](VideoProperties.md) |  |  [optional] |



## Enum: SourceEnum

| Name | Value |
|---- | -----|
| SOURCE_UNSPECIFIED | &quot;SOURCE_UNSPECIFIED&quot; |
| YOUTUBE | &quot;YOUTUBE&quot; |
| DRIVE | &quot;DRIVE&quot; |



