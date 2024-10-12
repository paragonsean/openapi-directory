# GooglePlayGameServices.EventBatchRecordFailure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failureCause** | **String** | The cause for the update failure. | [optional] 
**kind** | **String** | Uniquely identifies the type of this resource. Value is always the fixed string &#x60;games#eventBatchRecordFailure&#x60;. | [optional] 
**range** | [**EventPeriodRange**](EventPeriodRange.md) |  | [optional] 



## Enum: FailureCauseEnum


* `TOO_LARGE` (value: `"TOO_LARGE"`)

* `TIME_PERIOD_EXPIRED` (value: `"TIME_PERIOD_EXPIRED"`)

* `TIME_PERIOD_SHORT` (value: `"TIME_PERIOD_SHORT"`)

* `TIME_PERIOD_LONG` (value: `"TIME_PERIOD_LONG"`)

* `ALREADY_UPDATED` (value: `"ALREADY_UPDATED"`)

* `RECORD_RATE_HIGH` (value: `"RECORD_RATE_HIGH"`)




