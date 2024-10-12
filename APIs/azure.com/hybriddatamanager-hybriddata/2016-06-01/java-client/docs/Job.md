

# Job

Data service job.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endTime** | **OffsetDateTime** | Time at which the job ended in UTC ISO 8601 format. |  [optional] |
|**error** | [**Error**](Error.md) |  |  [optional] |
|**properties** | [**JobProperties**](JobProperties.md) |  |  |
|**startTime** | **OffsetDateTime** | Time at which the job was started in UTC ISO 8601 format. |  |
|**status** | [**StatusEnum**](#StatusEnum) | Status of the job. |  |
|**id** | **String** | Id of the object. |  [optional] [readonly] |
|**name** | **String** | Name of the object. |  [optional] [readonly] |
|**type** | **String** | Type of the object. |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| IN_PROGRESS | &quot;InProgress&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| WAITING_FOR_ACTION | &quot;WaitingForAction&quot; |
| FAILED | &quot;Failed&quot; |
| CANCELLED | &quot;Cancelled&quot; |
| CANCELLING | &quot;Cancelling&quot; |



