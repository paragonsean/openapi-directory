

# Reschedule


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**rescheduleType** | [**RescheduleTypeEnum**](#RescheduleTypeEnum) | Required. The type of the reschedule. |  [optional] |
|**scheduleTime** | **String** | Optional. Timestamp when the maintenance shall be rescheduled to if reschedule_type&#x3D;SPECIFIC_TIME, in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example &#x60;2012-11-15T16:19:00.094Z&#x60;. |  [optional] |



## Enum: RescheduleTypeEnum

| Name | Value |
|---- | -----|
| RESCHEDULE_TYPE_UNSPECIFIED | &quot;RESCHEDULE_TYPE_UNSPECIFIED&quot; |
| IMMEDIATE | &quot;IMMEDIATE&quot; |
| NEXT_AVAILABLE_WINDOW | &quot;NEXT_AVAILABLE_WINDOW&quot; |
| SPECIFIC_TIME | &quot;SPECIFIC_TIME&quot; |



