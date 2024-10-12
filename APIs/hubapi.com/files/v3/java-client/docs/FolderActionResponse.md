

# FolderActionResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**completedAt** | **OffsetDateTime** | When the requested changes have been completed. |  |
|**errors** | [**List&lt;StandardError&gt;**](StandardError.md) | Detailed errors resulting from the task. |  [optional] |
|**links** | **Map&lt;String, String&gt;** | Link to check the status of the task. |  [optional] |
|**numErrors** | **Integer** | Number of errors resulting from the requested changes. |  [optional] |
|**requestedAt** | **OffsetDateTime** | Timestamp representing when the task was requested. |  [optional] |
|**result** | [**Folder**](Folder.md) |  |  [optional] |
|**startedAt** | **OffsetDateTime** | Timestamp representing when the task was started at. |  |
|**status** | [**StatusEnum**](#StatusEnum) | Current status of the task. |  |
|**taskId** | **String** | ID of the task. |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;PENDING&quot; |
| PROCESSING | &quot;PROCESSING&quot; |
| CANCELED | &quot;CANCELED&quot; |
| COMPLETE | &quot;COMPLETE&quot; |



