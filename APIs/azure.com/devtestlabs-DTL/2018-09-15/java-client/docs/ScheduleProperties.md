

# ScheduleProperties

Properties of a schedule.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdDate** | **OffsetDateTime** | The creation date of the schedule. |  [optional] [readonly] |
|**dailyRecurrence** | [**DayDetails**](DayDetails.md) |  |  [optional] |
|**hourlyRecurrence** | [**HourDetails**](HourDetails.md) |  |  [optional] |
|**notificationSettings** | [**NotificationSettings**](NotificationSettings.md) |  |  [optional] |
|**provisioningState** | **String** | The provisioning status of the resource. |  [optional] [readonly] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the schedule (i.e. Enabled, Disabled) |  [optional] |
|**targetResourceId** | **String** | The resource ID to which the schedule belongs |  [optional] |
|**taskType** | **String** | The task type of the schedule (e.g. LabVmsShutdownTask, LabVmAutoStart). |  [optional] |
|**timeZoneId** | **String** | The time zone ID (e.g. Pacific Standard time). |  [optional] |
|**uniqueIdentifier** | **String** | The unique immutable identifier of a resource (Guid). |  [optional] [readonly] |
|**weeklyRecurrence** | [**WeekDetails**](WeekDetails.md) |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |



