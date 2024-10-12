

# JobSchedule

Scheduling properties of a job.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enabled** | **Boolean** | Whether or not the schedule is enabled. |  [optional] |
|**endTime** | **OffsetDateTime** | Schedule end time. |  [optional] |
|**interval** | **String** | Value of the schedule&#39;s recurring interval, if the schedule type is recurring. ISO8601 duration format. |  [optional] |
|**startTime** | **OffsetDateTime** | Schedule start time. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Schedule interval type |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ONCE | &quot;Once&quot; |
| RECURRING | &quot;Recurring&quot; |



