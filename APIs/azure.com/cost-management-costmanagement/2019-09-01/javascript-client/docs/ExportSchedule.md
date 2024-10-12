# CostManagementClient.ExportSchedule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recurrence** | **String** | The schedule recurrence. | 
**recurrencePeriod** | [**ExportRecurrencePeriod**](ExportRecurrencePeriod.md) |  | [optional] 
**status** | **String** | The status of the schedule. Whether active or not. If inactive, the export&#39;s scheduled execution is paused. | [optional] 



## Enum: RecurrenceEnum


* `Daily` (value: `"Daily"`)

* `Weekly` (value: `"Weekly"`)

* `Monthly` (value: `"Monthly"`)

* `Annually` (value: `"Annually"`)





## Enum: StatusEnum


* `Active` (value: `"Active"`)

* `Inactive` (value: `"Inactive"`)




