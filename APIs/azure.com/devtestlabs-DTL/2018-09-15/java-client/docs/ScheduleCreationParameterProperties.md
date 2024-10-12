

# ScheduleCreationParameterProperties

Properties for schedule creation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dailyRecurrence** | [**DayDetails**](DayDetails.md) |  |  [optional] |
|**hourlyRecurrence** | [**HourDetails**](HourDetails.md) |  |  [optional] |
|**notificationSettings** | [**NotificationSettings**](NotificationSettings.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the schedule (i.e. Enabled, Disabled) |  [optional] |
|**targetResourceId** | **String** | The resource ID to which the schedule belongs |  [optional] |
|**taskType** | **String** | The task type of the schedule (e.g. LabVmsShutdownTask, LabVmAutoStart). |  [optional] |
|**timeZoneId** | **String** | The time zone ID (e.g. Pacific Standard time). |  [optional] |
|**weeklyRecurrence** | [**WeekDetails**](WeekDetails.md) |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |



