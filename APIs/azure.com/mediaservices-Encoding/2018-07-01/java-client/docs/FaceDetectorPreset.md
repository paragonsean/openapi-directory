

# FaceDetectorPreset

Describes all the settings to be used when analyzing a video in order to detect all the faces present.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**resolution** | [**ResolutionEnum**](#ResolutionEnum) | Specifies the maximum resolution at which your video is analyzed. The default behavior is \&quot;SourceResolution,\&quot; which will keep the input video at its original resolution when analyzed. Using \&quot;StandardDefinition\&quot; will resize input videos to standard definition while preserving the appropriate aspect ratio. It will only resize if the video is of higher resolution. For example, a 1920x1080 input would be scaled to 640x360 before processing. Switching to \&quot;StandardDefinition\&quot; will reduce the time it takes to process high resolution video. It may also reduce the cost of using this component (see https://azure.microsoft.com/en-us/pricing/details/media-services/#analytics for details). However, faces that end up being too small in the resized video may not be detected. |  [optional] |



## Enum: ResolutionEnum

| Name | Value |
|---- | -----|
| SOURCE_RESOLUTION | &quot;SourceResolution&quot; |
| STANDARD_DEFINITION | &quot;StandardDefinition&quot; |



