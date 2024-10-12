

# PlayProgressiveInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdTime** | **String** | The time in ISO 8601 format when this video file was created. |  |
|**fps** | **BigDecimal** | The FPS of the video file. |  |
|**height** | **BigDecimal** | The height in pixels of the video. |  |
|**link** | **String** | The direct link to this video file. |  |
|**linkExpirationTime** | **String** | The time in ISO 8601 format when the link to this video file expires. |  |
|**log** | **Object** | The URLs for logging events. |  [optional] |
|**md5** | **String** | The MD5 hash of the video file. |  |
|**size** | **BigDecimal** | The file size in bytes of this video. |  |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the video file:  Option descriptions:  * &#x60;source&#x60; - The video is a source file.  * &#x60;video/mp4&#x60; - The video is in MP4 format.  * &#x60;video/webm&#x60; - The video is in WebM format.  * &#x60;vp6/x-video&#x60; - The video is in VP6 format.  |  |
|**width** | **BigDecimal** | The width in pixels of the video. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| SOURCE | &quot;source&quot; |
| VIDEO_MP4 | &quot;video/mp4&quot; |
| VIDEO_WEBM | &quot;video/webm&quot; |
| VP6_X_VIDEO | &quot;vp6/x-video&quot; |



