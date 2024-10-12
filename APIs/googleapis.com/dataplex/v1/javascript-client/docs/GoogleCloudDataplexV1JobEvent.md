# CloudDataplexApi.GoogleCloudDataplexV1JobEvent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endTime** | **String** | The time when the job ended running. | [optional] 
**executionTrigger** | **String** | Job execution trigger. | [optional] 
**jobId** | **String** | The unique id identifying the job. | [optional] 
**message** | **String** | The log message. | [optional] 
**retries** | **Number** | The number of retries. | [optional] 
**service** | **String** | The service used to execute the job. | [optional] 
**serviceJob** | **String** | The reference to the job within the service. | [optional] 
**startTime** | **String** | The time when the job started running. | [optional] 
**state** | **String** | The job state on completion. | [optional] 
**type** | **String** | The type of the job. | [optional] 



## Enum: ExecutionTriggerEnum


* `EXECUTION_TRIGGER_UNSPECIFIED` (value: `"EXECUTION_TRIGGER_UNSPECIFIED"`)

* `TASK_CONFIG` (value: `"TASK_CONFIG"`)

* `RUN_REQUEST` (value: `"RUN_REQUEST"`)





## Enum: ServiceEnum


* `SERVICE_UNSPECIFIED` (value: `"SERVICE_UNSPECIFIED"`)

* `DATAPROC` (value: `"DATAPROC"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `SUCCEEDED` (value: `"SUCCEEDED"`)

* `FAILED` (value: `"FAILED"`)

* `CANCELLED` (value: `"CANCELLED"`)

* `ABORTED` (value: `"ABORTED"`)





## Enum: TypeEnum


* `TYPE_UNSPECIFIED` (value: `"TYPE_UNSPECIFIED"`)

* `SPARK` (value: `"SPARK"`)

* `NOTEBOOK` (value: `"NOTEBOOK"`)




