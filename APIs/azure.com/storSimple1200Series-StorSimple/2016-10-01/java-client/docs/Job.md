

# Job

The Job.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endTime** | **OffsetDateTime** | The UTC time at which the job completed |  [optional] |
|**error** | [**JobErrorDetails**](JobErrorDetails.md) |  |  [optional] |
|**percentComplete** | **Integer** | The percentage of the job that is already complete |  |
|**properties** | [**JobProperties**](JobProperties.md) |  |  [optional] |
|**startTime** | **OffsetDateTime** | The UTC time at which the job was started |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Current status of the job |  |
|**id** | **String** | The identifier. |  [optional] [readonly] |
|**name** | **String** | The name. |  [optional] [readonly] |
|**type** | **String** | The type. |  [optional] [readonly] |



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



