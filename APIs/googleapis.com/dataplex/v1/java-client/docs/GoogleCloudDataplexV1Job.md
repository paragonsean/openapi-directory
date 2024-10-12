

# GoogleCloudDataplexV1Job

A job represents an instance of a task.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endTime** | **String** | Output only. The time when the job ended. |  [optional] [readonly] |
|**executionSpec** | [**GoogleCloudDataplexV1TaskExecutionSpec**](GoogleCloudDataplexV1TaskExecutionSpec.md) |  |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Output only. User-defined labels for the task. |  [optional] [readonly] |
|**message** | **String** | Output only. Additional information about the current state. |  [optional] [readonly] |
|**name** | **String** | Output only. The relative resource name of the job, of the form: projects/{project_number}/locations/{location_id}/lakes/{lake_id}/tasks/{task_id}/jobs/{job_id}. |  [optional] [readonly] |
|**retryCount** | **Integer** | Output only. The number of times the job has been retried (excluding the initial attempt). |  [optional] [readonly] |
|**service** | [**ServiceEnum**](#ServiceEnum) | Output only. The underlying service running a job. |  [optional] [readonly] |
|**serviceJob** | **String** | Output only. The full resource name for the job run under a particular service. |  [optional] [readonly] |
|**startTime** | **String** | Output only. The time when the job was started. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. Execution state for the job. |  [optional] [readonly] |
|**trigger** | [**TriggerEnum**](#TriggerEnum) | Output only. Job execution trigger. |  [optional] [readonly] |
|**uid** | **String** | Output only. System generated globally unique ID for the job. |  [optional] [readonly] |



## Enum: ServiceEnum

| Name | Value |
|---- | -----|
| SERVICE_UNSPECIFIED | &quot;SERVICE_UNSPECIFIED&quot; |
| DATAPROC | &quot;DATAPROC&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| RUNNING | &quot;RUNNING&quot; |
| CANCELLING | &quot;CANCELLING&quot; |
| CANCELLED | &quot;CANCELLED&quot; |
| SUCCEEDED | &quot;SUCCEEDED&quot; |
| FAILED | &quot;FAILED&quot; |
| ABORTED | &quot;ABORTED&quot; |



## Enum: TriggerEnum

| Name | Value |
|---- | -----|
| TRIGGER_UNSPECIFIED | &quot;TRIGGER_UNSPECIFIED&quot; |
| TASK_CONFIG | &quot;TASK_CONFIG&quot; |
| RUN_REQUEST | &quot;RUN_REQUEST&quot; |



