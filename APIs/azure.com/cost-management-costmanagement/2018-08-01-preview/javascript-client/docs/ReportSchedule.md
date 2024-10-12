# CostManagementClient.ReportSchedule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recurrence** | **String** | The schedule recurrence. | 
**recurrencePeriod** | [**ReportRecurrencePeriod**](ReportRecurrencePeriod.md) |  | [optional] 
**status** | **String** | The status of the schedule. Whether active or not. If inactive, the report&#39;s scheduled execution is paused. | [optional] 



## Enum: RecurrenceEnum


* `Daily` (value: `"Daily"`)

* `Weekly` (value: `"Weekly"`)

* `Monthly` (value: `"Monthly"`)

* `Annually` (value: `"Annually"`)





## Enum: StatusEnum


* `Active` (value: `"Active"`)

* `Inactive` (value: `"Inactive"`)




