# CloudMemorystoreForMemcachedApi.RescheduleMaintenanceRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rescheduleType** | **String** | Required. If reschedule type is SPECIFIC_TIME, must set up schedule_time as well. | [optional] 
**scheduleTime** | **String** | Timestamp when the maintenance shall be rescheduled to if reschedule_type&#x3D;SPECIFIC_TIME, in RFC 3339 format, for example &#x60;2012-11-15T16:19:00.094Z&#x60;. | [optional] 



## Enum: RescheduleTypeEnum


* `RESCHEDULE_TYPE_UNSPECIFIED` (value: `"RESCHEDULE_TYPE_UNSPECIFIED"`)

* `IMMEDIATE` (value: `"IMMEDIATE"`)

* `NEXT_AVAILABLE_WINDOW` (value: `"NEXT_AVAILABLE_WINDOW"`)

* `SPECIFIC_TIME` (value: `"SPECIFIC_TIME"`)




