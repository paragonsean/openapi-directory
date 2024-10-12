

# FileActionResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**completedAt** | **OffsetDateTime** | Time of completion of task. |  |
|**errors** | [**List&lt;StandardError&gt;**](StandardError.md) | Descriptive error messages. |  [optional] |
|**links** | **Map&lt;String, String&gt;** | Link to check the status of the requested task. |  [optional] |
|**numErrors** | **Integer** | Number of errors resulting from the task. |  [optional] |
|**requestedAt** | **OffsetDateTime** | Timestamp of when the task was requested. |  [optional] |
|**result** | [**ModelFile**](ModelFile.md) |  |  [optional] |
|**startedAt** | **OffsetDateTime** | Timestamp of when the task was started. |  |
|**status** | [**StatusEnum**](#StatusEnum) | Current status of the task. |  |
|**taskId** | **String** | ID of the requested task. |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;PENDING&quot; |
| PROCESSING | &quot;PROCESSING&quot; |
| CANCELED | &quot;CANCELED&quot; |
| COMPLETE | &quot;COMPLETE&quot; |



