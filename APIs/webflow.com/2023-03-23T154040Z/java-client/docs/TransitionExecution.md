

# TransitionExecution


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**completedBy** | **String** |  |  |
|**endTime** | **String** |  |  [optional] |
|**executionId** | **String** |  |  |
|**input** | **Object** |  |  |
|**logId** | **String** |  |  [optional] |
|**startTime** | **String** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**transitionId** | [**LogsTransitionId**](LogsTransitionId.md) |  |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| RUNNING | &quot;running&quot; |
| SUCCEEDED | &quot;succeeded&quot; |
| FAILED | &quot;failed&quot; |
| REJECTED | &quot;rejected&quot; |
| RETRY | &quot;retry&quot; |



