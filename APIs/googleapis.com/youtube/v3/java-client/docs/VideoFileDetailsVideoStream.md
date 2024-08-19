

# VideoFileDetailsVideoStream

Information about a video stream.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aspectRatio** | **Double** | The video content&#39;s display aspect ratio, which specifies the aspect ratio in which the video should be displayed. |  [optional] |
|**bitrateBps** | **String** | The video stream&#39;s bitrate, in bits per second. |  [optional] |
|**codec** | **String** | The video codec that the stream uses. |  [optional] |
|**frameRateFps** | **Double** | The video stream&#39;s frame rate, in frames per second. |  [optional] |
|**heightPixels** | **Integer** | The encoded video content&#39;s height in pixels. |  [optional] |
|**rotation** | [**RotationEnum**](#RotationEnum) | The amount that YouTube needs to rotate the original source content to properly display the video. |  [optional] |
|**vendor** | **String** | A value that uniquely identifies a video vendor. Typically, the value is a four-letter vendor code. |  [optional] |
|**widthPixels** | **Integer** | The encoded video content&#39;s width in pixels. You can calculate the video&#39;s encoding aspect ratio as width_pixels / height_pixels. |  [optional] |



## Enum: RotationEnum

| Name | Value |
|---- | -----|
| NONE | &quot;none&quot; |
| CLOCKWISE | &quot;clockwise&quot; |
| UPSIDE_DOWN | &quot;upsideDown&quot; |
| COUNTER_CLOCKWISE | &quot;counterClockwise&quot; |
| OTHER | &quot;other&quot; |



