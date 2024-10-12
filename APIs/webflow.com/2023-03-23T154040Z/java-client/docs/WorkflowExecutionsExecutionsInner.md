

# WorkflowExecutionsExecutionsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**completedBy** | [**List&lt;WorkflowExecutionCompletedByInner&gt;**](WorkflowExecutionCompletedByInner.md) |  |  [optional] |
|**completedTaskLogId** | **String** |  |  [optional] |
|**endTime** | **String** |  |  |
|**events** | **List&lt;Object&gt;** |  |  [optional] |
|**executionId** | **String** |  |  |
|**input** | **Object** |  |  |
|**logId** | **String** |  |  [optional] |
|**output** | **Object** |  |  |
|**startTime** | **String** |  |  |
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**transitionExecutions** | **Object** |  |  |
|**workflowId** | **String** |  |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| RUNNING | &quot;running&quot; |
| SUCCEEDED | &quot;succeeded&quot; |
| FAILED | &quot;failed&quot; |
| REJECTED | &quot;rejected&quot; |
| RETRY | &quot;retry&quot; |
| ERROR | &quot;error&quot; |



