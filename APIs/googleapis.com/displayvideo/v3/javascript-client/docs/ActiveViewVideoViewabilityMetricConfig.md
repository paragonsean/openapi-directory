# DisplayVideo360Api.ActiveViewVideoViewabilityMetricConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**displayName** | **String** | Required. The display name of the custom metric. | [optional] 
**minimumDuration** | **String** | The minimum visible video duration required (in seconds) in order for an impression to be recorded. You must specify minimum_duration, minimum_quartile or both. If both are specified, an impression meets the metric criteria if either requirement is met (whichever happens first). | [optional] 
**minimumQuartile** | **String** | The minimum visible video duration required, based on the video quartiles, in order for an impression to be recorded. You must specify minimum_duration, minimum_quartile or both. If both are specified, an impression meets the metric criteria if either requirement is met (whichever happens first). | [optional] 
**minimumViewability** | **String** | Required. The minimum percentage of the video ad&#39;s pixels visible on the screen in order for an impression to be recorded. | [optional] 
**minimumVolume** | **String** | Required. The minimum percentage of the video ad&#39;s volume required in order for an impression to be recorded. | [optional] 



## Enum: MinimumDurationEnum


* `UNSPECIFIED` (value: `"VIDEO_DURATION_UNSPECIFIED"`)

* `SECONDS_NONE` (value: `"VIDEO_DURATION_SECONDS_NONE"`)

* `SECONDS_0` (value: `"VIDEO_DURATION_SECONDS_0"`)

* `SECONDS_1` (value: `"VIDEO_DURATION_SECONDS_1"`)

* `SECONDS_2` (value: `"VIDEO_DURATION_SECONDS_2"`)

* `SECONDS_3` (value: `"VIDEO_DURATION_SECONDS_3"`)

* `SECONDS_4` (value: `"VIDEO_DURATION_SECONDS_4"`)

* `SECONDS_5` (value: `"VIDEO_DURATION_SECONDS_5"`)

* `SECONDS_6` (value: `"VIDEO_DURATION_SECONDS_6"`)

* `SECONDS_7` (value: `"VIDEO_DURATION_SECONDS_7"`)

* `SECONDS_8` (value: `"VIDEO_DURATION_SECONDS_8"`)

* `SECONDS_9` (value: `"VIDEO_DURATION_SECONDS_9"`)

* `SECONDS_10` (value: `"VIDEO_DURATION_SECONDS_10"`)

* `SECONDS_11` (value: `"VIDEO_DURATION_SECONDS_11"`)

* `SECONDS_12` (value: `"VIDEO_DURATION_SECONDS_12"`)

* `SECONDS_13` (value: `"VIDEO_DURATION_SECONDS_13"`)

* `SECONDS_14` (value: `"VIDEO_DURATION_SECONDS_14"`)

* `SECONDS_15` (value: `"VIDEO_DURATION_SECONDS_15"`)

* `SECONDS_30` (value: `"VIDEO_DURATION_SECONDS_30"`)

* `SECONDS_45` (value: `"VIDEO_DURATION_SECONDS_45"`)

* `SECONDS_60` (value: `"VIDEO_DURATION_SECONDS_60"`)





## Enum: MinimumQuartileEnum


* `UNSPECIFIED` (value: `"VIDEO_DURATION_QUARTILE_UNSPECIFIED"`)

* `NONE` (value: `"VIDEO_DURATION_QUARTILE_NONE"`)

* `FIRST` (value: `"VIDEO_DURATION_QUARTILE_FIRST"`)

* `SECOND` (value: `"VIDEO_DURATION_QUARTILE_SECOND"`)

* `THIRD` (value: `"VIDEO_DURATION_QUARTILE_THIRD"`)

* `FOURTH` (value: `"VIDEO_DURATION_QUARTILE_FOURTH"`)





## Enum: MinimumViewabilityEnum


* `UNSPECIFIED` (value: `"VIEWABILITY_PERCENT_UNSPECIFIED"`)

* `0` (value: `"VIEWABILITY_PERCENT_0"`)

* `25` (value: `"VIEWABILITY_PERCENT_25"`)

* `50` (value: `"VIEWABILITY_PERCENT_50"`)

* `75` (value: `"VIEWABILITY_PERCENT_75"`)

* `100` (value: `"VIEWABILITY_PERCENT_100"`)





## Enum: MinimumVolumeEnum


* `UNSPECIFIED` (value: `"VIDEO_VOLUME_PERCENT_UNSPECIFIED"`)

* `0` (value: `"VIDEO_VOLUME_PERCENT_0"`)

* `10` (value: `"VIDEO_VOLUME_PERCENT_10"`)




