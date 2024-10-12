

# DiaryAppointmentModel

Represents a single diary appointment for a staff member.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appointmentType** | **String** | The diary appointment type. |  [optional] |
|**cancelled** | **Boolean** | Whether the appointment has been cancelled. |  [optional] |
|**comment** | **String** | The appointment comments text. |  [optional] |
|**createdAt** | **OffsetDateTime** | The date/time this appointment was created. |  [optional] |
|**createdBy** | **String** | The staff member that created this appointment. |  [optional] |
|**etag** | **String** | A unique identifier defining the object and change revision. |  [optional] |
|**end** | **OffsetDateTime** | The end date/time of this appointment. |  [optional] |
|**OID** | **String** | The unique Object ID (OID). |  [optional] |
|**remindAt** | **OffsetDateTime** | The date/time to remind the staff member of this appointment. |  [optional] |
|**remindBefore** | [**RemindBeforeEnum**](#RemindBeforeEnum) | The number of minutes before the appointment start date/time to remind the staff member. -1 means don&#39;t remind. |  [optional] |
|**staff** | **String** | The staff member holding this appointment. |  [optional] |
|**start** | **OffsetDateTime** | The start date/time of this appointment. |  [optional] |
|**subject** | **String** | The appointment subject text. |  [optional] |



## Enum: RemindBeforeEnum

| Name | Value |
|---- | -----|
| MIN | &quot;Min&quot; |
| MIN2 | &quot;Min2&quot; |
| MIN5 | &quot;Min5&quot; |
| MIN10 | &quot;Min10&quot; |
| MIN15 | &quot;Min15&quot; |
| MIN30 | &quot;Min30&quot; |
| MIN45 | &quot;Min45&quot; |
| HOUR | &quot;Hour&quot; |
| HOUR2 | &quot;Hour2&quot; |
| HOUR3 | &quot;Hour3&quot; |
| HOUR6 | &quot;Hour6&quot; |
| HOUR12 | &quot;Hour12&quot; |
| DAY | &quot;Day&quot; |
| DAY2 | &quot;Day2&quot; |
| DAY3 | &quot;Day3&quot; |
| WEEK | &quot;Week&quot; |
| NO_REMINDER | &quot;NoReminder&quot; |



