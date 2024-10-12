# DisplayVideo360Api.PerformanceGoal

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**performanceGoalAmountMicros** | **String** | The goal amount, in micros of the advertiser&#39;s currency. Applicable when performance_goal_type is one of: * &#x60;PERFORMANCE_GOAL_TYPE_CPM&#x60; * &#x60;PERFORMANCE_GOAL_TYPE_CPC&#x60; * &#x60;PERFORMANCE_GOAL_TYPE_CPA&#x60; * &#x60;PERFORMANCE_GOAL_TYPE_CPIAVC&#x60; * &#x60;PERFORMANCE_GOAL_TYPE_VCPM&#x60; For example 1500000 represents 1.5 standard units of the currency. | [optional] 
**performanceGoalPercentageMicros** | **String** | The decimal representation of the goal percentage in micros. Applicable when performance_goal_type is one of: * &#x60;PERFORMANCE_GOAL_TYPE_CTR&#x60; * &#x60;PERFORMANCE_GOAL_TYPE_VIEWABILITY&#x60; * &#x60;PERFORMANCE_GOAL_TYPE_CLICK_CVR&#x60; * &#x60;PERFORMANCE_GOAL_TYPE_IMPRESSION_CVR&#x60; * &#x60;PERFORMANCE_GOAL_TYPE_VTR&#x60; * &#x60;PERFORMANCE_GOAL_TYPE_AUDIO_COMPLETION_RATE&#x60; * &#x60;PERFORMANCE_GOAL_TYPE_VIDEO_COMPLETION_RATE&#x60; For example, 70000 represents 7% (decimal 0.07). | [optional] 
**performanceGoalString** | **String** | A key performance indicator (KPI) string, which can be empty. Must be UTF-8 encoded with a length of no more than 100 characters. Applicable when performance_goal_type is set to &#x60;PERFORMANCE_GOAL_TYPE_OTHER&#x60;. | [optional] 
**performanceGoalType** | **String** | Required. The type of the performance goal. | [optional] 



## Enum: PerformanceGoalTypeEnum


* `UNSPECIFIED` (value: `"PERFORMANCE_GOAL_TYPE_UNSPECIFIED"`)

* `CPM` (value: `"PERFORMANCE_GOAL_TYPE_CPM"`)

* `CPC` (value: `"PERFORMANCE_GOAL_TYPE_CPC"`)

* `CPA` (value: `"PERFORMANCE_GOAL_TYPE_CPA"`)

* `CTR` (value: `"PERFORMANCE_GOAL_TYPE_CTR"`)

* `VIEWABILITY` (value: `"PERFORMANCE_GOAL_TYPE_VIEWABILITY"`)

* `CPIAVC` (value: `"PERFORMANCE_GOAL_TYPE_CPIAVC"`)

* `CPE` (value: `"PERFORMANCE_GOAL_TYPE_CPE"`)

* `CLICK_CVR` (value: `"PERFORMANCE_GOAL_TYPE_CLICK_CVR"`)

* `IMPRESSION_CVR` (value: `"PERFORMANCE_GOAL_TYPE_IMPRESSION_CVR"`)

* `VCPM` (value: `"PERFORMANCE_GOAL_TYPE_VCPM"`)

* `VTR` (value: `"PERFORMANCE_GOAL_TYPE_VTR"`)

* `AUDIO_COMPLETION_RATE` (value: `"PERFORMANCE_GOAL_TYPE_AUDIO_COMPLETION_RATE"`)

* `VIDEO_COMPLETION_RATE` (value: `"PERFORMANCE_GOAL_TYPE_VIDEO_COMPLETION_RATE"`)

* `OTHER` (value: `"PERFORMANCE_GOAL_TYPE_OTHER"`)




