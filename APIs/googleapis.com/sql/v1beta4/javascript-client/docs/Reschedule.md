# CloudSqlAdminApi.Reschedule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rescheduleType** | **String** | Required. The type of the reschedule. | [optional] 
**scheduleTime** | **String** | Optional. Timestamp when the maintenance shall be rescheduled to if reschedule_type&#x3D;SPECIFIC_TIME, in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example &#x60;2012-11-15T16:19:00.094Z&#x60;. | [optional] 



## Enum: RescheduleTypeEnum


* `RESCHEDULE_TYPE_UNSPECIFIED` (value: `"RESCHEDULE_TYPE_UNSPECIFIED"`)

* `IMMEDIATE` (value: `"IMMEDIATE"`)

* `NEXT_AVAILABLE_WINDOW` (value: `"NEXT_AVAILABLE_WINDOW"`)

* `SPECIFIC_TIME` (value: `"SPECIFIC_TIME"`)




