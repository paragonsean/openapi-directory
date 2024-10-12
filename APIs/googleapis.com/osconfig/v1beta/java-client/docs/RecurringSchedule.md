

# RecurringSchedule

Sets the time for recurring patch deployments.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endTime** | **String** | Optional. The end time at which a recurring patch deployment schedule is no longer active. |  [optional] |
|**frequency** | [**FrequencyEnum**](#FrequencyEnum) | Required. The frequency unit of this recurring schedule. |  [optional] |
|**lastExecuteTime** | **String** | Output only. The time the last patch job ran successfully. |  [optional] [readonly] |
|**monthly** | [**MonthlySchedule**](MonthlySchedule.md) |  |  [optional] |
|**nextExecuteTime** | **String** | Output only. The time the next patch job is scheduled to run. |  [optional] [readonly] |
|**startTime** | **String** | Optional. The time that the recurring schedule becomes effective. Defaults to &#x60;create_time&#x60; of the patch deployment. |  [optional] |
|**timeOfDay** | [**TimeOfDay**](TimeOfDay.md) |  |  [optional] |
|**timeZone** | [**TimeZone**](TimeZone.md) |  |  [optional] |
|**weekly** | [**WeeklySchedule**](WeeklySchedule.md) |  |  [optional] |



## Enum: FrequencyEnum

| Name | Value |
|---- | -----|
| FREQUENCY_UNSPECIFIED | &quot;FREQUENCY_UNSPECIFIED&quot; |
| WEEKLY | &quot;WEEKLY&quot; |
| MONTHLY | &quot;MONTHLY&quot; |
| DAILY | &quot;DAILY&quot; |



