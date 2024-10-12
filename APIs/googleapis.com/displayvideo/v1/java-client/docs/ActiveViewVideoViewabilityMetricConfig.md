

# ActiveViewVideoViewabilityMetricConfig

Configuration for custom Active View video viewability metrics.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayName** | **String** | Required. The display name of the custom metric. |  [optional] |
|**minimumDuration** | [**MinimumDurationEnum**](#MinimumDurationEnum) | The minimum visible video duration required (in seconds) in order for an impression to be recorded. You must specify minimum_duration, minimum_quartile or both. If both are specified, an impression meets the metric criteria if either requirement is met (whichever happens first). |  [optional] |
|**minimumQuartile** | [**MinimumQuartileEnum**](#MinimumQuartileEnum) | The minimum visible video duration required, based on the video quartiles, in order for an impression to be recorded. You must specify minimum_duration, minimum_quartile or both. If both are specified, an impression meets the metric criteria if either requirement is met (whichever happens first). |  [optional] |
|**minimumViewability** | [**MinimumViewabilityEnum**](#MinimumViewabilityEnum) | Required. The minimum percentage of the video ad&#39;s pixels visible on the screen in order for an impression to be recorded. |  [optional] |
|**minimumVolume** | [**MinimumVolumeEnum**](#MinimumVolumeEnum) | Required. The minimum percentage of the video ad&#39;s volume required in order for an impression to be recorded. |  [optional] |



## Enum: MinimumDurationEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;VIDEO_DURATION_UNSPECIFIED&quot; |
| SECONDS_NONE | &quot;VIDEO_DURATION_SECONDS_NONE&quot; |
| SECONDS_0 | &quot;VIDEO_DURATION_SECONDS_0&quot; |
| SECONDS_1 | &quot;VIDEO_DURATION_SECONDS_1&quot; |
| SECONDS_2 | &quot;VIDEO_DURATION_SECONDS_2&quot; |
| SECONDS_3 | &quot;VIDEO_DURATION_SECONDS_3&quot; |
| SECONDS_4 | &quot;VIDEO_DURATION_SECONDS_4&quot; |
| SECONDS_5 | &quot;VIDEO_DURATION_SECONDS_5&quot; |
| SECONDS_6 | &quot;VIDEO_DURATION_SECONDS_6&quot; |
| SECONDS_7 | &quot;VIDEO_DURATION_SECONDS_7&quot; |
| SECONDS_8 | &quot;VIDEO_DURATION_SECONDS_8&quot; |
| SECONDS_9 | &quot;VIDEO_DURATION_SECONDS_9&quot; |
| SECONDS_10 | &quot;VIDEO_DURATION_SECONDS_10&quot; |
| SECONDS_11 | &quot;VIDEO_DURATION_SECONDS_11&quot; |
| SECONDS_12 | &quot;VIDEO_DURATION_SECONDS_12&quot; |
| SECONDS_13 | &quot;VIDEO_DURATION_SECONDS_13&quot; |
| SECONDS_14 | &quot;VIDEO_DURATION_SECONDS_14&quot; |
| SECONDS_15 | &quot;VIDEO_DURATION_SECONDS_15&quot; |
| SECONDS_30 | &quot;VIDEO_DURATION_SECONDS_30&quot; |
| SECONDS_45 | &quot;VIDEO_DURATION_SECONDS_45&quot; |
| SECONDS_60 | &quot;VIDEO_DURATION_SECONDS_60&quot; |



## Enum: MinimumQuartileEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;VIDEO_DURATION_QUARTILE_UNSPECIFIED&quot; |
| NONE | &quot;VIDEO_DURATION_QUARTILE_NONE&quot; |
| FIRST | &quot;VIDEO_DURATION_QUARTILE_FIRST&quot; |
| SECOND | &quot;VIDEO_DURATION_QUARTILE_SECOND&quot; |
| THIRD | &quot;VIDEO_DURATION_QUARTILE_THIRD&quot; |
| FOURTH | &quot;VIDEO_DURATION_QUARTILE_FOURTH&quot; |



## Enum: MinimumViewabilityEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;VIEWABILITY_PERCENT_UNSPECIFIED&quot; |
| _0 | &quot;VIEWABILITY_PERCENT_0&quot; |
| _25 | &quot;VIEWABILITY_PERCENT_25&quot; |
| _50 | &quot;VIEWABILITY_PERCENT_50&quot; |
| _75 | &quot;VIEWABILITY_PERCENT_75&quot; |
| _100 | &quot;VIEWABILITY_PERCENT_100&quot; |



## Enum: MinimumVolumeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;VIDEO_VOLUME_PERCENT_UNSPECIFIED&quot; |
| _0 | &quot;VIDEO_VOLUME_PERCENT_0&quot; |
| _10 | &quot;VIDEO_VOLUME_PERCENT_10&quot; |



