# CloudDataplexApi.GoogleCloudDataplexV1Job

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endTime** | **String** | Output only. The time when the job ended. | [optional] [readonly] 
**executionSpec** | [**GoogleCloudDataplexV1TaskExecutionSpec**](GoogleCloudDataplexV1TaskExecutionSpec.md) |  | [optional] 
**labels** | **{String: String}** | Output only. User-defined labels for the task. | [optional] [readonly] 
**message** | **String** | Output only. Additional information about the current state. | [optional] [readonly] 
**name** | **String** | Output only. The relative resource name of the job, of the form: projects/{project_number}/locations/{location_id}/lakes/{lake_id}/tasks/{task_id}/jobs/{job_id}. | [optional] [readonly] 
**retryCount** | **Number** | Output only. The number of times the job has been retried (excluding the initial attempt). | [optional] [readonly] 
**service** | **String** | Output only. The underlying service running a job. | [optional] [readonly] 
**serviceJob** | **String** | Output only. The full resource name for the job run under a particular service. | [optional] [readonly] 
**startTime** | **String** | Output only. The time when the job was started. | [optional] [readonly] 
**state** | **String** | Output only. Execution state for the job. | [optional] [readonly] 
**trigger** | **String** | Output only. Job execution trigger. | [optional] [readonly] 
**uid** | **String** | Output only. System generated globally unique ID for the job. | [optional] [readonly] 



## Enum: ServiceEnum


* `SERVICE_UNSPECIFIED` (value: `"SERVICE_UNSPECIFIED"`)

* `DATAPROC` (value: `"DATAPROC"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `RUNNING` (value: `"RUNNING"`)

* `CANCELLING` (value: `"CANCELLING"`)

* `CANCELLED` (value: `"CANCELLED"`)

* `SUCCEEDED` (value: `"SUCCEEDED"`)

* `FAILED` (value: `"FAILED"`)

* `ABORTED` (value: `"ABORTED"`)





## Enum: TriggerEnum


* `TRIGGER_UNSPECIFIED` (value: `"TRIGGER_UNSPECIFIED"`)

* `TASK_CONFIG` (value: `"TASK_CONFIG"`)

* `RUN_REQUEST` (value: `"RUN_REQUEST"`)




