

# UpdateFlowMediaStreamRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributes** | [**UpdateFlowMediaStreamRequestAttributes**](UpdateFlowMediaStreamRequestAttributes.md) |  |  [optional] |
|**clockRate** | **Integer** | The sample rate (in Hz) for the stream. If the media stream type is video or ancillary data, set this value to 90000. If the media stream type is audio, set this value to either 48000 or 96000. |  [optional] |
|**description** | **String** | Description |  [optional] |
|**mediaStreamType** | [**MediaStreamTypeEnum**](#MediaStreamTypeEnum) | The type of media stream. |  [optional] |
|**videoFormat** | **String** | The resolution of the video. |  [optional] |



## Enum: MediaStreamTypeEnum

| Name | Value |
|---- | -----|
| VIDEO | &quot;video&quot; |
| AUDIO | &quot;audio&quot; |
| ANCILLARY_DATA | &quot;ancillary-data&quot; |



