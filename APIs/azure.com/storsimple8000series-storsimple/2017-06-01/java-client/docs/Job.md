

# Job

The job.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endTime** | **OffsetDateTime** | The UTC time at which the job completed. |  [optional] |
|**error** | [**JobErrorDetails**](JobErrorDetails.md) |  |  [optional] |
|**percentComplete** | **Integer** | The percentage of the job that is already complete. |  |
|**properties** | [**JobProperties**](JobProperties.md) |  |  [optional] |
|**startTime** | **OffsetDateTime** | The UTC time at which the job was started. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The current status of the job. |  |
|**id** | **String** | The path ID that uniquely identifies the object. |  [optional] [readonly] |
|**kind** | [**KindEnum**](#KindEnum) | The Kind of the object. Currently only Series8000 is supported |  [optional] |
|**name** | **String** | The name of the object. |  [optional] [readonly] |
|**type** | **String** | The hierarchical type of the object. |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| RUNNING | &quot;Running&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| FAILED | &quot;Failed&quot; |
| CANCELED | &quot;Canceled&quot; |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| SERIES8000 | &quot;Series8000&quot; |



