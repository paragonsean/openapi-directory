

# OperationResponse

Response for long running operation

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endTime** | **OffsetDateTime** | start time |  [optional] |
|**error** | [**DataShareErrorInfo**](DataShareErrorInfo.md) |  |  [optional] |
|**startTime** | **OffsetDateTime** | start time |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Operation state of the long running operation. |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACCEPTED | &quot;Accepted&quot; |
| IN_PROGRESS | &quot;InProgress&quot; |
| TRANSIENT_FAILURE | &quot;TransientFailure&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| FAILED | &quot;Failed&quot; |
| CANCELED | &quot;Canceled&quot; |



