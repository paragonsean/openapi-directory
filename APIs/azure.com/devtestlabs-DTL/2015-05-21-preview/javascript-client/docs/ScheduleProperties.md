# DevTestLabsClient.ScheduleProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dailyRecurrence** | [**DayDetails**](DayDetails.md) |  | [optional] 
**hourlyRecurrence** | [**HourDetails**](HourDetails.md) |  | [optional] 
**provisioningState** | **String** | The provisioning status of the resource. | [optional] 
**status** | **String** | The status of the schedule. | [optional] 
**taskType** | **String** | The task type of the schedule. | [optional] 
**timeZoneId** | **String** | The time zone id. | [optional] 
**weeklyRecurrence** | [**WeekDetails**](WeekDetails.md) |  | [optional] 



## Enum: StatusEnum


* `Enabled` (value: `"Enabled"`)

* `Disabled` (value: `"Disabled"`)





## Enum: TaskTypeEnum


* `LabVmsShutdownTask` (value: `"LabVmsShutdownTask"`)

* `LabVmsStartupTask` (value: `"LabVmsStartupTask"`)

* `LabBillingTask` (value: `"LabBillingTask"`)




