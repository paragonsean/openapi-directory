

# GoogleCloudAiplatformV1PipelineTaskDetail

The runtime detail of a task execution.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. Task create time. |  [optional] [readonly] |
|**endTime** | **String** | Output only. Task end time. |  [optional] [readonly] |
|**error** | [**GoogleRpcStatus**](GoogleRpcStatus.md) |  |  [optional] |
|**execution** | [**GoogleCloudAiplatformV1Execution**](GoogleCloudAiplatformV1Execution.md) |  |  [optional] |
|**executorDetail** | [**GoogleCloudAiplatformV1PipelineTaskExecutorDetail**](GoogleCloudAiplatformV1PipelineTaskExecutorDetail.md) |  |  [optional] |
|**inputs** | [**Map&lt;String, GoogleCloudAiplatformV1PipelineTaskDetailArtifactList&gt;**](GoogleCloudAiplatformV1PipelineTaskDetailArtifactList.md) | Output only. The runtime input artifacts of the task. |  [optional] [readonly] |
|**outputs** | [**Map&lt;String, GoogleCloudAiplatformV1PipelineTaskDetailArtifactList&gt;**](GoogleCloudAiplatformV1PipelineTaskDetailArtifactList.md) | Output only. The runtime output artifacts of the task. |  [optional] [readonly] |
|**parentTaskId** | **String** | Output only. The id of the parent task if the task is within a component scope. Empty if the task is at the root level. |  [optional] [readonly] |
|**pipelineTaskStatus** | [**List&lt;GoogleCloudAiplatformV1PipelineTaskDetailPipelineTaskStatus&gt;**](GoogleCloudAiplatformV1PipelineTaskDetailPipelineTaskStatus.md) | Output only. A list of task status. This field keeps a record of task status evolving over time. |  [optional] [readonly] |
|**startTime** | **String** | Output only. Task start time. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. State of the task. |  [optional] [readonly] |
|**taskId** | **String** | Output only. The system generated ID of the task. |  [optional] [readonly] |
|**taskName** | **String** | Output only. The user specified name of the task that is defined in pipeline_spec. |  [optional] [readonly] |



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



