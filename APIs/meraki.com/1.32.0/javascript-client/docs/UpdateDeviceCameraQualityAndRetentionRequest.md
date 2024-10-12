# MerakiDashboardApi.UpdateDeviceCameraQualityAndRetentionRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audioRecordingEnabled** | **Boolean** | Boolean indicating if audio recording is enabled(true) or disabled(false) on the camera | [optional] 
**motionBasedRetentionEnabled** | **Boolean** | Boolean indicating if motion-based retention is enabled(true) or disabled(false) on the camera. | [optional] 
**motionDetectorVersion** | **Number** | The version of the motion detector that will be used by the camera. Only applies to Gen 2 cameras. Defaults to v2. | [optional] 
**profileId** | **String** | The ID of a quality and retention profile to assign to the camera. The profile&#39;s settings will override all of the per-camera quality and retention settings. If the value of this parameter is null, any existing profile will be unassigned from the camera. | [optional] 
**quality** | **String** | Quality of the camera. Can be one of &#39;Standard&#39;, &#39;High&#39; or &#39;Enhanced&#39;. Not all qualities are supported by every camera model. | [optional] 
**resolution** | **String** | Resolution of the camera. Can be one of &#39;1280x720&#39;, &#39;1920x1080&#39;, &#39;1080x1080&#39;, &#39;2058x2058&#39;, &#39;2112x2112&#39;, &#39;2880x2880&#39;, &#39;2688x1512&#39; or &#39;3840x2160&#39;.Not all resolutions are supported by every camera model. | [optional] 
**restrictedBandwidthModeEnabled** | **Boolean** | Boolean indicating if restricted bandwidth is enabled(true) or disabled(false) on the camera. This setting does not apply to MV2 cameras. | [optional] 



## Enum: MotionDetectorVersionEnum


* `1` (value: `1`)

* `2` (value: `2`)





## Enum: QualityEnum


* `Enhanced` (value: `"Enhanced"`)

* `High` (value: `"High"`)

* `Standard` (value: `"Standard"`)





## Enum: ResolutionEnum


* `1080x1080` (value: `"1080x1080"`)

* `1280x720` (value: `"1280x720"`)

* `1920x1080` (value: `"1920x1080"`)

* `2058x2058` (value: `"2058x2058"`)

* `2112x2112` (value: `"2112x2112"`)

* `2688x1512` (value: `"2688x1512"`)

* `2880x2880` (value: `"2880x2880"`)

* `3840x2160` (value: `"3840x2160"`)




