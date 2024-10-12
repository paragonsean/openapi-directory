

# PerformanceGoal

Settings that control the performance goal of a campaign.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**performanceGoalAmountMicros** | **String** | The goal amount, in micros of the advertiser&#39;s currency. Applicable when performance_goal_type is one of: * &#x60;PERFORMANCE_GOAL_TYPE_CPM&#x60; * &#x60;PERFORMANCE_GOAL_TYPE_CPC&#x60; * &#x60;PERFORMANCE_GOAL_TYPE_CPA&#x60; * &#x60;PERFORMANCE_GOAL_TYPE_CPIAVC&#x60; * &#x60;PERFORMANCE_GOAL_TYPE_VCPM&#x60; For example 1500000 represents 1.5 standard units of the currency. |  [optional] |
|**performanceGoalPercentageMicros** | **String** | The decimal representation of the goal percentage in micros. Applicable when performance_goal_type is one of: * &#x60;PERFORMANCE_GOAL_TYPE_CTR&#x60; * &#x60;PERFORMANCE_GOAL_TYPE_VIEWABILITY&#x60; * &#x60;PERFORMANCE_GOAL_TYPE_CLICK_CVR&#x60; * &#x60;PERFORMANCE_GOAL_TYPE_IMPRESSION_CVR&#x60; * &#x60;PERFORMANCE_GOAL_TYPE_VTR&#x60; * &#x60;PERFORMANCE_GOAL_TYPE_AUDIO_COMPLETION_RATE&#x60; * &#x60;PERFORMANCE_GOAL_TYPE_VIDEO_COMPLETION_RATE&#x60; For example, 70000 represents 7% (decimal 0.07). |  [optional] |
|**performanceGoalString** | **String** | A key performance indicator (KPI) string, which can be empty. Must be UTF-8 encoded with a length of no more than 100 characters. Applicable when performance_goal_type is set to &#x60;PERFORMANCE_GOAL_TYPE_OTHER&#x60;. |  [optional] |
|**performanceGoalType** | [**PerformanceGoalTypeEnum**](#PerformanceGoalTypeEnum) | Required. The type of the performance goal. |  [optional] |



## Enum: PerformanceGoalTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;PERFORMANCE_GOAL_TYPE_UNSPECIFIED&quot; |
| CPM | &quot;PERFORMANCE_GOAL_TYPE_CPM&quot; |
| CPC | &quot;PERFORMANCE_GOAL_TYPE_CPC&quot; |
| CPA | &quot;PERFORMANCE_GOAL_TYPE_CPA&quot; |
| CTR | &quot;PERFORMANCE_GOAL_TYPE_CTR&quot; |
| VIEWABILITY | &quot;PERFORMANCE_GOAL_TYPE_VIEWABILITY&quot; |
| CPIAVC | &quot;PERFORMANCE_GOAL_TYPE_CPIAVC&quot; |
| CPE | &quot;PERFORMANCE_GOAL_TYPE_CPE&quot; |
| CLICK_CVR | &quot;PERFORMANCE_GOAL_TYPE_CLICK_CVR&quot; |
| IMPRESSION_CVR | &quot;PERFORMANCE_GOAL_TYPE_IMPRESSION_CVR&quot; |
| VCPM | &quot;PERFORMANCE_GOAL_TYPE_VCPM&quot; |
| VTR | &quot;PERFORMANCE_GOAL_TYPE_VTR&quot; |
| AUDIO_COMPLETION_RATE | &quot;PERFORMANCE_GOAL_TYPE_AUDIO_COMPLETION_RATE&quot; |
| VIDEO_COMPLETION_RATE | &quot;PERFORMANCE_GOAL_TYPE_VIDEO_COMPLETION_RATE&quot; |
| OTHER | &quot;PERFORMANCE_GOAL_TYPE_OTHER&quot; |



