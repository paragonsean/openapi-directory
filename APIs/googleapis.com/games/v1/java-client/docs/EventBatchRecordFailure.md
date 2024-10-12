

# EventBatchRecordFailure

A batch update failure resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**failureCause** | [**FailureCauseEnum**](#FailureCauseEnum) | The cause for the update failure. |  [optional] |
|**kind** | **String** | Uniquely identifies the type of this resource. Value is always the fixed string &#x60;games#eventBatchRecordFailure&#x60;. |  [optional] |
|**range** | [**EventPeriodRange**](EventPeriodRange.md) |  |  [optional] |



## Enum: FailureCauseEnum

| Name | Value |
|---- | -----|
| TOO_LARGE | &quot;TOO_LARGE&quot; |
| TIME_PERIOD_EXPIRED | &quot;TIME_PERIOD_EXPIRED&quot; |
| TIME_PERIOD_SHORT | &quot;TIME_PERIOD_SHORT&quot; |
| TIME_PERIOD_LONG | &quot;TIME_PERIOD_LONG&quot; |
| ALREADY_UPDATED | &quot;ALREADY_UPDATED&quot; |
| RECORD_RATE_HIGH | &quot;RECORD_RATE_HIGH&quot; |



