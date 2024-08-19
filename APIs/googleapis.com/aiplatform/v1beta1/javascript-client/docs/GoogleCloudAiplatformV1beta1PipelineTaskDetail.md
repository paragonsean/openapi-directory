# VertexAiApi.GoogleCloudAiplatformV1beta1PipelineTaskDetail

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. Task create time. | [optional] [readonly] 
**endTime** | **String** | Output only. Task end time. | [optional] [readonly] 
**error** | [**GoogleRpcStatus**](GoogleRpcStatus.md) |  | [optional] 
**execution** | [**GoogleCloudAiplatformV1beta1Execution**](GoogleCloudAiplatformV1beta1Execution.md) |  | [optional] 
**executorDetail** | [**GoogleCloudAiplatformV1beta1PipelineTaskExecutorDetail**](GoogleCloudAiplatformV1beta1PipelineTaskExecutorDetail.md) |  | [optional] 
**inputs** | [**{String: GoogleCloudAiplatformV1beta1PipelineTaskDetailArtifactList}**](GoogleCloudAiplatformV1beta1PipelineTaskDetailArtifactList.md) | Output only. The runtime input artifacts of the task. | [optional] [readonly] 
**outputs** | [**{String: GoogleCloudAiplatformV1beta1PipelineTaskDetailArtifactList}**](GoogleCloudAiplatformV1beta1PipelineTaskDetailArtifactList.md) | Output only. The runtime output artifacts of the task. | [optional] [readonly] 
**parentTaskId** | **String** | Output only. The id of the parent task if the task is within a component scope. Empty if the task is at the root level. | [optional] [readonly] 
**pipelineTaskStatus** | [**[GoogleCloudAiplatformV1beta1PipelineTaskDetailPipelineTaskStatus]**](GoogleCloudAiplatformV1beta1PipelineTaskDetailPipelineTaskStatus.md) | Output only. A list of task status. This field keeps a record of task status evolving over time. | [optional] [readonly] 
**startTime** | **String** | Output only. Task start time. | [optional] [readonly] 
**state** | **String** | Output only. State of the task. | [optional] [readonly] 
**taskId** | **String** | Output only. The system generated ID of the task. | [optional] [readonly] 
**taskName** | **String** | Output only. The user specified name of the task that is defined in pipeline_spec. | [optional] [readonly] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `PENDING` (value: `"PENDING"`)

* `RUNNING` (value: `"RUNNING"`)

* `SUCCEEDED` (value: `"SUCCEEDED"`)

* `CANCEL_PENDING` (value: `"CANCEL_PENDING"`)

* `CANCELLING` (value: `"CANCELLING"`)

* `CANCELLED` (value: `"CANCELLED"`)

* `FAILED` (value: `"FAILED"`)

* `SKIPPED` (value: `"SKIPPED"`)

* `NOT_TRIGGERED` (value: `"NOT_TRIGGERED"`)




