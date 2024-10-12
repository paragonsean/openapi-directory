

# Job

A device job.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endTime** | **OffsetDateTime** | The UTC date and time at which the job completed. |  [optional] [readonly] |
|**error** | [**JobErrorDetails**](JobErrorDetails.md) |  |  [optional] |
|**id** | **String** | The path ID that uniquely identifies the object. |  [optional] [readonly] |
|**name** | **String** | The name of the object. |  [optional] [readonly] |
|**percentComplete** | **Integer** | The percentage of the job that is complete. |  [optional] [readonly] |
|**properties** | [**JobProperties**](JobProperties.md) |  |  [optional] |
|**startTime** | **OffsetDateTime** | The UTC date and time at which the job started. |  [optional] [readonly] |
|**status** | [**StatusEnum**](#StatusEnum) | The current status of the job. |  [optional] [readonly] |
|**type** | **String** | The hierarchical type of the object. |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| RUNNING | &quot;Running&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| FAILED | &quot;Failed&quot; |
| CANCELED | &quot;Canceled&quot; |
| PAUSED | &quot;Paused&quot; |
| SCHEDULED | &quot;Scheduled&quot; |



