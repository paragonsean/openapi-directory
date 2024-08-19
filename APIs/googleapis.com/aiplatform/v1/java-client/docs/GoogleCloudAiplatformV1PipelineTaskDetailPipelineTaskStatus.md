

# GoogleCloudAiplatformV1PipelineTaskDetailPipelineTaskStatus

A single record of the task status.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**error** | [**GoogleRpcStatus**](GoogleRpcStatus.md) |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The state of the task. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. Update time of this status. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| PENDING | &quot;PENDING&quot; |
| RUNNING | &quot;RUNNING&quot; |
| SUCCEEDED | &quot;SUCCEEDED&quot; |
| CANCEL_PENDING | &quot;CANCEL_PENDING&quot; |
| CANCELLING | &quot;CANCELLING&quot; |
| CANCELLED | &quot;CANCELLED&quot; |
| FAILED | &quot;FAILED&quot; |
| SKIPPED | &quot;SKIPPED&quot; |
| NOT_TRIGGERED | &quot;NOT_TRIGGERED&quot; |



