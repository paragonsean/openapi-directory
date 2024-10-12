

# ReportConfigSchedule

The schedule associated with a report config.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**recurrence** | [**RecurrenceEnum**](#RecurrenceEnum) | The schedule recurrence. |  |
|**recurrencePeriod** | [**ReportConfigRecurrencePeriod**](ReportConfigRecurrencePeriod.md) |  |  |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the schedule. Whether active or not. If inactive, the report&#39;s scheduled execution is paused. |  [optional] |



## Enum: RecurrenceEnum

| Name | Value |
|---- | -----|
| DAILY | &quot;Daily&quot; |
| WEEKLY | &quot;Weekly&quot; |
| MONTHLY | &quot;Monthly&quot; |
| ANNUALLY | &quot;Annually&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;Active&quot; |
| INACTIVE | &quot;Inactive&quot; |



