

# WorkflowNode

The workflow node.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**error** | **String** | Output only. The error detail. |  [optional] [readonly] |
|**jobId** | **String** | Output only. The job id; populated after the node enters RUNNING state. |  [optional] [readonly] |
|**prerequisiteStepIds** | **List&lt;String&gt;** | Output only. Node&#39;s prerequisite nodes. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The node state. |  [optional] [readonly] |
|**stepId** | **String** | Output only. The name of the node. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| NODE_STATE_UNSPECIFIED | &quot;NODE_STATE_UNSPECIFIED&quot; |
| BLOCKED | &quot;BLOCKED&quot; |
| RUNNABLE | &quot;RUNNABLE&quot; |
| RUNNING | &quot;RUNNING&quot; |
| COMPLETED | &quot;COMPLETED&quot; |
| FAILED | &quot;FAILED&quot; |



