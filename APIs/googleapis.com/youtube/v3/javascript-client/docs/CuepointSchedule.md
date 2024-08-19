# YouTubeDataApiV3.CuepointSchedule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **Boolean** | This field is semantically required. If it is set false or not set, other fields in this message will be ignored. | [optional] 
**pauseAdsUntil** | **String** | If set, automatic cuepoint insertion is paused until this timestamp (\&quot;No Ad Zone\&quot;). The value is specified in ISO 8601 format. | [optional] 
**repeatIntervalSecs** | **Number** | Interval frequency in seconds that api uses to insert cuepoints automatically. | [optional] 
**scheduleStrategy** | **String** | The strategy to use when scheduling cuepoints. | [optional] 



## Enum: ScheduleStrategyEnum


* `scheduleStrategyUnspecified` (value: `"scheduleStrategyUnspecified"`)

* `concurrent` (value: `"concurrent"`)

* `nonConcurrent` (value: `"nonConcurrent"`)




