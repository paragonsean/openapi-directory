

# UpdateDeviceCameraQualityAndRetentionRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**audioRecordingEnabled** | **Boolean** | Boolean indicating if audio recording is enabled(true) or disabled(false) on the camera |  [optional] |
|**motionBasedRetentionEnabled** | **Boolean** | Boolean indicating if motion-based retention is enabled(true) or disabled(false) on the camera. |  [optional] |
|**motionDetectorVersion** | [**MotionDetectorVersionEnum**](#MotionDetectorVersionEnum) | The version of the motion detector that will be used by the camera. Only applies to Gen 2 cameras. Defaults to v2. |  [optional] |
|**profileId** | **String** | The ID of a quality and retention profile to assign to the camera. The profile&#39;s settings will override all of the per-camera quality and retention settings. If the value of this parameter is null, any existing profile will be unassigned from the camera. |  [optional] |
|**quality** | [**QualityEnum**](#QualityEnum) | Quality of the camera. Can be one of &#39;Standard&#39;, &#39;High&#39; or &#39;Enhanced&#39;. Not all qualities are supported by every camera model. |  [optional] |
|**resolution** | [**ResolutionEnum**](#ResolutionEnum) | Resolution of the camera. Can be one of &#39;1280x720&#39;, &#39;1920x1080&#39;, &#39;1080x1080&#39;, &#39;2058x2058&#39;, &#39;2112x2112&#39;, &#39;2880x2880&#39;, &#39;2688x1512&#39; or &#39;3840x2160&#39;.Not all resolutions are supported by every camera model. |  [optional] |
|**restrictedBandwidthModeEnabled** | **Boolean** | Boolean indicating if restricted bandwidth is enabled(true) or disabled(false) on the camera. This setting does not apply to MV2 cameras. |  [optional] |



## Enum: MotionDetectorVersionEnum

| Name | Value |
|---- | -----|
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |



## Enum: QualityEnum

| Name | Value |
|---- | -----|
| ENHANCED | &quot;Enhanced&quot; |
| HIGH | &quot;High&quot; |
| STANDARD | &quot;Standard&quot; |



## Enum: ResolutionEnum

| Name | Value |
|---- | -----|
| _1080X1080 | &quot;1080x1080&quot; |
| _1280X720 | &quot;1280x720&quot; |
| _1920X1080 | &quot;1920x1080&quot; |
| _2058X2058 | &quot;2058x2058&quot; |
| _2112X2112 | &quot;2112x2112&quot; |
| _2688X1512 | &quot;2688x1512&quot; |
| _2880X2880 | &quot;2880x2880&quot; |
| _3840X2160 | &quot;3840x2160&quot; |



