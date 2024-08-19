# YouTubeDataApiV3.Cuepoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cueType** | **String** |  | [optional] 
**durationSecs** | **Number** | The duration of this cuepoint. | [optional] 
**etag** | **String** |  | [optional] 
**id** | **String** | The identifier for cuepoint resource. | [optional] 
**insertionOffsetTimeMs** | **String** | The time when the cuepoint should be inserted by offset to the broadcast actual start time. | [optional] 
**walltimeMs** | **String** | The wall clock time at which the cuepoint should be inserted. Only one of insertion_offset_time_ms and walltime_ms may be set at a time. | [optional] 



## Enum: CueTypeEnum


* `cueTypeUnspecified` (value: `"cueTypeUnspecified"`)

* `cueTypeAd` (value: `"cueTypeAd"`)




