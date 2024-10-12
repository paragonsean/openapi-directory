

# Cuepoint

Note that there may be a 5-second end-point resolution issue. For instance, if a cuepoint comes in for 22:03:27, we may stuff the cuepoint into 22:03:25 or 22:03:30, depending. This is an artifact of HLS.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cueType** | [**CueTypeEnum**](#CueTypeEnum) |  |  [optional] |
|**durationSecs** | **Integer** | The duration of this cuepoint. |  [optional] |
|**etag** | **String** |  |  [optional] |
|**id** | **String** | The identifier for cuepoint resource. |  [optional] |
|**insertionOffsetTimeMs** | **String** | The time when the cuepoint should be inserted by offset to the broadcast actual start time. |  [optional] |
|**walltimeMs** | **String** | The wall clock time at which the cuepoint should be inserted. Only one of insertion_offset_time_ms and walltime_ms may be set at a time. |  [optional] |



## Enum: CueTypeEnum

| Name | Value |
|---- | -----|
| CUE_TYPE_UNSPECIFIED | &quot;cueTypeUnspecified&quot; |
| CUE_TYPE_AD | &quot;cueTypeAd&quot; |



