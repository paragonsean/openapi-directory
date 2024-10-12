

# TaskAddResult

Result for a single task added as part of an add task collection operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**eTag** | **String** | The ETag of the task, if the task was successfully added. |  [optional] |
|**error** | [**BatchError**](BatchError.md) |  |  [optional] |
|**lastModified** | **OffsetDateTime** | The last modified time of the task. |  [optional] |
|**location** | **String** | The URL of the task, if the task was successfully added. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the add task request. |  |
|**taskId** | **String** | The id of the task for which this is the result. |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| SUCCESS | &quot;success&quot; |
| CLIENTERROR | &quot;clienterror&quot; |
| SERVERERROR | &quot;servererror&quot; |
| UNMAPPED | &quot;unmapped&quot; |



