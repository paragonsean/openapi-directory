

# ScheduleProperties

Properties of a schedule.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dailyRecurrence** | [**DayDetails**](DayDetails.md) |  |  [optional] |
|**hourlyRecurrence** | [**HourDetails**](HourDetails.md) |  |  [optional] |
|**provisioningState** | **String** | The provisioning status of the resource. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the schedule. |  [optional] |
|**taskType** | [**TaskTypeEnum**](#TaskTypeEnum) | The task type of the schedule. |  [optional] |
|**timeZoneId** | **String** | The time zone id. |  [optional] |
|**weeklyRecurrence** | [**WeekDetails**](WeekDetails.md) |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |



## Enum: TaskTypeEnum

| Name | Value |
|---- | -----|
| LAB_VMS_SHUTDOWN_TASK | &quot;LabVmsShutdownTask&quot; |
| LAB_VMS_STARTUP_TASK | &quot;LabVmsStartupTask&quot; |
| LAB_BILLING_TASK | &quot;LabBillingTask&quot; |



